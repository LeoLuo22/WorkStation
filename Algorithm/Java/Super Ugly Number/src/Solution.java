public class Solution {
    public int nthSuperUglyNumber(int n, int[] primes) {
        int size = primes.length;
        int q[] = new int[n];
        int idxes[] = new int[size];
        int vals[] = new int[size];
        q[0] = 1;
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < size; j++) {
                vals[j] = q[idxes[j]] * primes[j];
            }
            q[i] = findMin(vals);
            for (int j = 0; j < size; j++) {
                if (vals[j] == q[i]) {
                    idxes[j] += 1;
                }
            }
        }
        return q[n - 1];
    }

    public int findMin(int[] nums) {
        int min = nums[0];
        for (int i = 1; i < nums.length; i++) {
            min = Math.min(min, nums[i]);
        }
        return min;
    }
}