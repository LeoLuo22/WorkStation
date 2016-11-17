
public class Solution {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Solution solution = new Solution();
		System.out.println(solution.countPrimes(3));

	}

	public int countPrimes(int n) {
		if(n <= 2)
			return 0;
		int rst = 0;
		boolean[] nums = new boolean[n];
		nums[0] = true;
		nums[1] = true;
		//System.out.println(nums[4]);
		int limit = (int)Math.sqrt(n);
		for(int i = 2; i < limit + 1; ++i){
			if(!nums[i]){
				for(int j = i * i; j < n; j += i){
					nums[j] = true;
				}
			}
		}
		for(int k = 0; k < n; ++k){
			if(!nums[k])
				++rst;
		}
		return rst;

	}

}
//22ms