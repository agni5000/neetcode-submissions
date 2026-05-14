class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash1 = [0] * 26
        
        if len(s) != len(t):
            return False

        for i in range (len(s)):
            hash1 [ord (s[i])- ord ("a")]+= 1 

        for i in range (len(t)):
            hash1 [ord (t[i])- ord ("a")]-= 1 
            if hash1 [ord(t[i] )- ord("a")] <0:
                return False
        return True
            
