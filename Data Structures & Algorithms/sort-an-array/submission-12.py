class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:


        #the idea of merge sort is to split up all nums into indivdual element  of the array with the smallest space comp[lexit
        #two thngs happening here 1 is we are going to partiton and then we are going to merge and each is going ot happen recursively 
        #what we are going to do is update the orginal array instead of making anew one to reduce space complexity 


        def merge(org,n1, n2):
            #two pointers 
            orgN = []
            l0 = 0
            l1, l2 = 0, 0
            
            while l1 < len(n1) and l2 < len(n2):
                if n1[l1] <= n2[l2]:
                    orgN.append(n1[l1])
                   
                    l1 += 1 
                else:
                    orgN.append(n2[l2])
                
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

            n1 = mergeSort(nums[:m]) #creates a copy and puts thati nto the funciton 
            n2 = mergeSort(nums[m:])

            return merge(nums, n1, n2)






        # return mergeSort(nums)
         
#^^this oslution take O(n) space we dont want that we want  

        # def merge(arr, L, M, R):
        #     #two pointers 
        #     left, right = arr[L:M], arr[M:R]
        #     i, j, k = L, 0, 0 
        #     #j and k are both pointer for the left and rihgt subarrays that we are pointing to
        #     while j < len(left) and k < len(right):
        #         if left[j] < right[k]:
        #             arr[i] = left[j]
        #             j += 1
        #         else:
        #             arr[i] = right[k]
        #             k += 1
        #         i += 1

        #     while j < len(left):
        #         arr[i] = left[j]
        #         j += 1
        #         i += 1 
            
        #     while k < len(right):
        #         arr[i] = right[k]
        #         k += 1
        #         i += 1


            


                

        # def mergeSort(nums, l, r):

        #     #base case 
        #     if r - l <= 1:
        #         return
            

        #     #paritiont 
        #     m = (r + l) // 2 

        #     mergeSort(nums, l, m) #creates a copy and puts thati nto the funciton 
        #     mergeSort(nums, m, r)

        #     merge(nums,l, m, r)


        return mergeSort(nums)
      

        