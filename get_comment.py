import re
from turtle import title
from urllib import response
import requests
from get_id import get_id 

def get_comment(video_list):

    url2 = "https://www.googleapis.com/youtube/v3/commentThreads"

    for id in video_list:

        params2 = {
                "key": "AIzaSyC-EdQIhOL5j0VcUeVgZyARJZOt3cBtzd0",
                "part": ["snippet"],
                "videoId": id
                }

                #response2에 댓글 정보 저장
        response2 = requests.get(url2, params=params2).json()['items']

        #comment_List에 topLevelComment 저장
        comment_List = []
        for item in response2:
            comment_List.append(item['snippet']['topLevelComment']['snippet']['textDisplay'])
        #반복문 comment_List가 생성될 때마다 Comment_List.txt파일로 저장
        with open('Comment_List.txt', 'a', encoding = 'UTF-8') as f:
            for comment in comment_List:
                f.write(comment + '\n')

    return (comment_List)