# 1436
# You are given the array paths, where paths[i] = [cityAi, cityBi] means there
# exists a direct path going from cityAi to cityBi. Return the destination city,
#  that is, the city without any path outgoing to another city.
# It is guaranteed that the graph of paths forms a line without any loop,
# therefore, there will be exactly one destination city.

# EXAMPLES
# Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
# Output: "Sao Paulo"
# Explanation: Starting at "London" city you will reach "Sao Paulo" city which is the destination city.
# Your trip consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo".


def destCity(paths):
    d = set()
    o = set()
    for lst_cities in paths:
        outgoing, destination = lst_cities
        o.add(outgoing)
        d.add(destination)

    result = (d.difference(o))

    for res in result:
        return res


print(destCity([["pYyNGfBYbm", "wxAscRuzOl"], ["kzwEQHfwce", "pYyNGfBYbm"]]))


# --------------------------------------------------------------------------------------------------------

# 1365
# Given the array nums, for each nums[i] find out how many numbers
# in the array are smaller than it. That is, for each nums[i] you
# have to count the number of valid j's such that j != i and nums[j] < nums[i].
# Return the answer in an array.

# EXAMPLE:
# Input: nums = [8,1,2,2,3]
# Output: [4,0,1,1,3]


def smallerNumbersThanCurrent(nums):
    copy_list = nums[:]
    result_list = []

    for number in nums:
        count = 0
        for copy_number in copy_list:
            if number != copy_number and number > copy_number:
                count += 1
        result_list.append(count)

    return result_list


# -------------------------------------------------------------------------------------------------------

# 6
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
# (you may want to display this pattern in a fixed font for better legibility)
# And then read line by line: "PAHNAPLSIIGYIR"
# Write the code that will take a string and make this conversion given a number of rows:
# string convert(string s, int numRows);


# Example:

# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"


def convert(s, numRows):
    # first let's create a dictionary, where we are going to store the chars for each row

    # P   A
    # A P L
    # Y   I ...

    # If numRows is 3, the sequence of rows would be 123212321 ...

    d = {row: "" for row in range(1, numRows + 1)}

    # we are starting at row 1:

    row = 1

    # we need to have a variable up, so when the count is less than the numRows, we can deactivate it

    up = True

    for char in s:
        d[row] += char
        print(d)
        if row == 1 or (row < numRows and up):
            row += 1
            up = True
        else:
            row -= 1
            up = False

    print(d)

    convert = ""

    for value in d.values():
        convert += value

    return convert


# print(convert("PAYPALISHIRING", 3))

nums = [-1, 2, 1, -4]
target = 1


def sum_closest_target(nums, target):

    nums = sorted(nums)
    closest = 10000000
    for i in range(len(nums) - 2):

        lower = i + 1
        higher = len(nums) - 1

        while lower < higher:

            sum = nums[i] + nums[lower] + nums[higher]

            if sum == target:
                return sum

            if abs(target - sum) < abs(target - closest):
                closest = sum

            if sum <= target:
                lower += 1

            if sum > target:
                higher -= 1

    return closest


# print(sum_closest_target([4, 0, 5, -5, 3, 3, 0, -4, -5], -2))


# 121. Best Time to Buy and Sell Stock

# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.


def stock(prices):

    buy, sell = 0, 1
    profit = 0

    while sell < len(prices):
        if prices[buy] < prices[sell]:
            earnings = prices[sell] - prices[buy]
            profit = max(profit, earnings)

        else:
            buy = sell

        sell += 1

    return profit


nums = [60, 3, 2]
k = 0


def twoSumLessThanK(nums, k):

    nums.sort()
    answer = -1
    left = 0
    right = len(nums) - 1

    while left < right:
        sum = nums[left] + nums[right]
        if sum < k:
            answer = max(answer, sum)
            left += 1

        else:
            right -= 1

    return answer


# print(twoSumLessThanK(nums, k))


# 482. License Key Formatting
# Easy

# You are given a license key represented as a string s that consists of only alphanumeric characters and dashes. The string is separated into n + 1 groups by n dashes. You are also given an integer k.

# We want to reformat the string s such that each group contains exactly k characters, except for the first group, which could be shorter than k but still must contain at least one character. Furthermore, there must be a dash inserted between two groups, and you should convert all lowercase letters to uppercase.

# Return the reformatted license key.


# Example 1:

# Input: s = "5F3Z-2e-9-w", k = 4
# Output: "5F3Z-2E9W"
# Explanation: The string s has been split into two parts, each part has 4 characters.
# Note that the two extra dashes are not needed and can be removed.


def licenseKeyFormatting(s, k):

    chars = s.split("-")
    print(chars)
    str_chars = ""

    for item in chars:
        str_chars += item

    str_chars = str_chars[::-1]

    result = ""

    count = 0

    for char in str_chars:
        if count == k:
            result += "-"
            count = 0

        result += char.upper()
        count += 1

    return result[::-1]


print(licenseKeyFormatting("2713nh-31sj", 3))


# 905. Sort Array By Parity
# Easy

# Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

# Return any array that satisfies this condition.


# Example 1:

# Input: nums = [3,1,2,4]
# Output: [2,4,3,1]
# Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

# Example 2:

# Input: nums = [0]
# Output: [0]

def sortArrayByParity(nums):

    odds = []
    even = []

    for num in nums:
        if num % 2 == 0:
            even.append(num)
        else:
            odds.append(num)

    return even + odds


nums = [0, 1, 0, 3, 12]

zeros = []

sort_lst = sorted(nums)
print(sort_lst)

for num in sort_lst:
    if num == 0:
        zeros.append(num)
    if num > 0:
        break

print(sort_lst + zeros)


# 283. Move Zeroes
# Easy

# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.


# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Example 2:

# Input: nums = [0]
# Output: [0]

def moveZeroes(nums):

    left = 0
    for i in range(len(nums)):
        print(nums[i])
        if nums[i] != 0:
            nums[i], nums[left] = nums[left], nums[i]
            left += 1

    return nums

# 268. Missing Number
# Easy

# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.


# Example 1:

# Input: nums = [3,0,1]
# Output: 2
# Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

# Example 2:

# Input: nums = [0,1]
# Output: 2
# Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

# Example 3:

# Input: nums = [9,6,4,2,3,5,7,0,1]
# Output: 8
# Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.


def missingNumber(self, nums: List[int]) -> int:

    # numbers = range(0,10**4)

    # range_num = set(numbers[:(len(nums) + 1)])

    # nums = set(nums)

    # for num in range_num.difference(nums):
    # return num

    complete_list = True
    nums.sort()

    for i in range(len(nums) - 1):
        if nums[i + 1] != (nums[i] + 1):
            complete_list = False
            return (nums[i] + 1)

    if complete_list == True:
        if nums[0] == 0:
            return (nums[-1] + 1)
        else:
            return 0
