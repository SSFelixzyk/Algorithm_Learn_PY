import collections


def twoSum(nums, target):
    # 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    table = {}
    
    for i, num in enumerate(nums):
        j = table.get(target-num)
        if j is None:
            table[num] = i 
        else:
            return [i,j]

def groupAnagrams(strs):
    # 给定一个字符串数组，将字母异位词组合在一起。字母异位词是由重新排列字母得到的相同字符串。
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    
    groups = collections.defaultdict(list)
    for s in strs:
        count = [0]*26
        for ch in s:
            count[ord(ch)-ord("a")]+=1
        groups[tuple(count)].append(s)

    return groups.values()

def longestConsecutive(nums):
    # 给定一个未排序的整数数组 nums ，返回最长连续序列的长度。
    """
    :type nums: List[int]
    :rtype: int
    """

    nums_set = set(nums)
    res = 0

    for num in nums_set:
        if num-1 not in nums_set:
            cur_len = 1
            current = num

            while current+1 in nums_set:
                current +=1
                cur_len +=1
            
            res = max(res,cur_len)

    return res

def moveZeroes(nums):
    # 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    slow = 0
    n = len(nums)
    for fast in range(n):
        if nums[fast] != 0:
            nums[slow] = nums[fast]
            slow += 1
    
    nums[slow:] = [0]*(n-slow)

def maxArea(height):
    # 给定 n 个非负整数 a1, a2, ..., an，其中每个数代表坐标中的一个点 (i, ai) 。n 个点形成的容器可以容纳最多多少水。
    """
    :type height: List[int]
    :rtype: int
    """
    n = len(height)

    left = 0
    right = n-1

    water = 0

    while left < right and left < n-1 and right > 0:

        if height[left] <= height[right]:
            water = max(water, height[left]*(right-left))
            left +=1
        else:
            water = max(water, height[right]*(right-left))
            right -=1
    
    return water

def threeSum(nums):
    # 给你一个整数数组 nums ，判断是否存在三元组 [nums[a], nums[b], nums[c]] ，使得 0 <= a, b, c < n ，且 a、b、c 互不相同，nums[a] + nums[b] + nums[c] == 0 。请你返回所有和为 0 且不重复的三元组。
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """

    nums.sort()
    n = len(nums)
    res = []

    for i, num in enumerate(nums):
        if i == 0 or num != nums[i-1]:
            right = n-1
            left = i +1
            while left < right:
                if left == i+1 or nums[left] != nums[left-1]:
                    while num + nums[left] + nums[right] > 0 and right > left:
                        right -= 1
                    if left == right:
                        break
                    if num + nums[left] + nums[right] == 0:
                        res.append([num,nums[left],nums[right]])
                left += 1

    return res

def trap(height):
    # 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
    """
    :type height: List[int]
    :rtype: int
    """
    n = len(height)
    leftmax = height[0]
    rightmax = height[n-1]
    i = 1
    j = n-2

    res = 0

    while i <= j:
        
        if leftmax < rightmax:
            leftmax = max(leftmax,height[i])
            res += max(leftmax - height[i], 0)
            i += 1

        else:
            rightmax = max(rightmax,height[j])
            res += max(rightmax - height[j], 0)
            j -= 1
    
    return res
    
def lengthOfLongestSubstring(s):
    # 给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。
    """
    :type s: str
    :rtype: int
    """
    n = len(s)
    hasChar = {}
    left, right = 0, 0
    res = 0

    while left <= right and right < n:
        c = s[right]

        if hasChar.get(c, 0):
            res = max(res, right - left)
            while True:
                if s[left] == c:
                    left += 1
                    break
                del hasChar[s[left]]
                left += 1
        else:
            hasChar.setdefault(c,1)

        right += 1

    res = max(res, right - left)
    
    return res

def findAnagrams(s, p):
    # 给定一个字符串 s 和一个 字符串 p ，找到 s 中所有 p 的 字母异位词 的子串的下标。
    """
    :type s: str
    :type p: str
    :rtype: List[int]
    """
    window = len(p)
    n = len(s)

    if window > n:
        return []
    
    count = [0]*26
    res = []

    for i in range(window):
        count[ord(s[i])-97] +=1
        count[ord(p[i])-97] -=1
    
    differ = [c!=0 for c in count].count(True)
    
    if differ == 0:
        res.append(0)

    for i in range(n-window):

        # 左边界的字母
        if count[ord(s[i])-97] == 1:
            differ -= 1
        elif count[ord(s[i])-97] == 0:
            differ += 1

        count[ord(s[i])-97] -= 1

        # 右边界的字母
        if count[ord(s[i+window])-97] == -1:
            differ -= 1
        elif count[ord(s[i+window])-97] == 0:
            differ += 1

        count[ord(s[i+window])-97] += 1


        if differ == 0:
            res.append(i+1)
    
    return res

def subarraySum(nums, k):
    # 给定一个整数数组 nums 和一个整数 k ，请你返回子数组中元素的总和等于 k 的个数。
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    # 前缀和 转换成 两数和(差)
    n = len(nums)
    pre_sum = [0]*n

    pre_sum[0] = nums[0]
    for i, num in enumerate(nums):
        if i==0:
            continue
        pre_sum[i] = pre_sum[i-1] + num
    
    table = {}
    count = 0

    table[0] = 1
    for i, presum in enumerate(pre_sum):
        times = table.get(presum - k)
        table[presum] = table.get(presum, 0) + 1
        if times is not None:
            count += times

    return count