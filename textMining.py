from collections import Counter
from PIL import Image
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

"""
: download java >= 1.9
: sys.version
: download JPype1-JPversion-cp{Pyversoin}-win_{winversion}.whl
: move file to cmd directory
: pip install JPype1-JPversion-cp{Pyversoin}-win_{winversion}.whl
: pip install konlpy

[Error] 
: SystemError: java.nio.file.InvalidPathException: Illegal char <*> at index 52:
: solution : https://stackoverflow.com/questions/65842567/systemerror-java-nio-file-invalidpathexception
"""

import os
from konlpy.tag import Okt
import nltk         # natural language tool kit
from nltk import tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer   # 사전 기반 감성 분석툴
#nltk.download('punkt')
#nltk.download('vader_lexicon')

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator # wordcloud 라이브러리


def get_morphs(news_list):

    #print(df_data['title'])

    text_list = news_list['content']   #Series
    print(text_list)    
    okt = Okt()
    total_sentence = []

    # 해당 날짜 뉴스 키워드 추출
    for date in set(news_list['date']):
        date_news_list = news_list[news_list.date == date]
        
        total_sentence = ' '.join(title for title in date_news_list['title'])
        total_sentence = ' '.join(desc for desc in date_news_list['content']) 
        total_sentence = okt.morphs(total_sentence, norm=True, stem=True)     #형태소 분석(pos tagger)
    
        #total_sentence.vocab()    # 빈도수 체크 FreqDist객체에 담긴다.
    
        # 불용어 처리
        stopword=[':','"', ',', '이','는','은','저','데','근데', '그러나','그리고','는데','하는데','한데','가','저', '=', '.','의', '있다', '을','를', '에','게','에게','에서','에는','돼다','로도','와', '으로']
        total_sentence = [i for i in total_sentence if i not in stopword]

        # TOP 50 글자
        counter = Counter(total_sentence)
        total_sentence_50 = counter.most_common(50)
    # end : for set(news_list['date'])

        # word cloud 생성
        #cloud_mask = np.array(Image.open('마스크이미지.png'))
        wordcloud = WordCloud(background_color='black', max_font_size=20).generate(total_sentence)

        plt.figure()
        plt.axis('off')
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.show()



path_dir = 'C:/work/project/NewsCrawler/data/news'
file_list = os.listdir(path_dir)

for file_name in file_list:
    df_data = pd.read_csv(f'{path_dir}/{file_name}')
    get_morphs(df_data)


# print(okt.normalize(text))  # 정규화 처리
# print(okt.phrases(text))   # 어구 추출
# print(okt.morphs(text))   #형태소 분석
# print(okt.nouns(text))  #명사 추출 
# nouns = okt.nouns(text)
# words = nltk.Text(okt.nouns(text))    # 단어를 문장으로 만들기
# print(words) 
# print(set(words.tokens))     # 중복단어 제거



# plt.figure(figsize=(12,7))
# # Plot 한글 글꼴 처리
# path = 'C:\Windows\Fonts\malgunbd.ttf'
# font_name = fm.FontProperties(fname=path).get_name()
# print(font_name)
# plt.rc('font', family=font_name)
#words.plot()

# print(text)
# # 연관있는 단어 추출
# words.concordance('긍정')


# # 사전 기반 감성 분석
# lines_list = tokenize.sent_tokenize(text)    # 텍스트를 문장 단위로 자르기 
# print(lines_list)
# sid = SentimentIntensityAnalyzer()

# result = ""
# for article in text_list:
#     noun_list = okt.nouns(article)
#     noun_line = nltk.Text(noun_list)
#     result += f" {article}" 
#     for sent in tokenize.sent_tokenize(article):
#         ss = sid.polarity_scores(sent)   #문장을 단어별로 분석해서 문장의 pos(긍정)/neu(중립)/neg(부정)에 대한 점수및 종합 점수 계산
        
#         print(article)
#         print(ss['compound'], ss['pos'], ss['neg'], ss['neu'])
#         print()

# print(result)
# print(words)



