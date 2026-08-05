class Solution(object):
    def calPoints(self, operations):
        x = []
        for ops in operations:
            if ops.lstrip("-+").isnumeric():
                x.append(int(ops))
            elif ops == "C":
                x.pop()
            elif ops == "D":
                x.append(x[-1]*2)
            
            elif ops == "+":
                x.append(x[-1] + x[-2])
                
        return sum(x)