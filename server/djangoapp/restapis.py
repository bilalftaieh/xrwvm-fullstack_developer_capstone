"""
This module is used to interact with the backend and sentiment analyzer services.
"""

import os
import requests
from dotenv import load_dotenv

load_dotenv()

backend_url = os.getenv('backend_url', default="http://localhost:3030")
sentiment_analyzer_url = os.getenv('sentiment_analyzer_url', default="http://localhost:5050/")


def get_request(endpoint, **kwargs):
    """
    This function sends a GET request to the specified endpoint with the provided parameters.
    Returns a JSON response if successful, None otherwise.
    """
    params = ""
    if kwargs:
        for key, value in kwargs.items():
            params = params + key + "=" + value + "&"

    request_url = f"{backend_url}{endpoint}?{params}"

    print(f"GET from {request_url}")
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(request_url, timeout=5)
        return response.json()
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        print("Network exception occurred")
        return None


def analyze_review_sentiments(text):
    """
    This function sends a GET request to the sentiment analyzer service with the provided text.
    Returns a JSON response if successful, None otherwise.
    """
    request_url = f"{sentiment_analyzer_url}analyze/{text}"
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(request_url, timeout=5)
        return response.json()
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        print("Network exception occurred")
        return None


def post_review(data_dict):
    """
    This function sends a POST request to the backend service with the provided data.
    Returns a JSON response if successful, None otherwise.
    """
    request_url = f"{backend_url}/insert_review"
    try:
        response = requests.post(request_url, json=data_dict, timeout=5)
        print(response.json())
        return response.json()
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        print("Network exception occurred")
        return None
