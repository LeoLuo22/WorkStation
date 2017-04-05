package com.leo.sort;

/**
 * Created by Leo on 2017/3/29.
 */
public class Insert {
    public static void insertionsort(int[] data, int first, int n) {
        int i, j;
        int index;
        int temp;
        int entry;
        int toinsert;//保存待插入元素下标

        for (i = 0; i < n; ++i) {
            toinsert = first + i;
            entry = data[toinsert];

            for (j = toinsert; j > first; --j) {
                if (entry < data[j-1]) {
                    data[j] = data[j - 1];
                    data[j-1] = entry;
                }
            }
        }
    }

    public static void main(String[] args) {
        int[] a = new int[]{8, 2, 5, 3, 10, 7, 1, 4, 6, 9};
        insertionsort(a, 0, 10);
        for (int i : a)
            System.out.print(i + " ");
    }
}
