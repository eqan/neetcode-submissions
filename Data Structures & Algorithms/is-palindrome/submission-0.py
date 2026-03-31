class Solution:
    def isPalindrome(self, s: str) -> bool:
        lin_str = ""
        opp_str = ""
        for c in s:
            if c.isalnum():
                c_lower = c.lower()
                lin_str += c_lower
                opp_str = c_lower + opp_str
        print(lin_str)
        print(opp_str)
        if lin_str == opp_str:
            return True
        return False