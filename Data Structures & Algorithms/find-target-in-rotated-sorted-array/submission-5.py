class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #so we are searchuing using binary search algorithm 
        #so we divide the array in two and keep doing it until we reach the target 
        #how do you write. binary search alogrithm in python? 
        #first we need to find the point where we cut 

        #okat we need a left and right pointer solution for this where ew figure out if we're in the right or left sorted portion fo the array 
        l, r = 0, len(nums) - 1 #bc we are going to be using nums[r] directly so we need it to be at len(nums) - 1 

        while l <= r: #we need the equals becasue if its just one element in the array we can check fro it as well 
            mid = (l+r) // 2 
            if nums[mid] == target:
                return mid
            #as we move these pointer throuhg the array we will get to search for our target using binary search with left and right pointers 
            #left portion 
            if nums[mid] >= nums[l]:
                if nums[mid] < target or nums[l] > target: #this means we need to search teh right portion then 
                    l = mid + 1 
                else:
                    r = mid - 1 #now we are searching throuhg left 
            #right portion 
            else: #basically nums[mid] < nums[l] and so now we need to serarc throuhg right portion 
                if target < nums[mid] or target > nums[r]: #here we then search left portion instead 
                    r = mid - 1
                else: #we actually are searching the right portion 
                    l = mid + 1

            


        return -1



        