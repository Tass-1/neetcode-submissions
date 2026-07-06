class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tc = {}
        for i in range(len(t)):
            ch = t[i]
            tc[ch] = tc.get(ch , 0) + 1
        wc = {}
        res = [float("inf"), -1 , -1]
        have = 0
        need = len(tc)
        l=0
        for r in range(len(s)):
            char = s[r]
            wc[char] = wc.get(char , 0) + 1
            if( char in tc and tc[char] == wc[char]):
                have = have + 1
            
            while( have == need):
                if( r-l+1) < res[0]:
                    res[0] = r-l+1 
                    res[1] = l 
                    res[2] = r 
                lchar = s[l]
                wc[lchar] = wc[lchar] - 1
                if( lchar in tc and wc[lchar] < tc[lchar]):
                    have = have - 1
                l = l + 1
        if( res[0] == float("inf")):
            return ""
        else:
            return s[res[1]:res[2]+1]





