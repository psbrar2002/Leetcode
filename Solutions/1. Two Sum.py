'''
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Input: nums = [3,2,4], target = 6
Output: [1,2]

Input: nums = [3,3], target = 6
Output: [0,1]
'''
# Brute Force Approach: 

# Time Complexity: O(n^2)
# Space Complexity: O(1)
def btwoSum(nums,target):
    for i in range(len(nums)): # First loop to loop the nums array from the start
        for j in range(i+1,len(nums)): # Second loop to loop the nums array one step ahead of the first loop so we can compare 
            if nums[i] + nums[j] == target: # Compare to check if adding up the values equal our target value 
                return [i, j] # If they do equal the target we would just return the indicies of both values 


# Optimal Solution: 

# Time Complexity: O(n)
# Space Complexity: O(n)
def twoSum(nums,target):
    dict = {} # Intiialize a dictionary 

    for i in range (0,len(nums)): # Loop through each value in nums 
        diff = target-nums[i]  # Take the difference of the value you are currently on and the target value to get the difference (This value will be in the nums list)

        if diff in dict: # Check if we discover the diff in the dictionary
            return [dict[diff],i] # Return the index of diff in the array and the index of i  
        
        dict[nums[i]] = i # Assign the value of i to the key nums[i]



isBrute = input("Enter yes for a brute force solution and no for an optimal solution: ")
if isBrute == "yes":
    print(btwoSum([2,7,11,15],9))
    print(btwoSum([3,2,4],6))
    print(btwoSum([3,3],6))
    print("brute")
elif isBrute == "no": 
    print(twoSum([2,7,11,15],9))
    print(twoSum([3,2,4],6))
    print(twoSum([3,3],6))
    print("not brute")
else:
    print("Invalid input")