import java.util.Arrays;

public class Solution {
    public int singleNumber(int[] nums) {
        Arrays.sort(nums);
		if(nums.length == 1)
			return nums[0];
		if(nums[0] != nums[1] && nums[1] == nums[2])
			return nums[0];
		if(nums[nums.length - 1] != nums[nums.length - 2] && nums[nums.length - 2] == nums[nums.length - 3])
				return nums[nums.length - 1];
		for(int i = 1; i < nums.length; ++i){
			if(nums[i] != nums[i - 1] && nums[i] != nums[i + 1])
				return nums[i];
		}
		return 0;
    }
}