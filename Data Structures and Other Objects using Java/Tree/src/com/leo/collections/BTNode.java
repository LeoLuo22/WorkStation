package com.leo.collections;

/**
 * Created by Leo on 2017/3/9.
 */
public class BTNode {
    private Object data;
    private BTNode left;
    private BTNode right;

    public BTNode(Object initialData, BTNode initialLeft, BTNode initialRight) {
        this.data = initialData;
        this.left = initialLeft;
        this.right = initialRight;
    }

    public Object getData() {
        return this.data;
    }

    public BTNode getLeft() {
        return this.left;
    }

    public BTNode getRight() {
        return this.right;
    }

    public void setData(Object newData) {
        this.data = newData;
    }

    public void setLeft(BTNode newLeft) {
        this.left = newLeft;
    }

    public void setRight(BTNode newRight) {
        this.right = newRight;
    }

    public boolean isLeaf() {
        return (this.left == null) && (this.right == null);
    }

    public Object getLeftmostData() {
        if (this.left == null)
            return this.data;
        else
            return this.left.getLeftmostData();
    }

    public Object getRightmostData() {
        if (this.right == null)
            return this.data;
        else
            return this.right.getRightmostData();
    }

    public BTNode removeLeftmost() {
        /**
         * 删除以该节点为根节点的树的最左节点
         */
        if (this.left == null)
            return this.right;
        else {
            this.left = this.left.removeLeftmost();
            return this;
        }
    }

    public BTNode removeRightmost() {
        if (this.right == null)
            return this.left;
        else {
            this.right = this.right.removeRightmost();
            return this;
        }
    }

    public static BTNode treeCopy(BTNode source) {
        BTNode leftCopy, rightCopy;

        if (source == null)
            return null;
        else {
            leftCopy = treeCopy(source.left);
            rightCopy = treeCopy(source.right);
            return new BTNode(source.data, leftCopy, rightCopy);
        }
    }
}
