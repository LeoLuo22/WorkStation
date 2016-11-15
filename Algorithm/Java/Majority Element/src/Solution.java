import java.util.Arrays;

public class Solution {
	public int majorityElement(int[] nums) {
		Arrays.sort(nums);
		int flag = nums.length / 2;
		int tmp = nums[0];
		int count = 1;
		for(int i = 0; i < nums.length; ++i){
			if(count > flag)
				return tmp;
			if(tmp == nums[i + 1])
				count += 1;
			else {
				tmp = nums[i + 1];
				count = 1;
			}
		}
		return 0;
	}
}
//6ms
