# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 20:56:10 2018
分时间段 提取新闻文本 词频矩阵 词云图

@author: situ
"""
import pandas as pd
import os
import re
import jieba
import csv
import numpy as np
import collections
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import PIL.Image as Image

os.chdir("E:/graduate/class/Statistical Case Studies/homework7")
path = "E:/graduate/class/Statistical Case Studies/homework7/rawdata"
def batch_read_csv(path):   
    #filenames = os.listdir("./rawdata")
    filenames = os.listdir(path)
    for i in list(range(len(filenames))):
        abfilename = os.path.join(path,filenames[i])
        if i==0:
            df = pd.read_csv(abfilename,encoding = "gb18030")
        if i>0:
            df = df.append(pd.read_csv(abfilename,encoding = "gb18030"))
    return df
df = batch_read_csv(path)
df.head(5)
df.shape

df.to_csv("alldata.csv",index = False,encoding = "gb18030")

#删除重复内容
sum(df["title"].duplicated()) 
df[df["title"].duplicated()]

df = df.drop_duplicates(["title","detail"])
#内容为空，则把摘要补过去
df["detail"][df["detail"].isnull()] = df["title"][df["detail"].isnull()]+"\n"+df["abstract"][df["detail"].isnull()]



#从这里开始看起----------------------------------------------------------------
"""
从百度百科查到的：

美国商务部：
2018年4月16日晚，美国商务部发布公告称，美国政府在未来7年内禁止中兴通讯向美国企业购买敏感产品。

中华人民共和国商务部：
2018年4月17日，商务部新闻发言人回应指出，中方一贯要求中国企业在海外经营过程中，遵守东道国的法律政策，合法合规开展经营。中兴公司与数百家美国企业开展了广泛的贸易投资合作，为美国贡献了数以万计的就业岗位。希望美方依法依规，妥善处理，并为企业创造公正、公平、稳定的法律和政策环境。商务部将密切关注事态进展，随时准备采取必要措施，维护中国企业的合法权益。 [5] 
2018年4月19日，针对中兴被美国“封杀”的问题，商务部新闻发言人高峰在新闻发布会上表示，中方密切关注进展，随时准备采取必要措施，维护中国企业合法权益。 [1] 

中兴通讯：
2018年4月20日，中兴通讯发布关于美国商务部激活拒绝令的声明，称在相关调查尚未结束之前，美国商务部工业与安全局执意对公司施以最严厉的制裁，对中兴通讯极不公平，“不能接受！”
2018年4月22日晚间，中兴通讯公告，2016年4月以来，公司吸取过去在出口管制合规方面的教训，高度重视出口管制合规工作，把合规视为公司战略的基石和经营的前提及底线。美国商务部工业与安全局激活拒绝令，公司已经且正在采取措施以遵守该拒绝令。公司积极与相关方沟通以及寻求解决方案。

划分四个时间段
4月17日
4月18-4月19
4月20-4月23
4月24至今
"""

os.chdir("E:/graduate/class/Statistical Case Studies/homework7")
df = pd.read_csv("alldata.csv",encoding = "gb18030")
df.head(5)

#period1
def get_text(data):
    text=data["detail"]
    text = text.dropna() 
    len(text)
    text=[t.encode('utf-8').decode("utf-8") for t in text] 
    return text

def get_stop_words(file='stopWord.txt'):
    file = open(file, 'rb').read().decode('utf8').split(',')
    file = [line.strip() for line in file]
    return set(file)                                         #查分停用词函数


def rm_tokens(words):                                        # 去掉一些停用词和完全包含数字的字符串
    words_list = list(words)
    stop_words = get_stop_words()
    for i in range(words_list.__len__())[::-1]:
        if words_list[i] in stop_words:                      # 去除停用词
            words_list.pop(i)
        elif words_list[i].isdigit():
            words_list.pop(i)
    return words_list



def rm_char(text):
    text = re.sub('\x01', '', text)                        #全角的空白符
    text = re.sub('\u3000', '', text) 
    text = re.sub(r"[，\)、(↓%：·；▲ \s+]","", text.encode("utf-8").decode("utf-8")) 
    text = re.sub(r"[\n\da-z+（）《》↗><‘’“”.-]","",text,flags=re.I)
    return text

def convert_doc_to_wordlist(str_doc, cut_all):
    sent_list = str_doc.split('\n')
    sent_list = map(rm_char, sent_list)                       # 去掉一些字符，例如\u3000
    word_2dlist = [rm_tokens(jieba.cut(part, cut_all=cut_all))
                   for part in sent_list]                     # 分词
    word_list = sum(word_2dlist, [])
    return word_list

def get_period_i(data,clean_text,i):
    j=0
    period_i=[]
    for j in list(range(len(clean_text))):
        if data['period'][j] == i:
            period_i.extend(clean_text[j])
    return period_i



def word_count(period_i,i):
#词频统计,转化成矩阵
    word_count = np.array(collections.Counter(period_i).most_common())
#    print (word_count[:10])
    csvfile = open("period_"+str(i)+".csv",'w',newline='') 
    writer = csv.writer(csvfile)
    for row in word_count[0:1000,]:
        writer.writerow([row[0], row[1]])
    csvfile.close()

def draw_wordcloud(period_i,i):
    word_count = np.array(collections.Counter(period_i).most_common())
    tf = {word_count[j][0]: int(word_count[j][1]) for j in range(len(word_count))} #词频统计词典
    coloring = np.array(Image.open("zhongxing.jpg")) #图片    
    my_wordcloud = WordCloud(background_color="white", max_words=2000,
                             mask=coloring, max_font_size=60, random_state=42, scale=2,
                             font_path=os.environ.get("FONT_PATH", "C:/Windows/Fonts/simfang.ttf"))
    my_wordcloud.fit_words(tf)
    image_colors = ImageColorGenerator(coloring)
    plt.figure(figsize=(18.5,10.5)) 
    plt.imshow(my_wordcloud.recolor(color_func=image_colors))
    plt.xticks([]),plt.yticks([]) #隐藏坐标线 
    plt.axis("off")
    plt.imshow(my_wordcloud)
    plt.savefig("period_"+str(i)+"_wordcloud.jpg")
    plt.show()
    
def main():
    os.chdir("E:/graduate/class/Statistical Case Studies/homework7")
    clean_text=[convert_doc_to_wordlist(line,cut_all=False) for line in get_text(df)]
    num_period = np.unique(df["period"])
    for i in num_period:
        period_i = get_period_i(df,clean_text,i)
        word_count(period_i,i)
        draw_wordcloud(period_i,i)
    
if __name__ == '__main__':
    main()    
    