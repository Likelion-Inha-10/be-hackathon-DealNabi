import pandas as pd

def info2table(video_title,video_des,video_channelTitle,video_viewCount):

    data = {'영상제목': video_title,
            '영상설명': video_des,
            '채널명': video_channelTitle,
            '조회수': video_viewCount}
    df = pd.DataFrame(data)

    df.to_excel('info.xlsx', encoding='utf-8-sig')