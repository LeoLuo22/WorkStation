package com.leo.collections;

import java.util.NoSuchElementException;

/**
 * Created by Leo on 2017/3/1.
 */
public class ObjectQueue implements Cloneable{
    private Object[] data;
    private int manyItems;
    private int front;
    private int rear;

    public ObjectQueue() {
        /**
         * 初始化容量为10的空队列。
         * @postcondition
         *  队列为空，容量为10
         * @throws
         *  OutOfMemoryError.没有足够空间
         */
        final int INITIAL_CAPACITY = 10;
        manyItems = 0;
        data = new Object[INITIAL_CAPACITY];
    }

    public ObjectQueue(int initialCapacity) {
        /**
         * 以指定的容量初始化一个空队列
         * @param initialCapacity
         *  队列的初始容量
         * @precondition
         *  initialCapacity非负
         * @postcondition
         *  队列为空且容量为initialCapacity
         * @throws
         *  IllegalArgumentException,参数为负
         * @throws
         *  OutOfMemoryError
         */
        if (initialCapacity < 0)
            throw new IllegalArgumentException("Argument must greater than zero");
        manyItems = 0;
        data = new Object[initialCapacity];
    }

    public Object clone() {
        /**
         * 产生这个队列的一个副本
         * @return
         *  副本
         * @throws
         *  OutOfMemoryError
         */
        ObjectQueue answer;

        try{
            answer = (ObjectQueue) super.clone();
        }
        catch (CloneNotSupportedException e){
            throw new RuntimeException("Does not cloneable");
        }

        answer.data = (Object[]) data.clone();

        return answer;
    }

    public void ensureCapacity(int minimumCapacity) {
        /**
         * 改变这个队列的当前容量
         * @param minimumCapacity
         *  新容量
         * @postcondition
         *  队列的容量至少为minimumCapacity。
         * @throws
         *  OutOfMemoryError
         */
        Object biggerArray[];
        int n1, n2;

        if (data.length >= minimumCapacity)//不需要改变
            return;
        else if (manyItems == 0)//只是增加数组的大小，因为队列为空
            data = new Object[minimumCapacity];
        else if (front <= rear){
            //创建更大的数组，并将data[front]...data[rear]复制到其中
            biggerArray = new Object[minimumCapacity];
            System.arraycopy(data, front, biggerArray, front, this.manyItems);
            this.data = biggerArray;
        }
        else {
            biggerArray = new Object[minimumCapacity];
            n1 = this.data.length - this.front;
            n2 = this.rear + 1;
            System.arraycopy(this.data, this.front, biggerArray, 0, n1);
            System.arraycopy(this.data, 0, biggerArray, n1, n2);

            this.front = 0;
            this.rear = this.manyItems - 1;
            this.data = biggerArray;
        }
    }

    public int getCapacity() {
        return this.data.length;
    }

    public Object getFront() {
        Object answer;
        if (this.manyItems == 0)
            throw new NoSuchElementException("Queue underflow");
        answer = data[this.front];
        this.manyItems--;
        return answer;
    }

    public void insert(Object item) {
        if (this.manyItems == this.data.length) {
            this.ensureCapacity(this.manyItems * 2 + 1);
        }

        if (this.manyItems == 0) {
            this.front = 0;
            this.rear = 0;
        }

        else
            this.rear = this.nextIndex(this.rear);
        this.data[rear] = item;
        this.manyItems++;
    }

    public boolean isEmpty() {
        return (this.manyItems == 0);
    }

    private int nextIndex(int i) {
        if (i == this.data.length - 1)
            return 0;
        return i + 1;
    }

    public int size() {
        return this.manyItems;
    }

    public void trimToSize() {
        /**
         * 将这个队列的当前容量减少到实际大小
         * @postcondition
         *  队列的容量被改为它当前的大小
         * @throws
         *  OutOfMemoryError
         */
        Object fit[];

        if (this.size() == this.data.length) //数组的长度等于数据项的个数
            return;
        else if (this.size() == 0){//数据项的个数为0
            fit = new Object[0];
            this.data = fit;
            return;
        }
        else if (this.front <= this.rear) {
            fit = new Object[this.size()];
            System.arraycopy(this.data, this.front, fit, 0, this.manyItems);
            this.data = fit;
            return;
        }
        else {
            int n1, n2;
            fit = new Object[this.size()];
            n1 = this.data.length - this.front;
            System.arraycopy(this.data, this.front, fit, 0, n1);
            n2 = this.rear + 1;
            System.arraycopy(this.data, 0, fit, n1, n2);
        }
    }
}
