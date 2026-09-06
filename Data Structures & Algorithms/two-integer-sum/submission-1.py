class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        res = []
        
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff not in dic.keys():
                dic[nums[i]] = i
            else:
                res.append(dic[diff])
                res.append(i)
        
        return res
            
### idea ###
# form an eqn to prevent nested loop (diff)
# check if diff exsist as a key and the val is the ind
# else store the curr element in dict n val is ind