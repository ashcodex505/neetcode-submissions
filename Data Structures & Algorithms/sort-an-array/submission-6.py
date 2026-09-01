class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:


        #the idea of merge sort is to split up all nums into indivdual element  of the array with the smallest space comp[lexit
        #two thngs happening here 1 is we are going to partiton and then we are going to merge and each is going ot happen recursively 
        #what we are going to do is update the orginal array instead of making anew one to reduce space complexity 


        def merge(orgN,n1, n2):
            #two pointers 
            l0 = 0
            l1, l2 = 0, 0
            
            while l1 < len(n1) and l2 < len(n2):
                if n1[l1] <= n2[l2]:
                    orgN[l0] = n1[l1]
                   
                    l1 += 1 
                else:
                    orgN[l0] = n2[l2]
                
                    l2 += 1 
                l0 += 1 
            
            
            orgN[l0: ] = n1[l1:] if l1 < len(n1) else n2[l2:]
            
            return orgN


                

        def mergeSort(nums):

            #base case 
            if len(nums) <= 1:
                return nums
            

            #paritiont 
            m = len(nums) // 2

            n1 = mergeSort(nums[:m])
            n2 = mergeSort(nums[m:])

            return merge(nums, n1, n2)






        return mergeSort(nums)
         


        