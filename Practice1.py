class Solution(object):
    def containsDuplicate(self, nums):
        list.sort(nums);
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                return True;
        return False;
        