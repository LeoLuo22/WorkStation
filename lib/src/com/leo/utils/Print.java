package com.leo.utils;

/**
 * Created by Leo on 2017/1/16.
 */
public class Print {
    /**
     * Using print like Python
     */
    public static void print(String s){
        /**
         * 默认换行，参数为字符串
         */
        System.out.println(s);
    }

    public static void print(int s){
        /**
         * 默认换行，参数为字符串
         */
        System.out.println(s);
    }

    public static void print(String s, String end) {
        /**
         * 不换行版本
         */
        System.out.print(s+end);
    }
}
