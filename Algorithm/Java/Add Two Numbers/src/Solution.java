
class ListNode {
	int val;
	ListNode next;

	ListNode(int x) {
		val = x;
	}
}

public class Solution {
	public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
		ListNode ret = new ListNode(0);
		ListNode cur = ret;

		int sum = 0;
		while (true) {
			if (l1 != null) {
				sum += l1.val;
				l1 = l1.next;
			}
			if (l2 != null) {
				sum += l2.val;
				l2 = l2.next;
			}
			cur.val = sum % 10;
			sum /= 10;
			if (l1 != null || l2 != null || sum != 0) {
				cur = (cur.next = new ListNode(0));
			} else {
				break;
			}
		}
		return ret;
	}
}