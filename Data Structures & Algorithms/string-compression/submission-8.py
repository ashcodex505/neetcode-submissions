class Solution:
    def compress(self, chars: List[str]) -> int:
       #need to remember for palantir si that u need to think out loud they dont care about syntax at all 
       
       #alog needs to use O(1) space complexity 
       #we are looping throug hthe string list of chars 
       #saying to do a two pointer solution 

       #two pointer solution one insert pointer and i pointer 
       #insert pointer that is our writer pointer 
       insert = 0
       i = 0 
       while i < len(chars):
            group = 1 
            while group + i < len(chars) and chars[group+i] == chars[i]:
                group += 1
            
            chars[insert] = chars[i]
            insert += 1

            if group > 1:
                str_list = list(str(group))
                chars[insert:insert+len(str_list)] = str_list
                insert += len(str_list)
            
            
            i += group 
       return insert