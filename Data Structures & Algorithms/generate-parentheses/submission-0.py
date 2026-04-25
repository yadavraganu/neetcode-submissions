class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        temp_str = []   
        
        def _helper(open_num, close_num):
            
            if open_num == close_num == n:
                res.append(''.join(temp_str))

            if open_num < n:
                temp_str.append('(')
                _helper(open_num + 1, close_num)
                temp_str.pop()
            
            if close_num < open_num:
                temp_str.append(')')
                _helper(open_num, close_num + 1)
                temp_str.pop()
            
        _helper(0,0)  
        
        return res

        