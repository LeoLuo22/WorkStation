
public class Solution {
	
	public static void main(String[] args){
		Solution solution = new Solution();
		System.out.println(solution.titleToNumber("AA"));
	}
	
    public int titleToNumber(String s) {
    	String string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    	int result = 0, j = 0;
    	for(int i = s.length() - 1; i > -1; --i){
    		char c = s.charAt(i);
    		int trans = 0, tmp = 1;
    		trans = string.indexOf(c) + 1;
    		for(int k = 0; k < j; ++k)
    			tmp *= 26;
    		trans *= tmp;
    		result += trans;
    		j += 1;
    	}
        return result;
    }
}