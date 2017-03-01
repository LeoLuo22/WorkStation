import numpy
def shape(A):
    """
        返回矩阵的形状（几行几列）
        @param A
         矩阵[[],[]]
        @return ()
    """
    num_rows = len(A)#行数
    num_cols = len(A[0]) if A else 0#列数

    return (num_rows, num_cols)

def get_row(A, i):
    """获取一行"""
    return A[i]

def get_column(A, j):
    """获取一列"""
    return [A_i[j] for A_i in A]

def main():
    a = numpy.matrix('1 2 3; 4 5 6; 7 8 9')
    print(a)

if __name__ == '__main__':
    main()

