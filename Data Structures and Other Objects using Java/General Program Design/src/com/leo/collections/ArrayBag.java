package com.leo.collections;

/**
 * Created by Leo on 2017/3/2.
 */
public class ArrayBag {
    /**
     * 保存对象的包
     */
    private Object[] data;
    private int manyItems;

    public ArrayBag () {
        /**
         * 初始化空包，初始容量为10
         * @postcondition
         *  包是空，初始容量为10
         * @throws
         *  OutOfMemoryError
         */
        final int INITIAL_CAPACITY = 10;
        manyItems = 0;
        data = new Object[INITIAL_CAPACITY];
    }

    public ArrayBag (int initialCapacity) {
        /**
         * 用指定的初始容量来初始化空包
         * @param initialCapacity
         *  包的初始容量
         * @precondition
         *  initialCapacity不为负
         * @postcondition
         *  生成空包。容量为给定的容量
         * @throws
         *  IllegalArgumentException
         * @throws
         *  OutOfMemoryError
         */
        if (initialCapacity < 0) throw new IllegalArgumentException(initialCapacity + " is negative. ");

        this.manyItems = 0;
        this.data = new Object[initialCapacity];
    }

    public void add (Object element) {
        /**
         * 将某个对象的指针放入包中。如果新增的对象指针会使得包超出当前的容量，那么
         * 在增加新元素前增加容量。新元素可以是null指针。
         * @param element
         *  增加到包中的元素
         * @postcondition
         *  指定对象的指针被增加到了包中
         * @throws
         *  OutOfMemoryError
         * @warning
         *  OverFlow
         */
        if (this.manyItems == this.data.length) {//如果当前容量已满
            //this.ensureCapacity(this.manyItems * 2 + 1);
            Object[] newData = new Object[this.data.length + 10];
            System.arraycopy(this.data, 0, newData, 0, this.manyItems);//拷贝到新数组
            this.data = newData;
        }

        this.data[this.manyItems] = element;
        ++this.manyItems;
        return;
    }

    public void addAll (ArrayBag addend) {
        /**
         * 增加一个包的所有内容到当前包中
         * @param addend
         *  一个包
         * @precondition
         *  addend不为null
         * @postcondition
         *  将addend中的元素增加到了当前包
         * @throws
         *  NullPointerException
         * @throws
         *  OutOfMemoryError
         *
         */
        if (addend == null) throw new NullPointerException();

        Object[] newData = new Object[this.data.length + addend.data.length];
        System.arraycopy(this.data, 0, newData, 0, this.manyItems);
        System.arraycopy(addend.data, 0, newData, this.manyItems, addend.manyItems);

        this.manyItems += addend.manyItems;
    }

    public Object clone () {
        /**
         * 返回当前包的一个副本
         * @eturn
         *  当前包的一个副本
         */
        ArrayBag answer;

        try {
            answer = (ArrayBag) super.clone();
        }
        catch (CloneNotSupportedException e) {
            throw new RuntimeException();
        }

        answer.data = (Object[]) data.clone();
        return answer;
    }

    public int countOccurrences(Object target) {
        /**
         * 用于统计包中某个特定元素出现的次数的存取方法
         * @param target
         *  将被统计的Object指针
         * @return
         *  target出现的次数。如果target不为null，那么将使用targer.equals方法来统计次数
         */
        int count = 0;

        if (target == null) {
            for (int j = 0; j < this.manyItems; ++j) {
                if (this.data[j] == null)
                    ++count;
            }
        }
        else {
            for (int i = 0; i < this.manyItems; ++i) {
                if (this.data[i].equals(target))
                    ++count;
            }
        }

        return count;
    }

    public void ensureCapacity (int minimumCapacity) {
        /**
         * 改变包的当前容量
         * @postcondition
         *  包的容量修改为至少为minimumCapacity
         * @throws
         *  OutOfMemoryError
         */
        if (this.data.length >= minimumCapacity)
            return;

        Object[] newData = new Object[minimumCapacity];
        System.arraycopy(this.data, 0, newData, 0, this.manyItems);

        this.data = newData;

        return;
    }

    public int getCapacity () {
        /**
         * 确定包的当前容量的存取方法。
         * @return
         *  当前包的容量
         */
        return this.data.length;
    }

    public Object grab () {
        /**
         * 从包中检索某个随机元素的存取方法
         * @precondition
         *  包不为空
         * @return
         *  返回从包中任意选定的元素
         * @throws
         *  IllegalStateException
         */
        if (this.data == null) throw new IllegalStateException();

        int index = (int) Math.random() * (this.manyItems - 1);
        return this.data[index];
    }

    public Boolean remove (Object target) {
        /**
         * 从包中移除某个指定元素的副本
         * @param target
         *  将从包中移除的元素
         * @postcondition
         *  如果找到，移除一个副本。返回true
         */
        for (int i = 0; i < this.manyItems; ++i) {
            if (this.data[i].equals(target)) {
                this.data[i] = null;
                return true;
            }
        }

        return false;
    }

    public int size () {
        /**
         * 确定包中元素个数
         * @return
         *  包中元素个数
         */
        return this.manyItems;
    }

    public void trimToSize () {
        /**
         * 将包的当前容量减小到元素个数
         * @postcondition
         *  容量与元素相同
         */
        if (this.data.length == this.manyItems)
            return;

        Object[] newData = new Object[this.manyItems];
        System.arraycopy(this.data, 0, newData, 0, this.manyItems);

        return;
    }

    public static ArrayBag union (ArrayBag b1, ArrayBag b2) {
        /**
         * 生成包含其它两个包的所有元素的新宝
         * @param b1, b2
         *  两个包
         * @precondition
         *  b1和b2不为空
         * @throws
         *  NullPointerException
         * @throws
         *  OutOfMemoryError
         */
        if (b1 == null || b2 == null) throw new NullPointerException();

        int size = b1.manyItems + b2.manyItems;

        ArrayBag arrayBag = new ArrayBag(size);

        System.arraycopy(b1.data, 0, arrayBag.data, 0, b1.manyItems );
        System.arraycopy(b2.data, 0, arrayBag.data, b1.manyItems, b2.manyItems);

        return arrayBag;
    }
}
