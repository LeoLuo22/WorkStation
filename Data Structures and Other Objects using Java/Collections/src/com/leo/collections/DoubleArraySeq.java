package com.leo.collections;

/**
 * Created by Leo on 2017/3/8.
 */
public class DoubleArraySeq {
    private double[] data;
    private int manyItems;
    private int currentIndex;

    public DoubleArraySeq() {
        this.data = new double[10];
    }

    public DoubleArraySeq(int initialCapacity) {
        if (initialCapacity < 0) throw new IllegalArgumentException();

        this.data = new double[initialCapacity];
    }

    public void addAfter(double element) {

    }
}
