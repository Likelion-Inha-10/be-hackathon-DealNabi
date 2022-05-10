import re
from turtle import title
from urllib import response
import requests

from get_id import get_id 
from get_info import get_info
from get_comment import get_comment
from wdcloud import wordcloud_from_text

import os

video_list=get_id(100)
video_title,video_des,video_channelTitle,video_viewCount=get_info(100)
get_comment(video_list)

#단어구름 작업 ------------------------------------------------------------------------------------------------------
#Comment_List.txt 입력받아 단어구름 이미지 출력
if __name__ == '__main__':
     wordcloud_from_text (input_file='Comment_List.txt')
#-------------------------------------------------------------------------------------------------------------------

#단어구름 작업 후 텍스트파일 삭제
os.remove('./Comment_List.txt')