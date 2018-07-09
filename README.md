# Statistical-Case-Studies
- 应用统计案例分析课程作业
- 指导老师：[feng.li](https://github.com/feng-li)

## [Lab1](http://nbviewer.jupyter.org/github/Snowing-ST/Statistical-Case-Studies/blob/master/Lab1%20Data%20Structures.ipynb)
- 1. 读取文本数据、文本数据预处理、统计词频、保存词频表至csv
    - 1.1 Read a text file
    - 1.2 Do the necessary cleaning
    - 1.3 Convert to other format（word count）
    - 1.4 Export to csv format
    
- 2. 读取鸢尾花数据、描述统计、scipy做线性代数运算
    - 2.1 Read a csv flie
    - 2.2 Do the description（不使用np、pd的描述统计）
    - 2.3 Convert it to dataframe
    - 2.4 Try some linear algebra（用scipy做矩阵转置、逆、行列式值、最小二乘、广义逆、特征值与特征向量）

## [Lab2](http://nbviewer.jupyter.org/github/Snowing-ST/Statistical-Case-Studies/blob/master/Lab2%20Statistical%20Modeling/Lab2%20Statistical%20Modeling.ipynb)
- 1. 用```scipy```包的```optimize.minimize```求似然函数的最大值
    - 1.1 极大似然函数生成正态分布随机数```np.random.normal```
    - 1.2 定义对数极大似然函数
    - 1.3 给定参数初值
    - 1.4 最小化负的对数极大似然函数```scipy.optimize.minimize```

- 2. 中文文本处理
    - 2.1 读入2018年政府工作报告txt文件
    - 2.2 去掉只有\n的空行，得到段落
    - 2.3 按照句号和感叹号分隔，去掉\n和空格，得到句子
    - 2.4 利用python正则表达式去除标点符号、数字、英文字母```re.sub```
    - 2.5 逐行写入txt、csv文件

## [Lab3](http://nbviewer.jupyter.org/github/Snowing-ST/Statistical-Case-Studies/blob/master/Lab3%20English%20Text%20Processing/Lab3%20English%20Text%20Processing.ipynb)

- **用nltk和re做英文文本处理**

1. 爬取新华网Business - Finance类别的新闻url  ```requests.get```+```json.loads```
2. 对每个url，爬取新闻标题及内容```xpath```
3. 批量读取新闻文本txt 
4. 文本预处理```nltk```+```re.sub```
5. 生成文本词频矩阵```sklearn.feature_extraction.text.CountVectorizer```
6. 根据词频绘制词云图```wordcloud```

![词云图](https://github.com/Snowing-ST/Statistical-Case-Studies/blob/master/Lab3%20English%20Text%20Processing/coin_mask.jpg)

## [Lab4](http://nbviewer.jupyter.org/github/Snowing-ST/Statistical-Case-Studies/blob/master/Lab4%20Chinese%20Text%20Processing/Lab4%20Chinese%20Text%20Processing.ipynb)

- **搜索并保存“中美贸易战”不同时间发布的新闻，用```jieba```提取关键词**

1. 批量读取文件
2. 提取所有文本数据
3. 加载自定义词典```jieba.load_userdict```
4. 分词```jieba.cut```
5. 添加自定义词汇jieba.add_word```
6. 去除字母、数字、标点、停用词
7. 提取关键词```jieba.analyse.extract_tags```

## [Lab5](https://github.com/Snowing-ST/Statistical-Case-Studies/tree/master/Lab5%20Scraping%20with%20Scrapy/newsSpider/spiders)

- **新浪新闻搜索scrapy spider**
1. [TradeWar.py](https://github.com/Snowing-ST/Statistical-Case-Studies/blob/master/Lab5%20Scraping%20with%20Scrapy/newsSpider/spiders/TradeWar.py):爬取搜索列表上的新闻详细内容

2. [TradeWarList.py](https://github.com/Snowing-ST/Statistical-Case-Studies/blob/master/Lab5%20Scraping%20with%20Scrapy/newsSpider/spiders/TradeWarList.py):爬取搜索列表上的新闻摘要

3. 修改了middlewares.py/items.py/settings.py

## [Lab6](https://github.com/Snowing-ST/Statistical-Case-Studies/tree/master/Lab6%20Scraping%20with%20xpath)

1. [TradeWarCrawl.py](https://github.com/Snowing-ST/Statistical-Case-Studies/blob/master/Lab6%20Scraping%20with%20xpath/TradeWarCrawl.py)
: 改写Lab5，多个不同搜索关键字并行爬取

2. [TradeWarCrawl - class.py](https://github.com/Snowing-ST/Statistical-Case-Studies/blob/master/Lab6%20Scraping%20with%20xpath/TradeWarCrawl%20-%20class.py): 改成类的形式，但不能并行爬取新闻

## [Lab7](https://github.com/Snowing-ST/Statistical-Case-Studies/tree/master/Lab7%20ZTE%20Events%20Text%20Analysis)
- **在新浪搜索爬取中兴事件的相关新闻并分时间段提取新闻观点**
- [preprocess.py](https://github.com/Snowing-ST/Statistical-Case-Studies/blob/master/Lab7%20ZTE%20Events%20Text%20Analysis/preprocess.py):对爬取的数据作文本预处理，提取词频，绘制词云图

 ![词云图](https://github.com/Snowing-ST/Statistical-Case-Studies/blob/master/Lab7%20ZTE%20Events%20Text%20Analysis/%E8%AF%8D%E4%BA%91%E5%9B%BE/period_1_wordcloud.jpg)

## [Lab8](https://github.com/Snowing-ST/Statistical-Case-Studies/tree/master/Lab8%20Probabilistic-Language-Modeling)
- **对爬取的新闻文本建立Ngram模型和word2vec模型**
1. [Probabilistic-Language-Modeling.ipynb](http://nbviewer.jupyter.org/github/Snowing-ST/Statistical-Case-Studies/blob/master/Lab8%20Probabilistic-Language-Modeling/Lab8%20Probabilistic-Language-Modeling.ipynb)
1. 利用Nram模型提取二元词频、并对新闻按时间段分类
2. 利用word2vec作简单的语义相似度探索

## [Lab9](https://github.com/Snowing-ST/Statistical-Case-Studies/tree/master/Lab9%20Dynamic%20Topic%20Model%20with%20Visulization)
- **对爬取的新闻文本建立动态主题模型**
1. [Dynamic Topic Models.ipynb](http://nbviewer.jupyter.org/github/Snowing-ST/Statistical-Case-Studies/blob/master/Lab9%20Dynamic%20Topic%20Model%20with%20Visulization/Lab9%20Dynamic%20Topic%20Models.ipynb)
2. 动态主题模型:```gensim.models.ldaseqmodel```
3. 提取每个时期的关键词
3. 动态主题模型可视化：```pyLDAvis```

## [Final Course Report](https://github.com/Snowing-ST/Statistical-Case-Studies/tree/master/CaseEx%20Extract%20Skill%20Imformation%20with%20LDA)
- **基于LDA 的招聘信息中技能要求提取与量化——以实习僧数据分析实习为例**
1. [实习僧爬虫:CaseEx_CrawlData.py](https://github.com/Snowing-ST/Statistical-Case-Studies/blob/master/CaseEx%20Extract%20Skill%20Imformation%20with%20LDA/CaseEx_CrawlData.py)
2. [文本预处理:CaseEx_preprocess.py](https://github.com/Snowing-ST/Statistical-Case-Studies/blob/master/CaseEx%20Extract%20Skill%20Imformation%20with%20LDA/CaseEx_preprocess.py)
3. [LDA提取并量化职位描述中的技能信息:CaseEx_LDA.py](https://github.com/Snowing-ST/Statistical-Case-Studies/blob/master/CaseEx%20Extract%20Skill%20Imformation%20with%20LDA/CaseEx_LDA.py)
4. [薪资与技能的回归分析:CaseEx_regression.py](https://github.com/Snowing-ST/Statistical-Case-Studies/blob/master/CaseEx%20Extract%20Skill%20Imformation%20with%20LDA/CaseEx_regression.py)
5. [报告全文:基于LDA的招聘信息中技能要求提取与量化.pdf](https://github.com/Snowing-ST/Statistical-Case-Studies/blob/master/CaseEx%20Extract%20Skill%20Imformation%20with%20LDA/%E5%9F%BA%E4%BA%8ELDA%E7%9A%84%E6%8B%9B%E8%81%98%E4%BF%A1%E6%81%AF%E4%B8%AD%E6%8A%80%E8%83%BD%E8%A6%81%E6%B1%82%E6%8F%90%E5%8F%96%E4%B8%8E%E9%87%8F%E5%8C%96.pdf)


![LDA可视化](https://github.com/Snowing-ST/Statistical-Case-Studies/blob/master/CaseEx%20Extract%20Skill%20Imformation%20with%20LDA/shixiseng.png)


------------------- 已完结 2018.07.06 ----------------------