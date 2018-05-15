# Statistical-Case-Studies
feng.li课程作业

## [Lab1](http://nbviewer.jupyter.org/github/Snowing-ST/Statistical-Case-Studies/blob/master/%E5%8F%B8%E5%BE%92%E9%9B%AA%E9%A2%96_2017210785_Lab1.ipynb)
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

## [Lab2](http://nbviewer.jupyter.org/github/Snowing-ST/Statistical-Case-Studies/blob/master/%E5%8F%B8%E5%BE%92%E9%9B%AA%E9%A2%96_2017210785_Lab2.ipynb)
- 1. 用scipy包的optimize.minimize求似然函数的最大值
    - 1.1 极大似然函数生成正态分布随机数np.random.normal
    - 1.2 定义对数极大似然函数
    - 1.3 给定参数初值
    - 1.4 最小化负的对数极大似然函数scipy.optimize.minimize

- 2. 中文文本处理
    - 2.1 读入2018年政府工作报告txt文件
    - 2.2 去掉只有\n的空行，得到段落
    - 2.3 按照句号和感叹号分隔，去掉\n和空格，得到句子
    - 2.4 利用python正则表达式去除标点符号、数字、英文字母re.sub
    - 2.5 逐行写入txt、csv文件

## [Lab3](http://nbviewer.jupyter.org/github/Snowing-ST/Statistical-Case-Studies/blob/master/%E5%8F%B8%E5%BE%92%E9%9B%AA%E9%A2%96_2017210785_Lab3.ipynb)

- **用nltk和re做英文文本处理**

1. 爬取新华网Business - Finance类别的新闻url  requests.get+json.loads
2. 对每个url，爬取新闻标题及内容xpath
3. 批量读取新闻文本txt 
4. 文本预处理nltk+re.sub
5. 生成文本词频矩阵sklearn.feature_extraction.text.CountVectorizer  
6. 根据词频绘制词云图wordcloud

![词云图](https://github.com/Snowing-ST/Statistical-Case-Studies/blob/master/Lab3%20English%20Text%20Processing/coin_mask.jpg)

## [Lab4](http://nbviewer.jupyter.org/github/Snowing-ST/Statistical-Case-Studies/blob/master/%E5%8F%B8%E5%BE%92%E9%9B%AA%E9%A2%96_2017210785_Lab4.ipynb)

- **搜索并保存“中美贸易战”不同时间发布的新闻，用jieba提取关键词**

1. 批量读取文件
2. 提取所有文本数据
3. 加载自定义词典jieba.load_userdict
4. 分词jieba.cut
5. 添加自定义词汇jieba.add_word
6. 去除字母、数字、标点、停用词
7. 提取关键词jieba.analyse.extract_tags

## [Lab5](https://github.com/Snowing-ST/Statistical-Case-Studies/tree/master/newsSpider/newsSpider/spiders)

- **新浪新闻搜索scrapy spider**
1. [TradeWar.py](https://github.com/Snowing-ST/Statistical-Case-Studies/blob/master/newsSpider/newsSpider/spiders/TradeWar.py):爬取搜索列表上的新闻详细内容

2. [TradeWarList.py](https://github.com/Snowing-ST/Statistical-Case-Studies/blob/master/newsSpider/newsSpider/spiders/TradeWarList.py):爬取搜索列表上的新闻摘要

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
1. [Ngram+word2vec](http://nbviewer.jupyter.org/github/Snowing-ST/Statistical-Case-Studies/blob/master/Lab8%20Probabilistic-Language-Modeling/%E5%8F%B8%E5%BE%92%E9%9B%AA%E9%A2%96_2017210785_Lab8.ipynb)
1. 利用Nram模型提取二元词频、并对新闻按时间段分类
2. 利用word2vec作简单的语义相似度探索
