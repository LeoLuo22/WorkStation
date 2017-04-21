import jieba
import numpy as np
from utils.mongo import connect
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

def get_cut_words(filename):
    """从文件读取停用词
        @param filename
         文件名
        @return
         List。包含停用词的列表
    """
    words = []
    with open(filename, 'r', encoding='utf8') as fh:
        for line in fh:
            words.append(line.replace('\n',''))
    return words

def del_stop_words(word, cutwords):
    """删除停用词
        @param word
         职位名称
        @param cutwords
         停用词列表
        @return
         去除停用词后的分词结果
    """
    result = jieba.cut(word)
    new_words = []
    for r in result:
        if r not in cutwords:
            new_words.append(r)
    return new_words

def get_all_vector(jobs, cutwords):
    """获取所有职位对应的向量
        @param jobs
         所有职位名称列表
        @param cutwords
         停用词列表
    """
    docs = []
    word_set = set()
    for job in jobs:
        doc = del_stop_words(job, cutwords)
        docs.append(doc)
        word_set = set(doc)

    word_set = list(word_set)
    docs_vsm = []

    for doc in docs:
        temp_vector = []
        for word in word_set:
            temp_vector.append(doc.count(word) * 1.0)
        docs_vsm.append(temp_vector)

    docs_matrix = np.array(docs_vsm)
    return docs_matrix

def cal_tfidf(docs_matrix):
    """计算TF-IDF
        @param doc_matrix
         numpy矩阵
    """
    column_sum = [ float(len(np.nonzero(docs_matrix[:,i])[0])) for i in range(docs_matrix.shape[1]) ]
    column_sum = np.array(column_sum)
    column_sum = docs_matrix.shape[0] / column_sum

    idf =  np.log(column_sum)
    idf =  np.diag(idf)

    for doc_v in docs_matrix:
        if doc_v.sum() == 0:
            doc_v = doc_v / 1
        else:
            doc_v = doc_v / (doc_v.sum())
        tfidf = np.dot(docs_matrix,idf)
        return tfidf
    #return names,tfidf

def main():
     cutwords = get_cut_words('cutwords.txt')
     jobs  = load_data()#[0:20]
     docs_matrix = get_all_vector(jobs, cutwords)
     weight = cal_tfidf(docs_matrix)
     clf = KMeans(n_clusters=7)
     s = clf.fit(weight)
     print(s.labels_)

if __name__=="__main__":
    main()
