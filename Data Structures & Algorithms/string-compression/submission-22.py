class Solution:
    def compress(self, chars: List[str]) -> int:
      #requires two poiner solution for u to do it 

      insert = 0
      i = 0

      #return numbers but we are also supoose to change the original array 
      #our i block is basically our read piinter while our insert is our write pointer 
      while i < len(chars):
        group = 1 

        while (group+i) < len(chars) and chars[i+group] == chars[i]:
            group += 1 
        
        chars[insert] = chars[i]
        insert += 1 
        if group > 1: 
            len_str = list(str(group))
            chars[insert: insert + len(len_str)] = len_str 
            insert += len(len_str)
        
        i += group #read pointer has now been updated 
    
      return insert 


        

