# bento_sevice.py
import pandas as pd
import numpy as np
import bentoml
from sklearn.preprocessing import StandardScaler

model_runner = bentoml.sklearn.get("svr:latest").to_runner()

svr = bentoml.Service("Svr_regressor", runners=[model_runner])


@svr.api(input=bentoml.io.PandasDataFrame(), output=bentoml.io.NumpyNdarray())
def predict(input_series: pd.DataFrame) -> np.ndarray:
    result = model_runner.predict.run(input_series)
    return result
