
class ListNode {
	int val;
	ListNode next;

	ListNode(int x) {
		val = x;
	}
}

public class Solution {
	public ListNode swapPairs(ListNode head) {
		if (head == null) {
			return null;
		}
		if (head.next == null) {
			return head;
		}
		ListNode tmp = head.next;
		head.next = swapPairs(tmp.next);
		tmp.next = head;

		return tmp;
	}
}