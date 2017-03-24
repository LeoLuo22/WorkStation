package com.leo.solutions;

/**
 * Created by Leo on 2017/3/24.
 */
public class One {
    /**
     * 使用循环实现二分查找
     */
    public static int search(int a[], int first, int size, int target){
        int middle = first + size / 2;
        boolean found = false;
        int index = -1;

        while (!found && size > 0){
            if (target == a[middle]){
                index = middle;
                found = true;
            }
            else if (target < a[middle]) {
                size = size / 2;
                middle = first + middle / 2;
            }
            else {
                first = middle;
                size = size / 2;
                middle = middle + size / 2;
            }
        }

        if (found)
            return index;
        return -1;
    }

    public static void main(String[] args){
        int[] a = new int[10];
        for(int i=0; i < 10; ++i){
            a[i] = i;
        }
        System.out.println(search(a, 0, 10, 99));
    }
}
