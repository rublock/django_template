import json

import requests


def get_cat(cat_num):
    cat_url = []
    for _ in range(int(cat_num)):
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
        cat_url.append(data[0]["url"])

    return cat_url
