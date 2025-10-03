class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        dict_ = {}
        total = len(nums)//3

        for num in nums:
            if num in dict_:
                dict_[num]+=1
            else:
                dict_[num] = 1
        
        for key, value in dict_.items():
            if value > total:
                ans.append(key)
        
        return ans
