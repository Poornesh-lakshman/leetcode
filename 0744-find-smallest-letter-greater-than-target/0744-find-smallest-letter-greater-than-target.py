class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        d=[]
        for i in letters:
            if ord(i)>ord(target):
                d.append(ord(i))
        if len(d)==0:
            return letters[0]
        else:
            sorted(d)
            return chr(d[0])