# be-hackathon-DealNabi
#### 대한민국에서 인기를 끌고 있는 상위 N개의 동영상에 대하여 
#### 그 "순위", "영상제목", "영상설명", 채널명", "조회수"를 조회하고 
#### 각 영상의 "최상위 댓글"을 각 100개 이상씩 조회하여야 한다.
----------------------------------------------------------------------

## 클래스 별 기능

### 1. get_id : 실시간 인기 동영상 상위 N개의 동영상 ID 조회
> input: N \
> output: video_list 

### 2. get_info : 실시간 인기 동영상 상위 N개의 "영상 제목", "영상 설명", "채널명", "조회수" 정보 조회
> input: N \
> output: video_title,video_des,video_channelTitle,video_viewCount

### 3. get_comment: 해당 동영상의 댓글 조회
> input: video_list \
> output: return comment_lsit & comment_list.txt 파일 생성

### 4. wdcloud: 조회된 댓글로 단어구름 형성
> input: comment_list.txt \
> output: wordcloud.png

### 5. info2table
> input: video_title,video_des,video_channelTitle,video_viewCount \
> output: exl 파일 생성

---------------------------------------------------------------------

## 고난과 역경 . . .

### 1. python 버전 통일 (downgrade)
> sol1 : 삭제 후 재설치 (반드시 Add Python to PATH 체크박스 표시!!!) \
> sol2 : 가상환경 

### 2. request의 사용법
> API 별 Required parameters 체크 필수 ! \
> response 에서 복잡한 다중 딕셔너리 형식 받을 때 주의! ex. snippet
> ![image](https://user-images.githubusercontent.com/87406368/167616837-f28af553-d79b-44a5-9784-776922e82a06.png)


### 3. selenium 이냐, request 냐 ?!
> selenium : 브라우저 상에서 마우스를 내리면서 동적으로 생성된 정보를 가져오는 툴
> request : request, params, response 를 통해 공공 데이터 API 이용
