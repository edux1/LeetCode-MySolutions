class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        q = deque([])
        i, count = 0, 0
        k = k % len(nums)
        while i < len(nums):
            q.append(nums[i])
            if count >= k:
                nums[i] = q.popleft()
            count += 1
            i += 1
        j = 0
        while j < k and len(q) >= 1:
            nums[j] = q.popleft()
            j += 1 





