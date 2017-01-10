import org.jetbrains.annotations.Contract;
import org.jetbrains.annotations.Nullable;

/**
 * Created by Leo on 2017/1/10.
 */
public class IntNode {
    private int data;
    private IntNode link;

    public IntNode(int initialData, IntNode initiallink){
        this.data = initialData;
        this.link = initiallink;
    }

    public int getData(){
        /**
         * 从当前节点获取数据
         * @return
         *     Current node's data
         */
        return this.data;
    }

    public IntNode getLink(){
        /**
         * 获得指向当前节点之后的下一个节点的指针
         * @return
         *      IntNode, next node
         */
        return this.link;
    }

    public void setData(int newdata){
        /**
         * 修改当前节点的数据
         * @param newdata
         *      New data this is to set to node
         */
        this.data = newdata;
    }

    public void setLink(IntNode link) {
        /**
         * 修改指向当前节点之后的下一个节点的指针
         * @param link
         *      指向链表中应该出现在当前节点之后的节点的指针
         */
        this.link = link;
    }

    public void addNodeAfter(int element){
        /**
         * 在当前节点之后添加节点
         * @param element
         *      要放在节点中的数据
         */
        this.link = new IntNode(element, this.link);
    }

    public void removeNodeAfter(){
        /**
         * 删除当前节点的后一个节点
         * @precondition
         *      当前节点不是链表的尾节点
         */
        this.link = this.link.link;
    }

    @Contract(pure = true)
    public static int listLength(IntNode head){
        /**
         * 计算链表中的节点数目
         * @param head
         *      链表的头指针
         * @return
         *      返回给定头指针的链表的节点数
         * @warning
         *      由于算术溢出，长度超过Int.MAX_VALUE的链表将产生错误答案
         */
        int answer = 0;
        for(IntNode cursor = head; cursor != null; cursor=cursor.link){
            answer++;
        }
        return answer;
    }

    @Nullable
    public static IntNode listSearch(IntNode head, int target){
        /**
         * 在链表中查找具有某个特定值的节点
         * @param head
         *      链表的头指针
         * @param target
         *      待查找的数据
         * @return
         *      指针，指向包含指定目标的第一个节点。
         *      如果没有这样的节点，返回null
         */
        for(IntNode cursor = head; cursor != null; cursor = cursor.link){
            if(target == cursor.getData())
                return cursor;
        }
        return null;
    }

    public static IntNode listPosition(IntNode head, int position){
        /**
         * 查找位于链表指定位置的节点
         * @param head
         *      链表的头指针
         * @param position
         *      节点序号（索引）
         * @precondition
         *      position > 0
         * @return
         *      返回指向指定位置的节点的指针。没有返回null
         * @throws
         *      IllegalArgumentException
         */
        IntNode cursor;
        int i;
        if(position <= 0)
            throw new IllegalArgumentException("position is not positive");
        cursor = head;
        for(i = 1; (i < position) && (cursor != null); i++)
            cursor = cursor.link;
        return cursor;
    }

    @Contract("null -> null")
    public static IntNode listCopy(IntNode source){
        /**
         * 复制链表
         * @param source
         *      要复制的链表的头指针
         * @return
         *      返回副本的头指针
         * @throws
         *      OutOfMemoryError
         */
        IntNode copyHead;
        IntNode copyTail;

        if(source == null)
            return null;

        copyHead = new IntNode(source.data, null);
        copyTail = copyHead;

        while (source.link != null){
            source = source.link;
            copyTail.addNodeAfter(source.data);
            copyTail = copyTail.link;
        }
        return copyHead;
    }

    public static IntNode[] listCopyWithTail(IntNode source){
        /**
         * 复制链表，同时返回链表的头尾指针
         * @param source
         *      将要复制的链表的头指针
         * @return
         *      索引0是头指针，索引1是尾指针
         * @throws
         *      OutOfMemoryError
         */
        IntNode copyHead;
        IntNode copyTail;
        IntNode[] answer = new IntNode[2];

        if(source == null)
            return null;

        copyHead = new IntNode(source.data, null);
        copyTail = copyHead;

        while (source.link != null){
            source = source.link;
            copyTail.addNodeAfter(source.data);
            copyTail = copyTail.link;
        }

        answer[0] = copyHead;
        answer[1] = copyTail;
        return answer;
    }

    public static IntNode[] listPart(IntNode start, IntNode end){
        /**
         * 复制链表的一部分，同时提供新副本的头指针和尾指针
         * @param start
         *      开始节点指针
         * @param end
         *      结束节点指针
         * @precondition
         *      start和end是指向同一链表中的节点的非null指针，且start所指节点在end所指节点之前
         * @return
         *      返回链表的一部分副本，从start节点开始，到end节点结束。
         *      返回值是一个数组，0是副本头指针，1是副本尾指针。
         * @throws
         *      IllegalArgumentError
         * @throws
         *      OutOfMemoryError
         */
        IntNode copyHead;
        IntNode copyTail;
        IntNode[] answer = new IntNode[2];

        if(start == null)
            throw new IllegalArgumentException("Start is null");
        if(end == null)
            throw new IllegalArgumentException("End is null");

        copyHead = new IntNode(start.data, null);
        copyTail = copyHead;
        while (start != end){
            start = start.link;
            if (start == null)
                throw new IllegalArgumentException("end node was not found on the list");
            copyTail.addNodeAfter(start.data);
            copyTail = copyTail.link;
        }

        answer[0] = copyHead;
        answer[1] = copyTail;
        return answer;
    }

    public static void main(String[] args){
        IntNode head;
        head = new IntNode(1, null);//Set as first node
        System.out.println(head.getData());
        head.link = new IntNode(2, null);//Insert a new node after head
        System.out.print(IntNode.listLength(head));
    }
}
