import javax.swing.table.TableColumnModel;

public class Solution {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println(new Solution().mySqrt(2));

	}

	public int mySqrt(int x) {
		if(x <= 1)
			return x;
		int begin = 1;
		int end = x;
		int mid = 0;
		while(begin <= end){
			mid = begin + (end - begin) / 2;
			if(mid == x / mid)
				return mid;
			else {
				if(mid < x / mid)
					begin = mid + 1;
				else {
					end = mid - 1;
				}
			}
		}
		return end;
	}

}
//4ms
