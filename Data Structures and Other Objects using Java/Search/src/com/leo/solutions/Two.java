package com.leo.solutions;

import org.omg.PortableInterceptor.SYSTEM_EXCEPTION;

import java.util.Random;
import java.util.Scanner;

/**
 * Created by Leo on 2017/3/24.
 */
public class Two {

    public static void search(int[] results, int begin, int size){
        int middle = begin + size / 2;
        System.out.println("你的数是"+results[middle]+"吗(y/n)");
        Scanner sc = new Scanner(System.in);
        if (sc.nextLine().equals("y")) {
            return;
        }
        else {
            System.out.println("你的数大于"+results[middle]+"吗?(y/n)");
            Scanner s = new Scanner(System.in);
            if (s.nextLine().equals("y")) {
                search(results, middle+1, (size-1)/2);
            }
            else
                search(results, begin, size/2);
        }
    }

    public static void main(String[] args) {
        int middle = 0;

        System.out.println("请在0-200之间想一个整数。");

        int[] results = new int[200];

        for (int i = 0; i < 200; ++i) {
            results[i] = i;
        }

        search(results, 0, 200);
    }
}
