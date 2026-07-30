class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):return False
        s2=s+s
        if goal in s2:return True
        else:return False