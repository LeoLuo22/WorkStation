package hanoi;

public class CountingBits {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		//for (String c : Integer.toBinaryString(5))
		CountingBits counti = new CountingBits();
		System.out.print(counti.countBits(5));

	}

	public int[] countBits(int num) {
		int[] result = new int[num + 1];
		int count = 0;
		for(int i = 0; i < num + 1; ++i){
			String s = Integer.toBinaryString(i);
			for(int j = 0; j < s.length(); ++j){
				if(s.charAt(j) == '1'){
						count += 1;
				}
			}
			result[i] = count;
			count = 0;
		}
		return result;

	}

}
