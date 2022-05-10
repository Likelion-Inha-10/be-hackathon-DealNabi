# from msilib import sequence
import requests
from bs4 import BeautifulSoup

def get_id(n):

    url = "https://www.googleapis.com/youtube/v3/videos"
    
    params = {
        "key": "AIzaSyC-EdQIhOL5j0VcUeVgZyARJZOt3cBtzd0",
        "part": ["snippet"],
        "chart": "mostPopular",
        "regionCode": "KR",
        "maxResults": n
    }

    response = requests.get(url, params=params).json()['items']
    video_List=[]
    for idx in range(len(response)):
        video_List.append(response[idx]['id'])

    return(video_List)
