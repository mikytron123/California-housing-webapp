from pathlib import Path
from testcontainers.core.container import DockerContainer
from testcontainers.core.image import DockerImage
from testcontainers.generic import ServerContainer
from python_on_whales import DockerClient
import os
import sys
import pytest
import pandas as pd

path = os.getcwd()
parent_path = Path().parent.resolve()

if str(parent_path) not in sys.path:
    sys.path.append(str(parent_path))
if path not in sys.path:
    sys.path.append(path)


@pytest.fixture(scope="module")
def server_container():
    
    cur_path = Path(__file__).parent.resolve()
    print(cur_path)
    print("------------------")
    alloy_path = cur_path.parent.parent / "alloy"
    print(alloy_path)
    alloy_image = DockerImage(path=str(alloy_path))
    alloy_image.build()

    alloy_container = DockerContainer(image=str(alloy_image))
    alloy_container.with_exposed_ports(4318)
    alloy_container.start()

    docker = DockerClient(compose_files=[str(cur_path.parent.parent / "docker-compose.yml")])
    docker.compose.build(services=["api"])
    # make sure to build api image before hand
    api_image = "mlapp-api:latest"
    api_port = 3010
    server = ServerContainer(port=api_port, image=str(api_image))
    server.with_env("ALLOY_HOST", alloy_container.get_container_host_ip())
    server.with_env("ALLOY_PORT", alloy_container.get_exposed_port(4318))
    server.with_env("API_PORT",str(api_port))
    server.start()
    yield server

    server.stop()
    alloy_container.stop()
    alloy_image.remove()


def test_predict_endpoint(server_container):
    # wait_for_logs(server_container, """Starting production HTTP BentoServer from "service:Housing_Regressor" listening on http://localhost:3008""")
    server_container.get_api_url = lambda: server_container._create_connection_url()
    client = server_container.get_client()
    cur_path = Path(__file__).resolve()

    csv_path = cur_path.parent.parent.parent / "X_head.csv"
    df = pd.read_csv(str(csv_path))

    payload = {"input_data": df.to_dict(orient="records")}
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
