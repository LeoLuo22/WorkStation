package com.leo.collections;


import com.leo.nodes.Node;
import com.leo.nodes.ObjectNode;

import java.util.NoSuchElementException;

/**
 * Created by Leo on 2017/3/1.
 */
public class ObjectLinkedQueue {
    /**
     * 由对象的指针构成的队列
     * 局限性：
     *  如果个数超过Int.MAX_VALUE将会出错
     */
    private int manyNodes;
    ObjectNode front;
    ObjectNode rear;

    public ObjectLinkedQueue () {
        /**
         * 初始化一个空队列
         * @postcondition
         *  队列为空
         */
        this.front = null;
        this.rear = null;
    }

    public Object clone () {
        /**
         * 产生该队列的一个副本
         * @return
         *  返回值是这个队列的一个副本。使用前强制转换为ObjectLinkedQueue
         * @throws
         *  OutOfMemoryError
         */
        ObjectLinkedQueue answer;
        ObjectNode[] cloneInfo;

        try {
            answer = (ObjectLinkedQueue) super.clone();
        }
        catch (CloneNotSupportedException e) {
            throw new RuntimeException();
        }

        cloneInfo = ObjectNode.listCopyWithTail(this.front);
        answer.front = cloneInfo[0];
        answer.rear = cloneInfo[1];

        return answer;
    }

    public Object getFront () {
        Object answer;
        if (this.manyNodes == 0)
            throw new NoSuchElementException();
        answer = this.front.getData();
        this.front = this.front.getLink();

        if (this.manyNodes == 0)
            this.rear = null;

        return answer;
    }

    public void insert (Object item) {
        if (isEmpty()) {
            this.front = new ObjectNode(item, null);
            this.rear = this.front;
        }
        else {
            this.rear.addNodeAfter(item);
            this.rear = this.rear.getLink();
        }

        ++this.manyNodes;
    }

    public boolean isEmpty () {
        return (this.manyNodes == 0);
    }

    public int size () {
        return manyNodes;
    }



}
