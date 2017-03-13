package com.leo.practice;

/**
 * Created by Leo on 2017/3/2.
 */
public class example {
    /**
     * Character的封装类
     */
    private char c;

    public example (char c) {
        this.c = c;
    }

    public char charValue () {
        return this.c;
    }

    public static void main (String[] args) {
        example ex = new example('W');
        System.out.println(ex.charValue());
    }
}
