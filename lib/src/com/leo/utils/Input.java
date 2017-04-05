package com.leo.utils;

import java.util.Scanner;
import static com.leo.utils.Print.*;
/**
 * Created by Leo on 2017/4/5.
 */
public class Input {
    public static String input(String s){
        /**
         * Python版input
         * @param s
         *  输入时的提示词
         */
        System.out.println(s);
        Scanner sc = new Scanner(System.in);
        String result = sc.next();
        return result;
    }

    public static String input(){
        /**
         * Python版input
         * 无提示词
         */
        Scanner sc = new Scanner(System.in);
        String result = sc.next();
        return result;
    }

    public static void main(String[] args){
        int s = Integer.parseInt(input("请输入"));
        s += 1;
        print(s);
    }
}
