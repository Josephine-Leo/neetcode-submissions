class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ds = {}
        dt = {}
        if len(s) != len(t):
            return False
        else:
            for i in range(len(s)):

                if s[i] not in ds:
                    ds[s[i]] = 1
                else:
                    ds[s[i]] += 1

                if t[i] not in dt:
                    dt[t[i]] = 1
                else:
                    dt[t[i]] += 1
            
            if ds.keys() == dt.keys():  

                for i in ds.keys():
                    if ds[i] != dt[i]:
                        return False

                return True

            return False