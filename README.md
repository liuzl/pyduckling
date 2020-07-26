# pyduckling

## Introduction

Python wrapper for facebook [Duckling](https://github.com/facebook/duckling/).

## Install

```sh
pip install git+https://github.com/liuzl/pyduckling
```

## Usage

```python
from duckling import *

ling = Duckling()
text = "我打算明天下午三点去清华智源中心，可能需要开车十五公里"
ret = ling(text)
print(ret)
```

Output in json format:
```json
[
  {
    "body": "明天下午三点",
    "start": 3,
    "value": {
      "values": [
        {
          "value": "2020-07-27T15:00:00.000+08:00",
          "grain": "hour",
          "type": "value"
        }
      ],
      "value": "2020-07-27T15:00:00.000+08:00",
      "grain": "hour",
      "type": "value"
    },
    "end": 9,
    "dim": "time",
    "latent": false
  },
  {
    "body": "十五公里",
    "start": 23,
    "value": {
      "value": 15,
      "type": "value",
      "unit": "kilometre"
    },
    "end": 27,
    "dim": "distance",
    "latent": false
  }
]
```
