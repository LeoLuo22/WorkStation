public class Solution {
    public String countAndSay(int n) {
    	
        if(n ==  1)
        	return "1";
        String after = generator("1");
        String begin = generator("1");
        for(int i = 0; i < n - 2; ++i){
        	after = generator(begin);
        	begin = after;
        }
        return after;
    }
    public static String generator(String begin){
    	int count = 1;
    	String result = "";
    	char tmp = begin.charAt(0);
    	for(int i = 0; i < begin.length(); ++i){
    		if(i == begin.length() - 1)
    			return result + count + begin.charAt(i);
    		else {
				if(tmp == begin.charAt(i + 1)){
					count += 1;
				}
				else {
					result = result + count + tmp;
					tmp = begin.charAt(i + 1);
					count = 1;
				}
			}
    	}
    	return "";
    }
}
//25ms