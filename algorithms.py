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

    result = []

    for i in range(len(nums) - 1):
        left = i + 1
        right = len(nums)
        while left < right:
            if nums[i] + nums[left] == target:
                return [i, left]
            else:
                left += 1

    return result


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


def missingNumber(nums):

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


# 529. Minesweeper
# Medium

# Let's play the minesweeper game (Wikipedia, online game)!

# You are given an m x n char matrix board representing the game board where:

#     'M' represents an unrevealed mine,
#     'E' represents an unrevealed empty square,
#     'B' represents a revealed blank square that has no adjacent mines (i.e., above, below, left, right, and all 4 diagonals),
#     digit ('1' to '8') represents how many mines are adjacent to this revealed square, and
#     'X' represents a revealed mine.

# You are also given an integer array click where click = [clickr, clickc] represents the next click position among all the unrevealed squares ('M' or 'E').

# Return the board after revealing this position according to the following rules:

#     If a mine 'M' is revealed, then the game is over. You should change it to 'X'.
#     If an empty square 'E' with no adjacent mines is revealed, then change it to a revealed blank 'B' and all of its adjacent unrevealed squares should be revealed recursively.
#     If an empty square 'E' with at least one adjacent mine is revealed, then change it to a digit ('1' to '8') representing the number of adjacent mines.
#     Return the board when no more squares will be revealed.


# Example 1:

# Input: board = [["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]], click = [3,0]
# Output: [["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]

# Example 2:

# Input: board = [["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]], click = [1,2]
# Output: [["B","1","E","1","B"],["B","1","X","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]


# Constraints:

#     m == board.length
#     n == board[i].length
#     1 <= m, n <= 50
#     board[i][j] is either 'M', 'E', 'B', or a digit from '1' to '8'.
#     click.length == 2
#     0 <= clickr < m
#     0 <= clickc < n
#     board[clickr][clickc] is either 'M' or 'E'.


class Solution:

    def getNumsMines(self, board, x, y):

        numsMines = 0

        for r in range(x-1, x + 2):
            for c in range(y-1, y+2):
                if r >= 0 and r < len(board) and c >= 0 and c < len(board[r]) and board[r][c] == "M":
                    numsMines += 1

        return numsMines

    def updateBoard(self, board, click):

        if not board:
            return board

        x, y = click

        if board[x][y] == "M":
            board[x][y] = "X"

        else:
            numsMines = self.getNumsMines(board, x, y)
            if numsMines:
                board[x][y] = str(numsMines)
            else:
                board[x][y] = "B"
                for r in range(x-1, x + 2):
                    for c in range(y-1, y+2):
                        if r >= 0 and r < len(board) and c >= 0 and c < len(board[r]) and board[r][c] != "B":
                            self.updateBoard(board, [r, c])

        return board


# 1861. Rotating the Box
# Medium

# You are given an m x n matrix of characters box representing a side-view of a box. Each cell of the box is one of the following:

#     A stone '#'
#     A stationary obstacle '*'
#     Empty '.'

# The box is rotated 90 degrees clockwise, causing some of the stones to fall due to gravity. Each stone falls down until it lands on an obstacle, another stone, or the bottom of the box. Gravity does not affect the obstacles' positions, and the inertia from the box's rotation does not affect the stones' horizontal positions.

# It is guaranteed that each stone in box rests on an obstacle, another stone, or the bottom of the box.

# Return an n x m matrix representing the box after the rotation described above.

def rotateTheBox(box):

    rows, columns = len(box), len(box[0])

    # iterate through each row
    for row in range(rows):

        # Place a pointer (elem) at the very end of the row (R->L)
        for elem in range(columns-1, -1, -1):

            # Move the pointer to the left until a rock (#) is found
            if (box[row][elem] == "#"):

                # Create a new pointer (obs) at the newly found rock's position
                obs = elem + 1

                # Move right (L->R) until an obstacle (or another rock) is found
                while (obs < columns and box[row][obs] == "."):
                    obs += 1

                # Cange the original rock's position to empty (".")
                box[row][elem] = "."

                # Mark cell left of the obstacle (obs) as a rock
                box[row][obs-1] = "#"

    # Rotation
    # rotBox = [[None for _ in range(rows)] for _ in range(columns)]
    # curCol = rows - 1
    # for r in range(rows):
    #     for c in range(columns):
    #         rotBox[c][curCol] = box[r][c]
    #     curCol -= 1

    return zip(*box[::-1])


n = 10
res = [0 for _ in range(n)]
print(res)


# def solution(a):

#     a =[4, 0, 1, -2, 3]

#     b = []

#     if len(a) == 1:
#         b = a
#         return b

#     if a == []:
#         return b

#     for i in range(len(a)):

#         print(i)
#         if i == 0:
#             n = a[i] + a[i + 1]

#         elif i == len(a) - 1:
#             n = a[i - 1] + a[i]

#         else:
#             n = a[i - 1] + a[i] + a[i + 1]

#         b.append(n)


#     return b


def solution(numbers):
    # n = [13 ,31, 30]

    t = True
    for i in range(len(numbers) - 1):

        if numbers[i] > numbers[i + 1]:
            print("im here")

            print(numbers[i + 1], numbers[i])
            str_num = str(numbers[i])
            reverse = str_num[::-1]
            int_num = int(reverse)
            numbers[i] = int_num

    for i in range(len(numbers) - 1):
        if numbers[i + 1] <= numbers[i]:
            t = False
            break

    return t


print(solution([13, 31, 30]))

a = "aabaadcb"
b = "asdeqd"

d1 = {}
d2 = {}


for char in a:
    d1[char] = d1.get(char, 0) + 1

for char in b:
    d2[char] = d2.get(char, 0) + 1
s1 = ""
s2 = ""

l1 = []
l2 = []

for item, value in d1.items():
    l1.append((item * value))

for item, value in d2.items():
    l2.append((item * value))


curr = 0
next = 1
right = len(l2) - 1
while next < right:
    if len(l2[curr]) < len(l2[next]):
        l2[curr], l2[next] = l2[next], l2[curr]
    next += 1


print(l1)
print(l2)

# 9. Palindrome Number
# Easy

# Given an integer x, return true if x is palindrome integer.

# An integer is a palindrome when it reads the same backward as forward.


def isPalindrome(x):

    x = str(x)
    reverse = x[::-1]

    if x == reverse:
        return True

    return False


# 13. Roman to Integer
# Easy

# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000


# Example 1:

# Input: s = "III"
# Output: 3
# Explanation: III = 3.


def romanToInt(s):

    vac = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
        'IV': 4,
        'IX': 9,
        'XL': 40,
        'XC': 90,
        'CD': 400,
        'CM': 900,
    }

    result = 0
    i = 0
    while i < len(s):
        print("im here")
        double = vac.get(s[i:i+2])
        single = vac.get(s[i:i+1])
        print(s[i:i+2])
        print(s[i:i+1])
        if double:
            result += double
            i += 2
        elif single:
            result += single
            i += 1
        print(result)

    return result

# 14. Longest Common Prefix
# Easy

# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".


# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"

def longestCommonPrefix(strs):
    # ["flower","flow","flight"]

    if len(strs) == 0:
        return ""

    if len(strs) == 1:
        return strs[0]

    prefix = strs[0]  # flower
    lprefix = len(strs[0])  # 6

    for word in strs[1:]:
        print(word)
        while prefix != word[:lprefix]:
            print(word[:lprefix])
            prefix = prefix[:lprefix - 1]
            lprefix -= 1
            if lprefix == 0:
                return ""
            print("prefix now is ", prefix)

        return prefix


# 20. Valid Parentheses
# Easy

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

#     Open brackets must be closed by the same type of brackets.
#     Open brackets must be closed in the correct order.
#     Every close bracket has a corresponding open bracket of the same type.

def isValid(s):

    # )(

    stack = []
    mapping = {")": "(", "}": "{", "]": "["}

    for char in s:
        if char in mapping:
            top_element_should_be = stack.pop() if stack else "#"
            if mapping[char] != top_element_should_be:
                return False
        else:
            stack.append(char)

    return not stack


# 26. Remove Duplicates from Sorted Array
# easy
def removeDuplicates(nums):

    previous = None
    free_index = 0

    for num in nums:
        # 1
        # 1
        # 2
        if num != previous:
            # yes
            # no
            # yes
            nums[free_index] = num
            # nums[0] = 1
            # pass
            # nums[1] = 2
            free_index += 1
            # free_index = 1
            # pass
            # free_index = 2
        previous = num
        # previous = 1
        # pass
        # previous = 2

    return free_index


# 27. Remove Element
# easy

def removeElement(nums, val):

    # correct_index_num = 0

    # for num in nums:
    #     if num != val:
    #         nums[correct_index_num] = num
    #         correct_index_num +=1

    # return correct_index_num

    fix = 0
    for curr in nums:
        if curr != val:
            nums[fix], curr = curr, nums[fix]
            fix += 1

    return fix

# 35. Search Insert Position
# Easy

# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.


# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2

# Example 2:

# Input: nums = [1,3,5,6], target = 2
# Output: 1

# Example 3:

# Input: nums = [1,3,5,6], target = 7
# Output: 4

def searchInsert(self, nums: List[int], target: int) -> int:

    # d = {}

    # for i in range(len(nums)):
    #     d[nums[i]] = d.get(nums[i], i)

    # if target in d:
    #     return d[target]

    # elif target > nums[-1]:
    #     return (d[nums[-1]] + 1 )

    # for num in nums:
    #     if num > target:
    #         return (d[num])

    if target in nums:
        return nums.index(target)
    else:
        if nums[-1] > target:
            for i in nums:
                if i > target:
                    return nums.index(i)
        else:
            return len(nums)

# 58. Length of Last Word
# Easy

# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal substring consisting of non-space characters only.


# Example 1:

# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.

def lengthOfLastWord(self, s: str) -> int:

    s = s.rstrip()
    new_str = s.split(" ")
    print(new_str)

    return len(new_str[-1])
