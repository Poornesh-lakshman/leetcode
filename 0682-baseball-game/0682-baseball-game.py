class Solution:
    def calPoints(self, operations: List[str]) -> int:
        op=operations
        d=[]
        for i in range(len(op)):
            if op[i]=='C':
                d.pop()
            elif op[i]=='D':
                d.append(d[-1]*2)
            elif op[i]=='+':
                d.append(d[-2]+d[-1])
            else:
                d.append(int(op[i]))
        return sum(d)