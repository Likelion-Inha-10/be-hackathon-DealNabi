import re
from turtle import title
from urllib import response
import requests
from get_id import get_id 

def get_info(n):
    url1 = "https://www.googleapis.com/youtube/v3/videos"

    params1_snippet = {
    "key": "AIzaSyCBrZ5VTkDJ10shyRllMxfnj5AN6Fo-NEY",
    "part": ["snippet"],
    "chart": "mostPopular",
    "regionCode": "KR",
    "maxResults": 100
    }

    params1_statistics = {
        "key": "AIzaSyCBrZ5VTkDJ10shyRllMxfnj5AN6Fo-NEY",
        "part": ["statistics"],
        "chart": "mostPopular",
        "regionCode": "KR",
        "maxResults": 100
    }

    response1_snippet = requests.get(url1, params=params1_snippet).json()['items']
    response1_statistics = requests.get(url1,params=params1_statistics).json()['items']

    video_title = []
    video_des = []
    video_channelTitle = []
    video_viewCount = []

    for idx in range(len(response1_snippet)):
        video_title.append(response1_snippet[idx]['snippet']['title'])
        video_des.append(response1_snippet[idx]['snippet']['description'])
        video_channelTitle.append(response1_snippet[idx]['snippet']['channelTitle'])
        video_viewCount.append(response1_statistics[idx]['statistics']['viewCount'])


    return video_title,video_des,video_channelTitle,video_viewCount
    