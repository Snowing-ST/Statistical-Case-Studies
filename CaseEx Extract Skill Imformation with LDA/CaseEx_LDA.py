#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 17:29:39 2018
提取招聘信息中的技能要求
以数据分析实习为例

@author: situ
"""


#LDA-------------------------------------------------------------------
from gensim import corpora
import os
import tempfile
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from gensim.models import LdaModel


os.chdir("/Users/situ/Documents/EDA/final")


def loadDataset(myfile):
    '''导入文本数据集'''
    f = open(myfile,'r',encoding = "utf-8")
    dataset = []
    for line in f.readlines():
#        print(line)
        dataset.append(line.strip().split())

    f.close()
    return dataset


clean_text4 = loadDataset("clean_text.txt")
TEMP_FOLDER = tempfile.gettempdir()
print('Folder "{}" will be used to save temporary dictionary and corpus.'.format(TEMP_FOLDER))
dictionary = corpora.Dictionary(clean_text4)
dictionary.save(os.path.join(TEMP_FOLDER, 'deerwester.dict'))  # store the dictionary, for future reference
print(dictionary)
print(dictionary.token2id)
corpus = [dictionary.doc2bow(text) for text in clean_text4]

corpora.MmCorpus.serialize(os.path.join(TEMP_FOLDER, 'deerwester.mm'), corpus)  # store to disk, for later use
len(corpus)

print('Number of unique tokens: %d' % len(dictionary))
print('Number of documents: %d' % len(corpus))


# Set training parameters.
num_topics = 5
#10 8
chunksize = 2000
passes = 20
iterations = 400
eval_every = None  # Don't evaluate model perplexity, takes too much time.

# Make a index to word dictionary.
temp = dictionary[0]  # This is only to "load" the dictionary.
id2word = dictionary.id2token

model = LdaModel(corpus=corpus, id2word=id2word, chunksize=chunksize, \
                       alpha='auto', eta='auto', \
                       iterations=iterations, num_topics=num_topics, \
                       passes=passes, eval_every=eval_every)

top_topics = model.top_topics(corpus,5)

# Average topic coherence is the sum of topic coherences of all topics, divided by the number of topics.
avg_topic_coherence = sum([t[1] for t in top_topics]) / num_topics
print('Average topic coherence: %.4f.' % avg_topic_coherence)

from pprint import pprint
pprint(top_topics)


model.print_topic(1,30)
model.print_topic(3,30)

#判断一个训练集文档属于哪个主题
for index, score in sorted(model[corpus[0]], key=lambda tup: -1*tup[1]):
    print("Score: {}\t Topic: {}".format(score, model.print_topic(index, 10)))
    
 
#给训练集输出其属于不同主题概率   
for index, score in sorted(model[corpus[0]], key=lambda tup: -1*tup[1]):
    print(index, score)
    
    
    
    
#判断一个测试集文档属于哪个主题
#unseen_document = [" ".join(text_i) for text_i in clean_text4[130]]
#unseen_document = " ".join(unseen_document)
    
unseen_document = text[130]
"""
还要对文档进行之前的文本预处理
"""


bow_vector = dictionary.doc2bow(unseen_document.split())
for index, score in sorted(model[bow_vector], key=lambda tup: -1*tup[1]):
    print("Score: {}\t Topic: {}".format(score, model.print_topic(index, 10)))

#给每个完整的分词后的文档生成不同主题的得分
import pandas as pd
import numpy as np
data = pd.read_csv("data_with_wordseg.csv",encoding = "gbk")
data.head()
lda_score = np.zeros((data.shape[0],num_topics))
for i in range(len(data["word_seg"])):
    line = data["word_seg"][i]
    bow_vector = dictionary.doc2bow(line.split())
    for index, score in sorted(model[bow_vector], key=lambda tup: -1*tup[1]):
        lda_score[i,index] = score
lda_score[:5,:]
lda_score_df = pd.DataFrame(lda_score,columns = ["lda"+str(i) for i in range(num_topics)])
lda_score_df.head()
data = pd.concat([data, lda_score_df], axis=1)
data.to_csv("data_with_lda_score.csv",index = False,encoding = "gbk")


#LDA visualization---------------------------------------------------

import pyLDAvis
import pyLDAvis.gensim

vis_wrapper = pyLDAvis.gensim.prepare(model,corpus,dictionary)
pyLDAvis.display(vis_wrapper)
pyLDAvis.save_html(vis_wrapper,"lda%dtopics.html"%num_topics)


#pyLDAvis.enable_notebook()
#pyLDAvis.prepare(mds='tsne', **movies_model_data)






#把文本中的技能要求提取出来，然后再对技能类文本聚类，看看能不能聚出高端技能、低端技能

lda_score = np.zeros((len(dataset),num_topics))
for i in range(len(dataset)):
    line = dataset[i]
    bow_vector = dictionary.doc2bow(line.split())
    for index, score in sorted(model[bow_vector], key=lambda tup: -1*tup[1]):
        lda_score[i,index] = score
lda_score[:5,:]
classify = pd.DataFrame(lda_score,columns = ["lda"+str(i) for i in range(num_topics)])
classify.head()




classify = pd.read_csv("clean_text_with_index.csv",encoding = "utf-8-sig")
classify.head()
classify["skill"][classify["lda8"]>0.5]=1


#classify.to_csv("text_labels.csv",index = False,encoding = "gbk")
# 手动把有关大数据、spark、hadoop、hive的样本选上


def skill_text_combine(df):
    """
    相同index的文本合并
    """
   
    index_list = df["index"].unique()
    skill_text = pd.DataFrame({"index":index_list,"skill_text":[""]*len(index_list)})
    for i in index_list:
        skill_text["skill_text"][skill_text["index"]==i] = " ".join(list(df["text"][df["index"]==i]))

    return skill_text

classify = pd.read_csv("text_labels.csv",encoding = "gbk")
skill_text = skill_text_combine(classify[classify["skill"]>0])
skill_text.to_csv("skill_text.csv",index = False,encoding = "gbk")

#一类只出现了msoffice
#一类还出现了sas spss python
#一类是大数据的软件相关


#重新索引，与去重且重新索引后的data合并，看看能不能对应得上，如果有的职位描述没有专业技能句子，赋值0，有的话，根据三种聚类方式进行打分123取平均
data.tail()
#重新索引
data["index"]=list(range(len(data)))

data_with_skill = pd.merge(data,skill_text,how = "outer",on="index")
data_with_skill.head(10)
data_with_skill["score"] = data_with_skill["score"].fillna(0)
data_with_skill.to_csv("data_with_skill.csv",index = False,encoding = "gbk")
