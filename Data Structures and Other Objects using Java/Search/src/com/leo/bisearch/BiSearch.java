package com.leo.bisearch;

/**
 * Created by Leo on 2017/3/23.
 */
public class BiSearch {
    public static int search(int[] a, int first, int size, int target){
        /**
         * 在已排好序的部分数组中查找指定的目标值
         * @param a
         *  要查找的数组名
         * @param first
         *  开始下表
         * @param size
         *  要查找的元素个数
         * @param target
         *  查找的目标元素
         * @precondition
         *  如果size > 0，那么a中first到first+size-1的下标
         *  应该是有效的。
         * @return
         *  找到返回所在的下标。否则-1
         * @throws
         *  ArrayIndexOutOfBoundsException
         */
        int middle = 0;

        if (size < 0)
            return -1;
        else {
            middle = first + size/2;
            if (target == a[middle])
                return middle;
            else if (target < a[middle])
                return search(a, first, size/2, target);
            else
                return search(a, middle+1, (size-1)/2, target);
        }
    }
}
