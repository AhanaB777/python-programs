"""The next greater element of some element x in an array is the first greater element that 
is to the right of x in the same array. 
You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a 
subset of nums2. 
For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and 
determine the next greater element of nums2[j] in nums2. If there is no next greater 
element, then the answer for this query is -1. 
Return an array ans of length nums1.length such that ans[i] is the next greater element as 
described above. 
Example 1: 
Input: nums1 = [4,1,2], nums2 = [1,3,4,2] 
Output: [-1,3,-1] 
Explanation: The next greater element for each value of nums1 is as follows: 
• 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer 
is -1. 
• 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3. 
• 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer 
is -1."""
nums1 = [4,1,2]
nums2 = [1,3,4,2]
res=[]
for i in range(0,len(nums1)):
    pass
ans=[]
for x in nums1:
        # Find the index of x in nums2
    index_in_nums2 = nums2.index(x)
        
        # Assume there is no next greater element
    next_greater = -1
        
        # Look to the right of index_in_nums2 in nums2
    for j in range(index_in_nums2 + 1, len(nums2)):
        if nums2[j] > x:
            next_greater = nums2[j]
            break  # Stop as soon as we find the first greater element
        
        # Add the result for this element
    ans.append(next_greater)
print(ans)
