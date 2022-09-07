from sys import stdin

class Matrix:
    def __init__(self, li):
        self.li = li.copy()
    
    def __str__(self):
        res = ''
        for row in self.li:
            line = '\t'.join([str(symbol) for symbol in row])
            res += line + '\n'
        return res[:-1]

    def size(self):
        return len(self.li), len(self.li[0])

exec(stdin.read())
