class Solution {
    public int characterReplacement(String s, int k) {

        int maxF = 0;
        int l  = 0 , r = 0;
        Map<Character, Integer> f_alph =  new HashMap<>();

        int max_l = 0;

        
        while ( r < s.length()){

            f_alph.put(s.charAt(r) , f_alph.getOrDefault(s.charAt(r) , 0) + 1);

            if (r - l + 1 - maxF <= k){
                maxF = Math.max(maxF, f_alph.getOrDefault(s.charAt(r),0));
                max_l = Math.max(max_l , r-l+1);
                r++;
            }else{
                l++;
                f_alph.put(s.charAt(r) , f_alph.get(s.charAt(r)) - 1);
            }

        }

        return max_l;

        
    }
}