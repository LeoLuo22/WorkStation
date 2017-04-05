package com.leo.sort;

/**
 * Created by Leo on 2017/3/29.
 */
public class Select {
    public static void selectionsort(int[] data, int first, int n){
        /**
         * @precondition
         *  data至少已有从data[first]开始的单元
         * @postcondition
         *  data的元素按从小到大排列
         */
        int i, j;
        int big;
        int temp;

        for(i = n-1; i > 0; i--){
            big = first;
            for (j = first + 1; j <= first + i; j++) {
                if (data[big] < data[j])
                    big = j;
            }
            temp = data[first+i];//first+i是未排好序的最后元素的坐标
            data[first+i] = data[big];//将最大值放到末尾
            data[big] = temp;
        }
    }
    public static void main(String[] args) {
        int[] a = new int[]{8, 2, 5, 3, 10, 7, 1, 4, 6, 9};
        selectionsort(a, 0, 10);
        for (int i : a)
            System.out.print(i + " ");
    }
}
