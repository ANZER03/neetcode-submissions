class Solution {
    public int characterReplacement(String s, int k) {

        int maxF = 0;
        int l  = 0 , r = 0;
        Map<Character, Integer> f_alph =  new HashMap<>();

        int max_l = 0;

        
        for (;  r < s.length() ; r++){

            f_alph.put(s.charAt(r) , f_alph.getOrDefault(s.charAt(r) , 0) + 1);
            maxF = Math.max(maxF, f_alph.getOrDefault(s.charAt(r),0));
            if ((r - l + 1) - maxF > k){
                // maxF = Math.max(maxF, f_alph.getOrDefault(s.charAt(r),0));
                f_alph.put(s.charAt(l) , f_alph.get(s.charAt(l)) - 1);
                l++;
            }

           max_l = Math.max(max_l , r - l + 1 );
        }

        return max_l;

        
    }
}