
public class Solution {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}
	public int minPatches(int[] nums, int n) {
		long miss = 1;
		int i = 0;
		int added = 0;
		while(miss <= n){
			if(i < nums.length && nums[i] <= miss){
				miss += nums[i++];
			}
			else {
				miss += miss;
				added++;
			}
		}
        return added;
    }

}
