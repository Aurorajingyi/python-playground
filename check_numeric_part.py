class Solution:
    def check_numeric_parts(self,s:str)->list:
        parts=s.split("+")
        for idx,part in enumerate(parts,1):
            if not part.isdecimal():
                return[False,f"Part{idx},'{part}'is not numeric"]
        return[True,"All parts are numeric"]

 #Testing code
sol = Solution()
print(sol.check_numeric_parts("+4"))
