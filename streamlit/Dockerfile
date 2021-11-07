FROM python:3.8

WORKDIR /usr/src/app
ENV PYTHONUNBUFFERED=0
COPY requirements.txt ./
RUN pip install --no-cache-dir -r ./requirements.txt

COPY . /usr/src/app
ENTRYPOINT ["streamlit", "run"]

CMD ["app.py"]
