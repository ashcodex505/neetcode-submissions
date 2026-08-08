class Solution:
    def search(self, nums: List[int], target: int) -> int:
      
      #doing this problme again 

      #so we do binary search with left and right pointers and basically we need to figure out first if we're in the left or 
      #the right portion of the array and then find if we need to search left or right based on where the mid is and the left and right pointers are 

      #need to set our left and right pointers 
        l, r = 0, len(nums) - 1 #bc we need to be able to directly access the string at pointer r 

        while l <= r: #bc our array could just be left with this [2] in which left and right would be equal 

            #calculate middle between left and right pointers 
            mid = (l + r) // 2
            #then we check if nums[mid] == target if it does we just return that index 
            if nums[mid] == target: 
                return mid 
            #now we check if the position at the mid is in the left portion or right portion of the array 

            #left portion - meaning our nums[mid] >= nums[l] bc it could be possible that our left pointer and mid pointer at pointing to the same thing  and target < nums[mid] and target > nums[l]
            if nums[mid] >= nums[l]:
                if target > nums[mid] or target < nums[l]:
                    #we know we need to go to the right portion so we change th eleft pointer 
                    l = mid + 1
                else: #if the first conditional is not true then we know target > nums[l] and nums[mid] > target 
                    #and so we change right pointer 
                    r = mid - 1
            #right portion meaning nums[mid] < nums[l]
            else:
                #now we check nums[mid] < nums[r] 
                if target < nums[mid] or target > nums[r]:
                    #now we change to search the left portion 
                    r = mid - 1
                else:
                    #if that condition is not true we know nums[mid] < nums[r] and target < nums[r]
                    #meaning that we can change our left pointer to search here
                    l = mid + 1 
    #if we search throuhg entire array and l and r pointers cross each other we know we have not found any number that matches the target so we return - 1
        return -1



        