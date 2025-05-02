# binary search
# Given a sorted array and a target value, return the index of the target value in the array. If the target value is not found, return -1.
# You must write an algorithm with O(log n) runtime complexity.
# 1. target belongs to [left,right]
# at this time, left = right is valid
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# 2. target belongs to [left,right)
# at this time, left = right is invalid
def binary_search_RightOpen(arr, target):
    left = 0
    right = len(arr)

    while left < right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid

    return -1

def DivideArea():
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])

    row_sum = [0 for _ in range(n)]
    col_sum = [0 for _ in range(m)]

    for i in range(n):

        row = input().split()

        r = 0
        for j in range(m):
            r += int(row[j])
            col_sum[j] += int(row[j])
        row_sum[i] = r

    pre_row = [0]*n
    pre_col = [0]*m

    s = 0
    for i in range(n):
        s += row_sum[i]
        pre_row[i] = s

    s = 0
    for j in range(m):
        s += col_sum[j]
        pre_col[j] = s

    diff = 100000
    total = pre_row[-1]
    for i in range(n):
        diff = min(diff, abs(2*pre_row[i] - total))

    for j in range(m):
        diff = min(diff, abs(2*pre_col[j] - total))

    print(diff)

class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):

        self.head = None
        self.mid = None
        self.tail = None

        self.midplus = 0
        self.size = 0
    
    def add(self,val):
        if self.size==0:
            self.head = Node(val)
            self.tail = self.head
            self.mid = self.head
        
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next
            self.midplus += 1
        
        self.size += 1
        if self.midplus == 2:
            self.midplus = 0
            self.mid = self.mid.next
    
    def remove(self,index):
        pass




