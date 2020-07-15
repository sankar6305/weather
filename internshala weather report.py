#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pandas import DataFrame,Series
import pandas as pd
import numpy as np


# In[6]:


weather={
    "request": {
        "type": "City",
        "query": "San Francisco, United States of America",
        "language": "en",
        "unit": "m"
    },
    "location": {
        "name": "San Francisco",
        "country": "United States of America",
        "region": "California",
        "lat": "37.775",
        "lon": "-122.418",
        "timezone_id": "America/Los_Angeles",
        "localtime": "2019-09-03 05:35",
        "localtime_epoch": 1567488900,
        "utc_offset": "-7.0"
    },
    "current": {
        "observation_time": "12:35 PM",
        "temparature": 16,
        "weather_code": 122,
        "weather_icons": [
            "https://assets.weatherstack.com/images/symbol.png"
        ],
        "weather_descriptions": [
            "Overcast"
        ],
    "wind_speed": 17,
    "wind_degree": 260,
    "wind_dir": "W",
    "pressure": 1016,
    "precip": 0,
    "humidity": 87,
    "cloudcover": 100,
    "feelslike": 16,
    "uv_index": 0,
    "visibility": 16
    }
}


# In[7]:


DataFrame(weather)


# In[8]:


contineu=input("If you want to update the temperature , type 'yes' otherwise type 'no',what is your option: ")


# In[16]:


if contineu=='yes':
    update=input("What is the updated value:")
    weather['current']['temparature']=update
else:
    pass


# In[17]:


DataFrame(weather)


# In[ ]:




