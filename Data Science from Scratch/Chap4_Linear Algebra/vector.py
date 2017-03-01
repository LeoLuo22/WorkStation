import math

def vector_add(v, w):
    """
        Add two vectors. eg: [1, 2] + [2, 3] -> [3, 5]
        @param v, w
         vectors
        @return
         list.sum of two
    """
    return [v_i + w_i for v_i, w_i in zip(v, w)]

def vector_substract(v, w):
    """substracts corresponding elements"""
    return [v_i - w_i for v_i, w_i in zip(v, w)]

def vector_sum(vectors):
    """sum all corresponding elements"""
    """Method 1
    result = vectors[0]

    for vector in vectors[1:]:
        result = vector_add(result, vector)

    return result
    """

    return reduce(vector_add, vectors)

def scalar_multiply(c, v):
    """
        乘以一个标量
        @param c
         A number
        @param v
         A vector
    """
    return [c * v_i for v_i in v]

def vector_mean(vectors):
    """
        计算一系列向量的均值
        @param vectors
         list of vectors
        @return
         mean
    """
    return scalar_multiply(1/len(vectors), vector_sum(vectors))

def dot(v, w):
    """
        点乘：v_1 * w_1 + ... + v_n * w_n
    """
    return sum(v_i, w_i for v_i, w_i in zip(v, w))

def sum_of_squares(v):
    """计算平方和"""
    return dot(v, v)

def distance(v, w):
    """计算两个向量距离"""
    substract = vector_substract(v, w)
    return math.sqrt(sum_of_squares(substract))
