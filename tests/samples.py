# needs to PEP8 it

SAMPLE_TRUE_MEASURE = {
                              "st": "2014-01-29T15:45:34Z",
                              "ms": {
                                "v": 321,
                                "p": "luminousIntensity",
                                "u": "candela"
                              },
                              "pms": [
                                {
                                  "v": "1",
                                  "p": "QoS",
                                  "u": ""
                                }
                              ]
                            }

SAMPLE_FALSE_MEASURE = {"lol":"false"}


SAMPLE_TRUE_MEASURE_COLLECTION = {
  "data": [
    {
      "st": "2014-01-29T15:45:34Z",
      "ms": {
        "v": 321,
        "p": "luminousIntensity",
        "u": "candela"
      },
      "pms": [
        {
          "v": "1",
          "p": "QoS",
          "u": ""
        }
      ]
    },
    {
      "st": "2014-01-29T15:45:34Z",
      "ms": {
        "v": 0,
        "p": "amount",
        "u": "unit"
      },
      "pms": [
        {
          "v": "1",
          "p": "QoS",
          "u": ""
        }
      ]
    }]
}

SAMPLE_FALSE_MEASURE_COLLECTION = {
    "data": [ 
        {"lol": "lol"},
        {"lol2": "lol2"} 
    ]
}