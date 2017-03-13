/**
 * Created by Leo on 2017/3/1.
 */
public class ObjectQueue {
    /**
     * 可以实现IntQueue, DoubleQueue等
     */
    public ObjectQueue() {
        /**
         * 初始化一个空队列
         * @postcondition
         *  队列为空
         */
    }

    public Object getFront() {
        /**
         * 取得队头数据项，并将其删除
         * @precondition
         *  队列非空
         * @postcondition
         *  返回队首数据项并将其删除
         * @throws
         *  NoSuchElementException。表明队列为空
         */
    }

    public void insert(Object item) {
        /**
         * 添加一个新元素到队尾，可以是null
         * @param item
         *  要添加的数据项
         * @postcondition
         *  数据添加到队尾
         * @throws
         *  OutOfMemoryError. 添加时内存不足
         */
    }

    public boolean isEmpty() {
        /**
         * 确定该队列是否为空
         * @return
         *  为空返回true
         */
    }

    public int size() {
        /**
         * 存取方法，确定队列中数据项的个数
         * @return
         *  int. 数据项的个数
         */
    }
}
