---------------1470. Shuffle the Array-----------------
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        list1=[]
        list2=[]
        list3=[]
        
        for i in range(0,(len(nums)//2)):
            if i<n:
                list1.append(nums[i])
                list1.append(nums[i+n])        
        return(list1)
---------------------1528. Shuffle String---------------
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        s_new = ''
        
        for i in range(len(indices)):
            s_new += s[indices.index(i)]
            
        print(s_new)
 ---------------2114. Maximum Number of Words Found in Sentences--------------
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        
        list1=[]
        
        for i in sentences:
            list1.append (len(i.split()))
            
        return max(list1) 
