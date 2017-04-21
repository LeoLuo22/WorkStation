"""实现职位的聚类"""
import jieba
from jieba import analyse
import numpy as np
from utils.mongo import connect
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import KMeans

def load_data():
    """载入职位名称
        @return -> list,所有的职位名
    """
    names = []
    cursor = connect('lagou', 'jobs')
    for result in cursor.find():
        names.append(result.get('name'))

    return names

def key_word_extract(sentence):
    """关键字提取
        @param sentence -> 职位信息
        @return -> 关键字
    """
    #seg_list = jieba.cut(sentence, cut_all=False)
    tags = analyse.extract_tags(sentence, topK=3)
    return seg_list
"""
def get_vsm():
    docs = load_data()
    for doc in docs:
        temp = []
        for
"""
def main():
    """
    names = load_data()
    for i in range(10):
        print(key_word_extract(names[i]))
    """
    k = k_means(cal_tfidf())
    for _ in k:
        print(_)

def cal_tfidf():
    corpus = load_data()[0:20]
    vectorizer = CountVectorizer()
    transformer = TfidfTransformer()

    tfidf = transformer.fit_transform(vectorizer.fit_transform(corpus))
    word = vectorizer.get_feature_names()
    weight = tfidf.toarray()

    return weight

def k_means(weight):
    clf = KMeans(n_clusters=7)
    s = clf.fit(weight)


    return s.labels_


if __name__ == '__main__':
    main()
