class Solution:
    def average(self, salary: List[int]) -> float:
        # a=min(salary)
        # b=max(salary)
        # salary.remove(a)
        # salary.remove(b)
        # return sum(salary)/len(salary)

        avg = (sum(salary) - max(salary) - min(salary)) / (len(salary) - 2)
        return avg