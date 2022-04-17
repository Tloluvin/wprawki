# Finish the solution so that it sorts the passed in array of numbers. If the function passes in an empty array or null/nil value then it should return an empty array.

def solution(nums):
    return sorted(nums) if nums != None else []


print(solution([1,2,3,10,5]))   # should return [1,2,3,5,10]
print(solution(None))           # should return []
print(solution([]))             # should return []
print(solution([20,2,10]))      # should return [2,10,20]
print(solution([2,20,10]))      # should return [2,10,20]
