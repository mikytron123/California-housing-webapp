# BentoML Service "svr_regressor"

This is a Machine Learning Service created with BentoML. 

## Inference APIs:

It contains the following inference APIs:

### /predict

* Input: PandasDataFrame
* Output: NumpyNdarray


## Customize This Message

This is the default generated `bentoml.Service` doc. You may customize it in your Bento
build file, e.g.:

```yaml
service: "image_classifier.py:svc"
description: "file: ./readme.md"
labels:
  foo: bar
  team: abc
docker:
  distro: debian
  gpu: True
python:
  packages:
    - tensorflow
    - numpy
```
