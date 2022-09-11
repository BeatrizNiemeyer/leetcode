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
    dict_cities = {}

    for list_of_cities in paths:
        outgoing, destination = list_of_cities
        dict_cities[outgoing] = dict_cities.get(outgoing, 0) + 1
        dict_cities[destination] = dict_cities.get(destination, 0)

    print(dict_cities)

    for city, value in dict_cities.items():
        if city == destination and value == 0:
            return city


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

    #[1, 8, 23, 24, 33, 34, 54, 75]

    higher_sum = "0"
    result_exists = False

    for i in range(len(nums) - 1):
        increment = 0

        if nums[i] > k:
            continue

        if nums[i] == k:
            return k

        while increment < len(nums) - 1:
            next = increment + 1

            if nums[next] < k:
                result = (nums[i] + nums[next])
                print(nums[i], nums[next])
                print(result)
                print(higher_sum)
                if result < 60:
                    result_exists = True
                    higher_sum = max(int(higher_sum), result)
            increment += 1

    if not result_exists:
        return -1
    return higher_sum


# print(twoSumLessThanK(nums, k))
