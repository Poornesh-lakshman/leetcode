class Solution:
    def secondHighest(self, s: str) -> int:
        a = sorted(set(ch for ch in s if ch.isdigit()))
        if len(a) < 2:
            return -1
        return int(a[-2])