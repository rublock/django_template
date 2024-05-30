import time

import requests


def get_cat():
    cat_img = []
    for _ in range(8):
        response = requests.get(
            "https://api.thecatapi.com/v1/images/search",
            params={
                "size": "small",
                "mime_types": "jpg",
                "format": "json",
                "has_breeds": "true",
                "order": "RANDOM",
                "page": "0",
                "limit": "1",
            },
        )
        data = response.json()
        cat_img.append(data[0]["url"])

    return cat_img
