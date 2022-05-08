import re
from turtle import title
from urllib import response
import requests

url1 = "https://www.googleapis.com/youtube/v3/videos"
url2 = "https://www.googleapis.com/youtube/v3/commentThreads"


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


#response1에 동영상 정보 저장
response1_snippet = requests.get(url1, params=params1_snippet).json()['items']
response1_statistics = requests.get(url1,params=params1_statistics).json()['items']

#video_List에 동영상 ID 저장
video_List = []
video_rank = [] 
video_title = []
video_des = []
video_channelTitle = []
video_viewCount = []

for idx in range(len(response1_snippet)):
    video_List.append(response1_snippet[idx]['id'])
    #video_rank.append() <- 순위 어떻게 불러오는지 모르겠네욤,,
    video_title.append(response1_snippet[idx]['snippet']['title'])
    video_des.append(response1_snippet[idx]['snippet']['description'])
    video_channelTitle.append(response1_snippet[idx]['snippet']['channelTitle'])
    video_viewCount.append(response1_statistics[idx]['statistics']['viewCount'])



#print(video_List)
#print(video_rank)
#print(video_title)
#print(video_des)
#print(video_channelTitle)
#print(video_viewCount)

for id in video_List:

    params2 = {
        "key": "AIzaSyCBrZ5VTkDJ10shyRllMxfnj5AN6Fo-NEY",
        "part": ["snippet"],
        "maxResults": 100,
        "videoId": id
    }

    #response2에 댓글 정보 저장
    response2 = requests.get(url2, params=params2).json()['items']

    #comment_List에 topLevelComment 저장
    comment_List = []
    for item in response2:
        comment_List.append(item['snippet']['topLevelComment']['snippet']['textDisplay'])

    #print(comment_List)

    # 이 밑에 구름 코드 적으면 될 거 같아요!!
        

