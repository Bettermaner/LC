# 78. 子集, 给定数组中无重复数


class Solution:
    def subsets(self, nums):		
        if not nums:
            return []
        res = []
        n = len(nums)

        def helper(idx, temp_list):
            res.append(temp_list)
            for i in range(idx, n):
                helper(i + 1, temp_list + [nums[i]])

        helper(0, [])
        return res


# 90. 子集 II， 给定数组中有重复数


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        n = len(nums)
        res = []
        nums.sort()
		# 思路1
        def helper1(idx, n, temp_list):
            if temp_list not in res:
                res.append(temp_list)
            for i in range(idx, n):
                helper1(i + 1, n, temp_list + [nums[i]])
		# 思路2
        def helper2(idx, n, temp_list):
            res.append(temp_list)
            for i in range(idx, n):
                if i > idx and  nums[i] == nums[i - 1]:
                    continue
                helper2(i + 1, n, temp_list + [nums[i]])

        helper2(0, n, [])
        return res



# 46. 全排列，给定字符中无重复字符


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return
        res = []
        n = len(nums)
        visited = [0] * n
        def helper1(temp_list,length):
            if length == n:
                res.append(temp_list)
            for i in range(n):
                if visited[i] :
                    continue
                visited[i] = 1
                helper1(temp_list+[nums[i]],length+1)
                visited[i] = 0
        def helper2(nums,temp_list,length):
            if length == n:
                res.append(temp_list)
            for i in range(len(nums)):
                helper2(nums[:i]+nums[i+1:],temp_list+[nums[i]],length+1)
        helper1([],0)
        return res


# 47. 全排列 II ，给定字符中有重复字符


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        nums.sort()
        n = len(nums)
        visited = [0] * n
        res = []

        def helper1(temp_list, length):
            # if length == n and temp_list not in res:
            # 	res.append(temp_list)
            if length == n:
                res.append(temp_list)
            for i in range(n):
                if visited[i] or (i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]):
                    continue
                visited[i] = 1
                helper1(temp_list + [nums[i]], length + 1)
                visited[i] = 0

        def helper2(nums, temp_list, length):
            if length == n and temp_list not in res:
                res.append(temp_list)
            for i in range(len(nums)):
                helper2(nums[:i] + nums[i + 1:], temp_list + [nums[i]], length + 1)


# 39.组合总和，每个数字在每个组合中可以使用无数次 。


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return []
        if min(candidates) > target:
            return []
        candidates.sort()
        res = []

        def helper(candidates, target, temp_list):
            if target == 0:
                res.append(temp_list)
            if target < 0:
                return
            for i in range(len(candidates)):
                if candidates[i] > target:
                    break
                helper(candidates[i:], target - candidates[i], temp_list + [candidates[i]])
        helper(candidates,target,[])
        return res


# 40. 组合总和 II，每个数字在每个组合中只能使用 一次 。


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        candidates.sort()
        n = len(candidates)
        res = []
        
        def backtrack(i, tmp_sum, tmp_list):
            if tmp_sum == target:
                res.append(tmp_list)
                return 
            for j in range(i, n):
                if tmp_sum + candidates[j]  > target : break
                if j > i and candidates[j] == candidates[j-1]:continue
                backtrack(j + 1, tmp_sum + candidates[j], tmp_list + [candidates[j]])
        backtrack(0, 0, [])    
        return res