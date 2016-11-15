import java.util.ArrayList;

public class Solution {
    public String toHex(int num) {
        long num1 = num;
		long max_dec = Long.parseLong("4294967296");
		if(num < 0){
			num1 = max_dec + num;
		}
		String string = "0123456789abcdef";
		ArrayList<Long> rst = new ArrayList<Long>();
		long mo = 0;
		long yu = num;
		while(num1 >= 16){
			mo = num1 % 16;
			yu = num1 / 16;
			rst.add(mo);
			num1 = yu;
		}
		rst.add(yu);
		String result = "";
		int j = rst.size();
		for(int i = j - 1; i > -1; --i)
		{
			result += string.charAt(Integer.parseInt(String.valueOf((rst.get(i)))));
		}
		return result;
    }
}
//11ms