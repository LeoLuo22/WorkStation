package com.leo.collections;

/**
 * Created by Leo on 2017/3/8.
 */
public class IntArrayBag {
    private int[] data;
    private int manyItems;

    public IntArrayBag () {
        /**
         * 使用初始容量10初始化空包
         * @postcondition
         *  该包为空且初始容量为10
         * @throws
         *  OutOfMemoryError
         */
        final int INITIAL_CAPACITY = 10;
        this.data = new int[INITIAL_CAPACITY];
    }

    public IntArrayBag(int initialCapacity) {
        /**
         * 使用指定的初始容量初始化一个空包
         * @param initialCapacity
         *  该包的初始容量
         * @precondition
         *  initialCapacity不为负
         * @postcondition
         *  初始化一个空包
         * @throws
         *  OutOfMemoryError
         * @throws
         *  IllegalArgumentException
         */
        if (initialCapacity < 0) throw new IllegalArgumentException();

        this.data = new int[initialCapacity];
    }

    public void add(int element) {
        /**
         * 添加一个新元素。如果该元素使得该包的容量超过了当前容量，那么
         * 在添加之前就增大容量。
         * @param element
         *  要添加的元素
         * @postcondition
         *  将该元素的一个副本添加到该包中
         * @throws
         *  OutOfMemoryError
         * @warning
         *  容量不能大于Integer.MAX_VALUE
         */
        if (this.manyItems == this.data.length) {//现在的元素数目和容量相等
            int[] newData = new int[this.data.length*2+1];
            System.arraycopy(this.data, 0, newData, 0, this.data.length);
            this.data = newData;
        }

        this.data[this.manyItems] = element;
        ++this.manyItems;
    }

    public void addAll(IntArrayBag addend) {
        /**
         * 将一个bag的元素全部添加进来
         * @param addend
         *  要添加的包
         * @preconditon
         *  addend不为空
         * @postcondition
         *  添加
         * @throws
         *  NullPointerException
         * @throws
         *  OutOfMemoryError
         * @warning
         *  Overflow
         */
        if (addend == null) throw new NullPointerException();

        this.ensureCapacity(this.manyItems+addend.size());
        System.arraycopy(addend.data, 0, this.data, this.manyItems, addend.size());
        this.manyItems += addend.size();
    }

    public Object clone() {
        /**
         * 生成该包的一个副本
         * @return
         *  该包的一个副本
         * @throws
         *  OutOfMemoryError
         */
        IntArrayBag answer = null;

        try {
            answer = (IntArrayBag) super.clone();
        }
        catch (CloneNotSupportedException e) {
            throw new RuntimeException();
        }

        answer.data = (int[]) data.clone();

        return answer;
    }

    public int countOccurrences(int target) {
        /**
         * 计算指定元素出现的次数
         * @param target
         *  指定元素
         * @return
         *  出现的次数
         */
        int count = 0;

        for (int i = 0; i < this.manyItems; ++i) {
            if (this.data[i] == target)
                ++count;
        }

        return count;
    }

    public void ensureCapacity (int minimumCapacity) {
        /**
         * 改变该包的当前容量
         * @param minimum
         *  该包的新容量
         * @postcondition
         *  将该包的容量变成至少minimumCapacity
         * @throws
         *  OutOfMemoryError
         */
        if (this.data.length >= minimumCapacity)
            return;

        int[] newData = new int[minimumCapacity];
        System.arraycopy(this.data, 0, newData, 0, this.manyItems);
        this.data = newData;
    }

    public int getCapacity () {
        /**
         * 获取该包的当前容量的存取方法
         * @return
         *  该包的当前容量
         */
        return this.data.length;
    }

    public boolean remove (int target) {
        /**
         * 从该包删除一个指定元素
         * @param target
         *  从该包删除的元素
         * @postcondition
         *  如果找到了target，就删除，并且返回true;
         */
        int index = 0;
        while (index < this.manyItems && target != this.data[index])
            ++index;

        if (this.manyItems == index)
            return false;

        else {
            --this.manyItems;
            this.data[index] = this.data[manyItems];
            return true;
        }
    }

    public int size () {
        /**
         * 确定该包中元素数目的存取方法
         * @return
         *  该包中元素的数目
         */
        return this.manyItems;
    }

    public void trimToSize () {
        /**
         * 将该包的容量减小成为它的实际大小
         * @postcondition
         *  变成它的当前大小
         * @throws
         *  OutOfMemoryError
         */
        if (this.data.length == this.manyItems) return;

        int[] newData = new int[this.manyItems];
        System.arraycopy(this.data, 0, newData, 0, this.manyItems);
        this.data = newData;

    }

    public static IntArrayBag union (IntArrayBag bag1, IntArrayBag bag2) {
        IntArrayBag answer = new IntArrayBag(bag1.size()+bag2.size());

        System.arraycopy(bag1, 0, answer.data, 0, bag1.size());
        System.arraycopy(bag2, 0, answer.data, bag1.size(), bag2.size());

        return answer;
    }

    public String toString () {
        String result = "";

        for (int i = 0; i < this.data.length; ++i) {
            result += this.data[i] + ", ";
        }

        return result;
    }

    public static void main (String[] args) {
        IntArrayBag intArrayBag = new IntArrayBag();
        for (int i = 0; i < 6; ++i)
            intArrayBag.add(i);
        intArrayBag.add(1);
        System.out.println(intArrayBag.size());
        System.out.println(intArrayBag.countOccurrences(1));

    }
}
