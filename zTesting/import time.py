
import time
def create_list(n):
    return list(range(1,n+1)) + [1]
big = create_list(1000000)
def find_repeating_twice(nums):
    for i in range(len(nums)):
        for j in range (i+1, len(nums)):
            if nums[i] == nums[j]:
                return nums[i]
        return None
start_time = time.time()
find_repeating_twice(big)
end_time = time.time()
print(f"{end_time - start_time}")
