import re
from turtle import title
from urllib import response
import requests

# 단어구름에 필요한 작업들 ---------------------------------------------------------------------------------------------
from collections import Counter
from wordcloud import WordCloud
from konlpy.tag import Okt
import nltk

def wordcloud_from_text(input_file, output_file='wordcloud.png'):
    # get text from file
    try:
        with open(input_file, "rb") as f:
            text=f.read().decode('utf8')
    except Exception as e:      #에러 발생 메세지 출력
        print ('wordcloud_from_text() - %s' %(e))
        return        

    # 예외 처리
    if text == None:    #input 파일에 텍스트가 없는 경우
        print ('wordcloud_from_text() text is None')
        return

    # get noun list
    noun_list = get_noun_list(text)

    # 예외 처리 2
    if len(noun_list) < 10:     #단어 빈도수가 10개가 안 되는 경우
        print ('wordcloud_from_text() - Too small noun list')
        return

    # Generate a word cloud image
    wc = WordCloud(font_path = './gulim.ttf',
                        background_color = 'white',
                        width=512, height=512,
                        max_font_size=500,
                        max_words=1000)
    wc.generate_from_frequencies(dict(noun_list))   #리스트에 담긴 튜플형태인 noun_list를 딕셔너리로 변환 
    # Save to png
    wc.to_file(output_file)
    print ('Create WordCloud:', output_file)

def get_noun_list(text, method=0):    
    # Sentence to token
    if method == 0:
        # 한국어
        noun = tokenizer_konlpy(text)
    else:
        # 영어
        noun = tokenizer_nltk(text)

    # count word
    count = Counter(noun)

    # get most frequent words
    noun_list = count.most_common(3000)     #3000개의 최빈값 추출
    return noun_list

def tokenizer_nltk(text):
    # NNP: 단수 고유명사, VB: 동사, VBP: 동사 현재형, TO: to 전치사, NN: 명사(단수형 혹은 집합형), DT: 관형사
    is_noun = lambda pos : (pos[:2] == 'NN' or pos[:2] == 'NNP')
    tokenized = nltk.word_tokenize(text)    
    return [word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)]    #pos_tag: 튜플 형태로 품사 정리

def tokenizer_konlpy(text):
    okt = Okt()
    return [word for word in okt.nouns(text) if len(word) >1]       #nouns: 명사 데이터를 리스트로 받음

#-------------------------------------------------------------------------------------------------------------------

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

#단어구름 작업 --------------------------------------------------------------------------------------------------------

    #반복문 comment_List가 생성될 때마다 Comment_List.txt파일로 저장
    with open('Comment_List.txt', 'a', encoding = 'UTF-8') as f:
        for comment in comment_List:
            f.write(comment + '\n')

#Comment_List.txt 입력받아 단어구름 이미지 출력
if __name__ == '__main__':
     wordcloud_from_text (input_file='Comment_List.txt')
#-------------------------------------------------------------------------------------------------------------------