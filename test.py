from msilib import sequence
import requests
from bs4 import BeautifulSoup
import pandas as pd

# keyword='아이유'
# url='https://www.youtube.com/results?search_query=' + keyword

def get_id(n):

    url = "https://www.googleapis.com/youtube/v3/videos"


    params = {
        "key": "AIzaSyC-EdQIhOL5j0VcUeVgZyARJZOt3cBtzd0",
        "part": "id",
        "chart": "mostPopular",
        "regionCode": "KR",
        "maxResults": n
    }

    response = requests.get(url, params=params).json()['items']
    video_List=[]
    for idx in range(len(response)):
        video_List.append(response[idx]['id'])

    return(video_List)


# html=response.text
# soup=BeautifulSoup(html,'html.parser')

# keyList=params['part'].keys()

# for item in keyList:
#     print(item,snippet[item])

# list=soup.get("part{title}")
# print(list)



# my_titles=soup.select('h3>a')
# title=[]
# Url=[]

# for idx in my_titles:
#     if idx.get('href')[:7]!='/watch?':
#         pass
#     else:
#         title.append(idx.text)
#         url.append(idx.get('href'))

# title_list=pd.DataFrame(Url,columns=['url'])        
# title_list['title']=title



