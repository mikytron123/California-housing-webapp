import pandas as pd
import numpy as np
import bentoml
from pydantic import BaseModel, Field
from prometheus_client import Counter
import os

ALLOY_HOST = os.getenv("ALLOY_HOST")
ALLOY_PORT = os.getenv("ALLOY_PORT")

if ALLOY_HOST is None:
    raise Exception("ALLOY_HOST must be set")

if ALLOY_PORT is None:
    raise Exception("ALLOY_PORT must be set")


class HousingData(BaseModel):
    MedInc: float = Field(ge=0.499900, le=15.0001)
    HouseAge: float = Field(ge=1, le=52)
    AveRooms: float = Field(ge=0.846154)
    AveBedrms: float = Field(ge=1 / 3)
    Population: float = Field(ge=3)
    AveOccup: float = Field(ge=0.692308)
    Latitude: float = Field(ge=32.54)
    Longitude: float = Field(ge=-124.35)


prediction_counter = Counter(
    name="model_predictions_total",
    documentation="Total number of predictions made",
    namespace="bentoml_service",
)


@bentoml.service(
    name="svr_regressor",
    workers="cpu_count",
    http={"port": 3010},
    metrics={"enabled": True},
    logging={
        "access": {
            "enabled": True,
            "request_content_length": True,
            "request_content_type": True,
            "response_content_length": True,
            "response_content_type": True,
            "skip_paths": ["/metrics", "/healthz", "/livez", "/readyz"],
        }
    },
    tracing={
        "exporter_type": "otlp",
        "sample_rate": 1.0,
        "otlp": {
            "protocol": "http",
            "endpoint": f"http://{ALLOY_HOST}:{ALLOY_PORT}/v1/traces",
        },
    },
    monitoring={
        "enabled": True,
        "type": "otlp",
        "options": {
            "endpoint": f"http://{ALLOY_HOST}:{ALLOY_PORT}/v1/logs",
            "insecure": True,
        },
    },
)
class Housing_Regressor:
    bento_model = bentoml.models.get("svr:latest")

    def __init__(self):
        self.model = bentoml.sklearn.load_model(self.bento_model)

    @bentoml.api()
    def predict(self, input_data: list[HousingData]) -> list[float]:
        with bentoml.monitor("house_pricer") as mon:
            data = [x.model_dump() for x in input_data]
            mon.log_batch(data, role="feature", data_type="numerical", name="feat")
            df = pd.DataFrame(data)
            rv = self.model.predict(df)
            prediction_counter.inc(amount=len(rv))
            mon.log_batch(
                rv.tolist(), role="prediction", data_type="numerical", name="pred"
            )
            return np.asarray(rv)
