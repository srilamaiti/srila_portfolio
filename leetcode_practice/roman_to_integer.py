# https://leetcode.com/problems/roman-to-integer/
class Solution:
    def romanToInt(self, s: str) -> int:
        split_literals = list(s)
        letter_dict = {"I": 1,
                       "V": 5,
                       "X": 10,
                       "L": 50,
                       "C": 100,
                       "D": 500,
                       "M": 1000
                      }
        spl_cases_dict = {'IV' : 4, 
                          'IX': 9, 
                          'XL': 40, 
                          'XC': 90, 
                          'CD': 400, 
                          'CM': 900
                         }
        res_list = []
        i = 0
        while i < len(split_literals):
            if ''.join(split_literals[i : i + 2]) in spl_cases_dict.keys():
                res_list.append(spl_cases_dict[''.join(split_literals[i : i + 2])])
                i += 2
            else:
                res_list.append(letter_dict[split_literals[i]])
                i += 1
        return sum(res_list)