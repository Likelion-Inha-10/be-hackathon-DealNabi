# be-hackathon-DealNabi
#### 대한민국에서 인기를 끌고 있는 상위 N개의 동영상에 대하여 
#### 그 "순위", "영상제목", "영상설명", 채널명", "조회수"를 조회하고 
#### 각 영상의 "최상위 댓글"을 각 100개 이상씩 조회하여야 한다.
----------------------------------------------------------------------

### 1. get_id : 실시간 인기 동영상 상위 N개의 동영상 ID 조회
> input: N \
> output: video_list 

### 2. get_info : 실시간 인기 동영상 상위 N개의 "영상 제목", "영상 설명", "채널명", "조회수" 정보 조회
> input: N
> output: video_title,video_des,video_channelTitle,video_viewCount

### 3. get_comment: 해당 동영상의 댓글 조회
> input: video_list
> output: return comment_lsit & comment_list.txt 파일 생성

### 4. wdcloud: 조회된 댓글로 단어구름 형성
> input: comment_list.txt
> output: wordcloud.png

### 5. info2table
> input: video_title,video_des,video_channelTitle,video_viewCount
> output: exl 파일 생성

---------------------------------------------------------------------

