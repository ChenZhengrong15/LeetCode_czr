# coding: UTF-8
# 写一个自动机


'''
            ' '	    +/-	    number	    other
start	    start	signed	in_number	end
signed	    end	    end	    in_number	end
in_number	end	    end	    in_number	end
end	        end	    end	    end	        end
'''

INT_MAX = 2 ** 31 - 1
INT_MIN = -2 ** 31


class Automaton:
    def __init__(self):
        self.state = 'start'
        self.sign = 1
        self.ans = 0
        self.table = {
            'start': ['start', 'signed', 'in_number', 'end'],
            'signed': ['end', 'end', 'in_number', 'end'],
            'in_number': ['end', 'end', 'in_number', 'end'],
            'end': ['end', 'end', 'end', 'end']
        }

    def get_col(self, ch: str) -> int:
        if ch.isspace():
            return 0
        if ch == '+' or ch == '-':
            return 1
        if ch.isdigit():
            return 2
        return 3

    def convert(self, ch):
        self.state = self.table[self.state][self.get_col(ch)]
        if self.state == 'in_number':
            self.ans = self.ans * 10 + int(ch)
            self.ans = min(self.ans, INT_MAX) if self.sign == 1 else min(-INT_MIN, self.ans)
            print(self.ans)
        elif self.state == 'signed':
            self.sign = 1 if ch == "+" else -1


class Solution:
    def myAtoi(self, str: str) -> int:
        automaton = Automaton()
        for ch in str:
            automaton.convert(ch)
        return automaton.ans * automaton.sign


s = Solution()
print(s.myAtoi("+1"))
