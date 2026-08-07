class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        a='abcdefghijklmnopqrstuvwxyz'
        for i in a:
            if i in sentence:
                continue
            else:
                return False
        return True