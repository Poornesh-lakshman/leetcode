class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d = {}
        c = ''
        pa = pattern
        w = s.split()

        if len(pattern) != len(w):
            return False

        for i in range(len(pattern)):
            if pattern[i] in d:
                if d[pattern[i]] != w[i]:
                    return False
            else:
                if w[i] in d.values():
                    return False
                d[pattern[i]] = w[i]

        for i in range(len(pattern)):
            c += d[pattern[i]] + ' '

        c = c.strip()

        if s == c:
            return True
        return False
                
