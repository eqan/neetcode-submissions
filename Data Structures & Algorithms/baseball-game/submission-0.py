class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []
        for i in range(len(operations)):
            _res = 0
            if operations[i] != 'C':
                if operations[i] == '+':
                    _res = res[-1] + res[-2]
                elif operations[i] == 'D':
                    _res = res[-1] * 2
                else:
                    _res = int(operations[i])
                res.append(_res)
            else:
                res.pop()
        return sum(res)