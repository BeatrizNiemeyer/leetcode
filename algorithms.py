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

def searchInsert(nums, target):

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


# 66. Plus One
# Easy

# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.


# Example 1:

# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].

# Example 2:

# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# Incrementing by one gives 4321 + 1 = 4322.
# Thus, the result should be [4,3,2,2].

# Example 3:

# Input: digits = [9]
# Output: [1,0]
# Explanation: The array represents the integer 9.
# Incrementing by one gives 9 + 1 = 10.
# Thus, the result should be [1,0].
def plusOne(digits):

    count = 0
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] == 9 and i == len(digits) - 1:
            digits.pop()
            count += 1
        elif digits[i] == 9:
            digits.pop()
            count += 1
        else:
            break

    if count != 0 and len(digits) == 0:
        digits.append(1)
        for i in range(count):
            digits.append(0)
    elif count != 0 and len(digits) > 0:
        digits[-1] = digits[-1] + 1
        for i in range(count):
            digits.append(0)

    else:
        digits[-1] = digits[-1] + 1

    return digits

    # carry = 0

    # for i in range(len(digits)-1, -1, -1):
    #     print(i)
    #     if digits[i] + 1 <= 9:
    #         digits[i] += 1
    #         carry = 0
    #         break
    #     else:
    #         digits[i] = 0
    #         carry = 1
    # else:
    #     print(digits)
    #     if carry == 1:
    #         digits.insert(0, 1)

    # return digits


# 67. Add Binary
# Easy

# Given two binary strings a and b, return their sum as a binary string.


# Example 1:

# Input: a = "11", b = "1"
# Output: "100"

# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"

def addBinary(a, b):
    # c = []
    # d = []

    # for num in a:
    #     c.append(int(num))

    # for num in b:
    #     d.append(int(num))

    # dif = abs(len(c) - len(d))

    # output = []

    # for i in range(dif):
    #     if len(c) < len(d):
    #         c.insert(0, 0)
    #     elif len(d) < len(c):
    #         d.insert(0, 0)

    # carry = 0

    # for i in range(len(c) - 1, -1, -1):
    #     if carry == 1 and c[i] == 1 and d[i] == 1:
    #         output.append(1)
    #         carry = 1
    #     elif carry == 0 and c[i] == 1 and d[i] == 1:
    #         output.append(0)
    #         carry = 1
    #     elif carry == 1 and (c[i] == 1 or d[i] == 1):
    #         output.append(0)
    #         carry = 1
    #     elif carry == 1 and (c[i] == 0 or d[i] == 0):
    #         output.append(1)
    #         carry = 0
    #     else:
    #         r = c[i] + d[i]
    #         output.append(r)
    #         carry = 0

    # output = output[::-1]

    # if carry == 1:
    #     output.insert(0, 1)

    # result = ""
    # for item in output:
    #     result += str(item)

    return result

    a = list(a)
    b = list(b)
    carry = 0
    result = ""

    while a or b or carry:
        if a:
            carry += int(a.pop())
        if b:
            carry += int(b.pop())

        result += str(carry % 2)
        carry = carry // 2

    return result[::-1]


# 69. Sqrt(x)
# Easy

# Given a non-negative integer x, compute and return the square root of x.

# Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

# Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.


# Example 1:

# Input: x = 4
# Output: 2

# Example 2:

# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.


def mySqrt(x):

    l = []

    if x == 0:
        return 0

    if x == 1:
        return 1

    for i in range(x + 1):
        if (i * i) == x:
            return i
        if (i * i) > x:
            l.append(i - 1)
            break

    return (l.pop())


# 70. Climbing Stairs
# Easy

# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?


# Example 1:

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps


def climbStairs(n):

    one, two = 1, 1

    0, 1, 2, 3, 4, 5

    for i in range(n - 1):
        temp = one
        one = two + one
        two = temp

    return one


# 136. Single Number
# Easy

# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.


# Example 1:

# Input: nums = [2,2,1]
# Output: 1


def singleNumber(nums):

    d = {}

    for num in nums:
        d[num] = d.get(num, 0) + 1

    for item, value in d.items():
        if value == 1:
            return item

    #  a= 2 * sum(set(nums)) - sum(nums)
    #    return a


# You are given a string s. Consider the following algorithm applied to this string:

#     Take all the prefixes of the string, and choose the longest palindrome between them.
#     If this chosen prefix contains at least two characters, cut this prefix from s and go back to the first step with the updated string. Otherwise, end the algorithm with the current string s as a result.

# Your task is to implement the above algorithm and return its result when applied to string s.

# Note: you can click on the prefixes and palindrome words to see the definition of the terms if you're not familiar with them.

# Example

#     For s = "aaacodedoc", the output should be solution(s) = "".
#         The initial string s = "aaacodedoc" contains only three prefixes which are also palindromes - "a", "aa", "aaa". The longest one between them is "aaa", so we cut if from s.
#         Now we have string "codedoc". It contains two prefixes which are also palindromes - "c" and "codedoc". The longest one between them is "codedoc", so we cut if from the current string and obtain the empty string.
#         Finally the algorithm ends on the empty string, so the answer is "".

#     For s = "codesignal", the output should be solution(s) = "codesignal".
#     The initial string s = "codesignal" contains the only prefix, which is also palindrome - "c". This prefix is the longest, but doesn't contain two characters, so the algorithm ends with string "codesignal" as a result.

#     For s = "", the output should be solution(s) = "".


#    if len(s) == 1:
#         return s

#     if len(s) == 0:
#         return ""

#     max_l = 0
#     lst_prefix = []
#     prefix =[]
#     for i in range(len(s) - 1):
#         l_prefix =  ""
#         for j in range(i, len(s)):
#             l_prefix += s[j]
#             if l_prefix == l_prefix[::-1] and len(l_prefix) > 1:
#                 lenght = len(l_prefix)

#                 lst_prefix.append(l_prefix)
#                 s.replace(l_prefix, "")


#     print(lst_prefix)
#     print(s)

# 169. Majority Element
# Easy

# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

def majorityElement(nums):

    d = {}

    for i in range(len(nums)):
        d[nums[i]] = d.get(nums[i], 0) + 1

    marjority = 0
    for value in d.values():
        marjority = max(value, marjority)

    for item, value in d.items():
        if value == marjority:
            return item

    # count = 0

    # for num in set(nums):
    #     counting = nums.count(num)
    #     print(counting)
    #     if counting > count:
    #         result = num
    #         count = counting

    # return result

        # d = {}
        # count = 0

        # for i in range(len(nums)):
        #     d[nums[i]] = d.get(nums[i], 0) + 1
        #     if d[nums[i]] > count:
        #         count = d[nums[i]]
        #         key = nums[i]

        # return key

# 704. Binary Search
# Easy

# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.

# Example 1:

# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4


def search(nums, target):

    if target in nums:
        return nums.index(target)
    else:
        return -1


# 409. Longest Palindrome
# Easy

# Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

# Letters are case sensitive, for example, "Aa" is not considered a palindrome here.


# Example 1:

# Input: s = "abccccdd"
# Output: 7
# Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

def longestPalindrome(s):

    result = 0
    d = {}
    add_1_to_dict = True
    l = []

    for char in s:
        d[char] = d.get(char, 0) + 1

    for item in d:
        if d[item] % 2 == 0:
            result += d[item]
        if d[item] % 2 == 1:
            result += (d[item] - 1)
            add_1_to_dict = False

    if add_1_to_dict == False:
        result += 1

    return result

# 1561. Maximum Number of Coins You Can Get
# Medium

# There are 3n piles of coins of varying size, you and your friends will take piles of coins as follows:

#     In each step, you will choose any 3 piles of coins (not necessarily consecutive).
#     Of your choice, Alice will pick the pile with the maximum number of coins.
#     You will pick the next pile with the maximum number of coins.
#     Your friend Bob will pick the last pile.
#     Repeat until there are no more piles of coins.

# Given an array of integers piles where piles[i] is the number of coins in the ith pile.

# Return the maximum number of coins that you can have.


# Example 1:

# Input: piles = [2,4,1,2,7,8]
# Output: 9
# Explanation: Choose the triplet (2, 7, 8), Alice Pick the pile with 8 coins, you the pile with 7 coins and Bob the last one.
# Choose the triplet (1, 2, 4), Alice Pick the pile with 4 coins, you the pile with 2 coins and Bob the last one.
# The maximum number of coins which you can have are: 7 + 2 = 9.
# On the other hand if we choose this arrangement (1, 2, 8), (2, 4, 7) you only get 2 + 4 = 6 coins which is not optimal.


def maxCoins(piles):

    number_of_triplets = len(piles) // 3
    result = 0
    piles = sorted(piles, reverse=True)

    j = 1
    for i in range(number_of_triplets):
        result += piles[j]
        j += 2

    return result

# 1472. Design Browser History
# Medium

# You have a browser of one tab where you start on the homepage and you can visit another url, get back in the history number of steps or move forward in the history number of steps.

# Implement the BrowserHistory class:

#     BrowserHistory(string homepage) Initializes the object with the homepage of the browser.
#     void visit(string url) Visits url from the current page. It clears up all the forward history.
#     string back(int steps) Move steps back in history. If you can only return x steps in the history and steps > x, you will return only x steps. Return the current url after moving back in history at most steps.
#     string forward(int steps) Move steps forward in history. If you can only forward x steps in the history and steps > x, you will forward only x steps. Return the current url after forwarding in history at most steps.


class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.cur = 0

    def visit(self, url: str) -> None:
        self.cur += 1
        self.history = self.history[:self.cur]
        self.history.append(url)

    def back(self, steps: int) -> str:

        self.cur = max(0, (self.cur - steps))

        return self.history[self.cur]

    def forward(self, steps: int) -> str:
        self.cur = min(len(self.history) - 1, self.cur + steps)

        return self.history[self.cur]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)


# You are given two strings - pattern and source. The first string pattern contains only the symbols 0 and 1, and the second string source contains only lowercase English letters.

# Let's say that pattern matches a substring source[l..r] of source if the following three conditions are met:

#     they have equal length,
#     for each 0 in pattern the corresponding letter in the substring is a vowel,
#     for each 1 in pattern the corresponding letter is a consonant.


# pattern = "2"
# source = "0101011"


# difference = (len(source) - len(pattern))
# i = 0
# count = 0

# while i <= difference:
#     if pattern == source[i: len(pattern) + i]:
#         count += 1
#     i += 1

# print(count)

# s = "oitudobem"
# print(s.join(reversed(s)))


# 290. Word Pattern
# Easy

# Given a pattern and a string s, find if s follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.


# Example 1:

# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true

def wordPattern(pattern, s):

    s = s.split(" ")
    set_pattern = set(pattern)
    set_s = set(s)

    if len(set_pattern) != len(set(set_s)):
        return False

    if len(pattern) != len(s):
        return False

    d = {}
    for i in range(len(s)):
        if s[i] not in d:
            d[s[i]] = pattern[i]

    print(d)

    for i in range(len(s)):
        if pattern[i] != d[s[i]]:
            return False

    return True


# You are given an array of arrays a. Your task is to group the arrays a[i] by their mean values, so that arrays with equal mean values are in the same group, and arrays with different mean values are in different groups.

# Each group should contain a set of indices (i, j, etc), such that the corresponding arrays (a[i], a[j], etc) all have the same mean. Return the set of groups as an array of arrays, where the indices within each group are sorted in ascending order, and the groups are sorted in ascending order of their minimum element.

# Example

#     For

#     a = [[3, 3, 4, 2],
#          [4, 4],
#          [4, 0, 3, 3],
#          [2, 3],
#          [3, 3, 3]]

#     the output should be

#     solution(a) = [[0, 4],
#                      [1],
#                      [2, 3]]

#         mean(a[0]) = (3 + 3 + 4 + 2) / 4 = 3;
#         mean(a[1]) = (4 + 4) / 2 = 4;
#         mean(a[2]) = (4 + 0 + 3 + 3) / 4 = 2.5;
#         mean(a[3]) = (2 + 3) / 2 = 2.5;
#         mean(a[4]) = (3 + 3 + 3) / 3 = 3.


# 5. Longest Palindromic Substring
# Medium

# Given a string s, return the longest palindromic substring in s.

# A string is called a palindrome string if the reverse of that string is the same as the original string.


# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

# Example 2:

# Input: s = "cbbd"
# Output: "bb"

def longestPalindrome(s):

    res = ""
    len_res = 0

    for i in range(len(s)):
        l, r = i, i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if r - l + 1 > len_res:
                res = s[l: r + 1]
                len_res = (r - l + 1)

            l -= 1
            r += 1

        l, r = i, i + 1

        while l >= 0 and r < len(s) and s[l] == s[r]:

            if r - l + 1 > len_res:
                res = s[l: r + 1]
                len_res = (r - l + 1)

            l -= 1
            r += 1

    return res


# 3. Longest Substring Without Repeating Characters
# Medium

# Given a string s, find the length of the longest substring without repeating characters.


# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

def lengthOfLongestSubstring(s):
    seen_char = ""
    l_count = 0

    for char in s:
        if char in seen_char:
            find_index = seen_char.find(char)
            seen_char = seen_char[find_index + 1:]
        seen_char += char
        if len(seen_char) > l_count:
            l_count = len(seen_char)

    return l_count

# 322. Coin Change
# Medium

# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

# You may assume that you have an infinite number of each kind of coin.


# Example 1:

# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1

def coinChange(coins, amount):

    dp = [(amount + 1)] * (amount + 1)
    dp[0] = 0

    for a in range(amount + 1):
        for c in coins:
            if a - c >= 0:
                dp[a] = min(dp[a], 1 + dp[a-c])

    return dp[amount] if dp[amount] != amount + 1 else -1


# 300. Longest Increasing Subsequence
# Medium

# Given an integer array nums, return the length of the longest strictly increasing subsequence.

# A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].


# Example 1:

# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.


def lengthOfLIS(nums):

    dp = [1] * len(nums)

    for i in range(len(nums) - 1, -1, -1):
        for j in range(i + 1, len(nums)):
            if nums[i] < nums[j]:
                dp[i] = max(dp[i], 1 + dp[j])

    return max(dp)

# 139. Word Break
# Medium

# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

# Note that the same word in the dictionary may be reused multiple times in the segmentation.


# Example 1:

# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".

def wordBreak(s, wordDict):

    dp = [False] * (len(s) + 1)
    dp[len(s)] = True

    for i in range(len(s) - 1, -1, - 1):

        for w in wordDict:
            print(s[i: i + len(w)], w)
            if (i + len(w)) <= len(s) and s[i: i + len(w)] == w:
                dp[i] = dp[i + len(w)]
            if dp[i]:
                break

    return dp[0]


# You are given an array of strings arr. Your task is to construct a string from the words in arr, starting with the 0th character from each word (in the order they appear in arr), followed by the 1st character, then the 2nd character, etc. If one of the words doesn't have an ith character, skip that word.

# Return the resulting string.

# Example

#     For arr = ["Daisy", "Rose", "Hyacinth", "Poppy"], the output should be solution(arr) = "DRHPaoyoisapsecpyiynth".
#         First, we append all 0th characters and obtain string "DRHP";
#         Then we append all 1st characters and obtain string "DRHPaoyo";
#         Then we append all 2nd characters and obtain string "DRHPaoyoisap";
#         Then we append all 3rd characters and obtain string "DRHPaoyoisapsecp";
#         Then we append all 4th characters and obtain string "DRHPaoyoisapsecpyiy";
#         Finally, only letters in the arr[2] are left, so we append the rest characters and get "DRHPaoyoisapsecpyiynth";


# 4. Median of Two Sorted Arrays
# Hard

# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.

def findMedianSortedArrays(nums1, nums2):

    all_nums = sorted(nums1 + nums2)
    length = len(all_nums)

    print(all_nums)
    if length % 2 == 0:
        return ((all_nums[(length//2)-1+(length//2)+1]))/2
    else:
        return all_nums[(len(all_nums)//2)]


# 151. Reverse Words in a String
# Medium

# Given an input string s, reverse the order of the words.

# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

# Return a string of the words in reverse order concatenated by a single space.

# Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.


# Example 1:

# Input: s = "the sky is blue"
# Output: "blue is sky the"


def reverseWords(s):

    l = s.split(" ")

    print(l)
    s2 = ""

    for i in range(len(l) - 1, -1, -1):
        if l[i] != "":
            s2 += l[i] + " "

    return s2.strip()

# 56. Merge Intervals
# Medium

# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

# Example 1:

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].


def merge(intervals):

    intervals.sort(key=lambda i: i[0])
    output = [intervals[0]]

    for item in intervals[1:]:
        start, end = item
        last_end = output[-1][1]
        if start <= last_end:
            output[-1][1] = max(last_end, end)
        else:
            output.append([start, end])

    return output


# 17. Letter Combinations of a Phone Number
# Medium

# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


# Example 1:

# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

def letterCombinations(digits):

    d = {"2": "abc",
         "3": "def",
         "4": "ghi",
         "5": "jkl",
         "6": "mno",
         "7": "pqrs",
         "8": "tuv",
         "9": "wxyz"
         }

    if len(digits) == 0:
        return []
    if len(digits) == 1:
        return list(d[digits[0]])

    l = list(d[digits[0]])  # a , b , c

    for digit in digits[1:]:  # 3
        l = [(old + new) for old in l for new in list(d[digit])]

    return l


# 75. Sort Colors
# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# You must solve this problem without using the library's sort function.

# Example 1:

# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
def sortColors(nums):
    """
    Do not return anything, modify nums in-place instead.
    """

    for i in range(len(nums)-1, -1, -1):
        for j in range(len(nums) - 1, -1, -1):
            if nums[i] >= nums[j] and i != j:
                nums[i], nums[j] = nums[j], nums[i]

    return nums

# 49. Group Anagrams

# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]

def groupAnagrams(strs):

    d = defaultdict(list)

    for s in strs:
        d["".join(sorted(s))].append(s)

    return d.values()

# 706. Design HashMap

# Design a HashMap without using any built-in hash table libraries.

# Implement the MyHashMap class:

#     MyHashMap() initializes the object with an empty map.
#     void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
#     int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
#     void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.


class MyHashMap:

    def __init__(self):
        self.d = {}

    def put(self, key: int, value: int) -> None:
        self.d[key] = value

    def get(self, key: int) -> int:
        if key in self.d:
            return self.d[key]
        else:
            return -1

    def remove(self, key: int) -> None:
        if key in self.d:
            del self.d[key]


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)


# 1356. Sort Integers by The Number of 1 Bits

# You are given an integer array arr. Sort the integers in the array in ascending order by the number of 1's in their binary representation and in case of two or more integers have the same number of 1's you have to sort them in ascending order.

# Return the array after sorting it.

def sortByBits(arr):

    d = defaultdict(list)
    l = []
    for num in arr:
        a = bin(num)
        binary = a[2:]
        d[binary.count("1")].append(num)
        l.append(binary.count("1"))

    res = []
    l.sort()
    for num in set(l):
        d[num].sort()
        for item in d[num]:
            res.append(item)

    return res


# 347. Top K Frequent Elements

# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

def topKFrequent(nums):

    d = {}

    for num in nums:
        d[num] = d.get(num, 0) + 1

    values = []

    for value in d.values():
        values.append(value)

    values.sort(reverse=True)

    values = values[:k]

    res = set()
    for item, value in d.items():
        for v in values:
            if value == v:
                res.add(item)

    return list(res)

# 22. Generate Parentheses
# Medium

# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.


def generateParenthesis(n):

    stack = []
    res = []

    def checking_par(opening, closing):
        if opening == closing == n:
            res.append("".join(stack))
            return

        if opening < n:
            stack.append("(")
            checking_par(opening + 1, closing)
            stack.pop()

        if closing < opening:
            stack.append(")")
            checking_par(opening, closing + 1)
            stack.pop()

    checking_par(0, 0)
    return res


# 167. Two Sum II - Input Array Is Sorted
# Medium

# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

# The tests are generated such that there is exactly one solution. You may not use the same element twice.

# Your solution must use only constant extra space.


# Example 1:

# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].


def twoSum(numbers, target):

    d = {}

    for i, n in enumerate(numbers):
        if (target - (n)) in d:
            return([d[target - n], i + 1])
        else:
            d[n] = d.get(n, i)


# 7. Reverse Integer
# Medium

# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

# Example 1:

# Input: x = 123
# Output: 321


def reverse(x):

    if x == 0:
        return x

    s = str(x)[::-1]

    if s[-1] == "-":
        s = "-" + s[:-1]

    for char in s:
        if char == "0":
            s = s.replace(char, "", 1)
        if char != "0":
            break

    if abs(int(s)) > (2**31):
        return 0

    return int(s)


# 125. Valid Palindrome
# Easy

# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.


def isPalindrome(s):

    if s == " ":
        return True

    res = ""

    for char in s:
        if char.isalnum():
            res += char.lower()

    if res == res[::-1]:
        return True


# 202. Happy Number
# Easy

# Write an algorithm to determine if a number n is happy.

# A happy number is a number defined by the following process:

#     Starting with any positive integer, replace the number by the sum of the squares of its digits.
#     Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
#     Those numbers for which this process ends in 1 are happy.

# Return true if n is a happy number, and false if not.

def isHappy(self, n: int) -> bool:

    s = set()

    while n != 1:
        summ = 0
        for num in str(n):
            summ += int(num) ** 2
        if summ in s:
            return False
        else:
            s.add(summ)
            n = summ

    return True

# 18. 4Sum
# Medium
# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

#     0 <= a, b, c, d < n
#     a, b, c, and d are distinct.
#     nums[a] + nums[b] + nums[c] + nums[d] == target


def fourSum(nums, target):
    nums.sort()

    res = []
    for i in range(len(nums)-3):
        cur1 = nums[i]
        for j in range(i + 1, len(nums)-2):
            cur2 = nums[j]
            l, r = j + 1, len(nums) - 1
            while l < r:
                summ = cur1 + cur2 + nums[l] + nums[r]
                # print(summ)
                if summ > target:
                    r -= 1
                elif summ < target:
                    l += 1
                elif summ == target:
                    if [cur1, cur2, nums[l], nums[r]] not in res:
                        res.append([cur1, cur2, nums[l], nums[r]])
                    l += 1
                    r -= 1

    return res

# 29. Divide Two Integers
# Medium

# Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

# The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

# Return the quotient after dividing dividend by divisor.

# Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231.


# Example 1:

# Input: dividend = 10, divisor = 3
# Output: 3
# Explanation: 10/3 = 3.33333.. which is truncated to 3.

def divide(dividend, divisor):

    res = abs(dividend) // abs(divisor)

    if str(dividend)[0] == "-" and str(divisor)[0] != "-":
        res = "-" + str(res)
        res = int(res)
    elif str(dividend)[0] != "-" and str(divisor)[0] == "-":
        res = "-" + str(res)
        res = int(res)

    if res > (2 ** 31) - 1:
        return (2 ** 31) - 1
    elif res < (-2 ** 31) - 1:
        return (-2 ** 31) - 1

    return res

# 33. Search in Rotated Sorted Array
# Medium

# There is an integer array nums sorted in ascending order (with distinct values).

# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity.


# Example 1:

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4

def search(nums, target):

    if target in nums:
        return nums.index(target)
    else:
        return -1


# 34. Find First and Last Position of Element in Sorted Array
# Medium

# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.


# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]


def searchRange(nums, target):

    res = []

    d = defaultdict(list)

    for i, num in enumerate(nums):
        d[num].append(i)

    for item in d:
        if item == target:
            res = d[item]

    if not res:
        return [-1, -1]

    return [res[0], res[-1]]

# 217. Contains Duplicate
# Easy

# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example 1:

# Input: nums = [1,2,3,1]
# Output: true


def containsDuplicate(nums):

    # d = {}

    # for num in nums:
    #     d[num] = d.get(num, 0 ) + 1

    # for value in d.values():

    #     if value > 1:
    #         return True

    # return False

    set_nums = set(nums)

    if len(set_nums) < len(nums):
        return True

    return False


# 205. Isomorphic Strings
# Easy

# Given two strings s and t, determine if they are isomorphic.

# Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.


# Example 1:

# Input: s = "egg", t = "add"
# Output: true

def isIsomorphic(s, t):

    d1 = {}
    d2 = {}
    for i in range(len(s)):
        if s[i] not in d1:
            d1[s[i]] = t[i]
            d2[t[i]] = s[i]

    s2 = ""
    for char in t:
        if char not in d2:
            return False
        else:
            s2 += d2[char]

    if s2 == s:
        return True
    else:
        return False

# 12. Integer to Roman
# Medium


# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

#     I can be placed before V (5) and X (10) to make 4 and 9.
#     X can be placed before L (50) and C (100) to make 40 and 90.
#     C can be placed before D (500) and M (1000) to make 400 and 900.


def intToRoman(num):

    number = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    values = ['I', 'IV', 'V', 'IX', 'X', 'XL',
              'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
    roman_value = ""
    i = 12
    while num != 0:
        print(number[i])
        if number[i] <= num:
            num = num - number[i]
            roman_value += values[i]
        else:
            i = i-1
        print(num)
    return roman_value


# 243. Shortest Word Distance

# Given an array of strings wordsDict and two different strings that already exist in the array word1 and word2, return the shortest distance between these two words in the list.

# Example 1:

# Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "coding", word2 = "practice"
# Output: 3


def shortestDistance(words):

    shortestDistance = len(words)
    position1, position2 = -1, -1
    for i in range(len(words)):
        if words[i] == word1:
            position1 = i
        elif words[i] == word2:
            position2 = i

        if position1 != -1 and position2 != -1:
            shortestDistance = min(
                shortestDistance, abs(position1 - position2))

    return shortestDistance

    w1 = []
    w2 = []
    res = 400000

    for i, w in enumerate(words):
        if w == word1:
            w1.append(i)
        elif w == word2:
            w2.append(i)

    for i in range(len(w1)):
        for j in range(len(w2)):
            subt = abs(w1[i] - w2[j])
            if subt < res:
                res = subt
    return res

# 39. Combination Sum
# Medium


# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

# The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.


# Example 1:

# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.

def combinationSum(candidates, target):

    res = []

    def backtracking(remaining, comb, start):

        if remaining == 0:
            res.append(comb.copy())
            return

        elif remaining < 0:
            return

        for i in range(start, len(candidates)):
            # print(comb)
            comb.append(candidates[i])

            backtracking((remaining - candidates[i]), comb, i)

            comb.pop()

    backtracking(target, [], 0)

    return res

    results = []


# 46. Permutations
# Medium

# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

# Example 1:

# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

def permute(nums):

    res = []

    if len(nums) == 1:
        return [nums.copy()]

    for i in range(len(nums)):
        n = nums.pop(0)
        perms = self.permute(nums)

        for perm in perms:
            perm.append(n)

        res.extend(perms)
        nums.append(n)

    return res


# 47. Permutations II
# Medium

# Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

# Example 1:

# Input: nums = [1,1,2]
# Output:
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]


def permuteUnique(nums):

    # res = []

    # if len(nums) == 1:
    #     return [nums.copy()]

    # for i in range(len(nums)):
    #     n = nums.pop(0)
    #     perms = self.permuteUnique(nums)

    #     for perm in perms:
    #         perm.append(n)

    #     res.extend(perms)
    #     nums.append(n)

    # return [list(item) for item in set(tuple(row) for row in res)]

    res = []
    perm = []

    d = {n: 0 for n in nums}
    for n in nums:
        d[n] += 1

    def dfs():

        if len(perm) == len(nums):
            res.append(perm.copy())
            return

        for item in d:
            if d[item] > 0:
                perm.append(item)
                d[item] -= 1

                dfs()
                d[item] += 1
                perm.pop()

    dfs()

    return res


# 28. Find the Index of the First Occurrence in a String
# Medium

# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# Example 1:

# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.

def strStr(haystack, needle):

    return haystack.find(needle)


# 43. Multiply Strings
# Medium

# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.


# Example 1:

# Input: num1 = "2", num2 = "3"
# Output: "6"


def multiply(self, num1: str, num2: str) -> str:

    return str(int(num1) * int(num2))

# 415. Add Strings
# Easy

# Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

# You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

# Example 1:

# Input: num1 = "11", num2 = "123"
# Output: "134"


def addStrings(num1, num2):

    d = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5,
         "6": 6, "7": 7, "8": 8, "9": 9, "0": 0}

    num1 = num1[::-1]
    num2 = num2[::-1]

    dif_len = max(len(num1), len(num2)) - min(len(num1), len(num2))

    if len(num1) < len(num2):
        for i in range(dif_len):
            num1 += "0"
    elif len(num1) > len(num2):
        for i in range(dif_len):
            num2 += "0"

    s = ""
    sobra = 0
    for i in range(len(num1)):
        res = d[num1[i]] + d[num2[i]] + sobra
        if res > 9:
            sobra = 1
            s += str(res)[-1]
        if res <= 9:
            s += str(res)
            sobra = 0

    if sobra > 0:
        s = s + "1"

    return s[::-1]


# 189. Rotate Array
# Medium

# Given an array, rotate the array to the right by k steps, where k is non-negative.


# Example 1:

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]

def rotate(nums, k):
    """Do not return anything, modify nums in-place instead.
    """

    # for i in range(k):
    #     n = nums.pop()
    #     nums.insert(0, n)

    k = k % len(nums)
    n = len(nums) - k
    nums[:] = nums[n:] + nums[:n]


# 215. Kth Largest Element in an Array
# Medium


# Example 1:

# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5

def findKthLargest(nums, k):

    nums.sort()

    return nums[-k]


# 78. Subsets
# Medium

# Given an integer array nums of unique elements, return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.


# Example 1:

# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

# Example 2:

# Input: nums = [0]
# Output: [[],[0]]

def subsets(nums):

    res = []
    substring = []

    def dfs(i):
        if i >= len(nums):
            res.append(substring.copy())
            return

        substring.append(nums[i])
        dfs(i + 1)

        substring.pop()
        dfs(i + 1)

    dfs(0)
    return res


# 128. Longest Consecutive Sequence
# Medium

# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.


# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

def longestConsecutive(nums):
    nums = set(nums)
    nums = list(nums)
    nums.sort()
    count = 0
    res = []

    l, r = 0, 1

    if not nums:
        return 0

    if len(nums) == 1:
        return 1

    for i in range(len(nums) - 1):
        if r < len(nums) and nums[r] == nums[l] + 1:
            count += 1
            l += 1
            r += 1
        else:
            count = 0
            l += 1
            r += 1
        res.append(count + 1)
    return max(res)


# 119. Pascal's Triangle II
# Easy

# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

# Example 1:

# Input: rowIndex = 3
# Output: [1,3,3,1]

def getRow(rowIndex):

    l = [[1], [1, 1]]
    count = 0

    while count <= rowIndex:
        l2 = []
        for i in range(len(l[-1])-1):
            l2.append(l[-1][i] + l[-1][i + 1])
        l2 = [1] + l2 + [1]
        l.append(l2)
        count += 1

    return l[rowIndex]

# 118. Pascal's Triangle
# Easy

# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

# Example 1:

# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]


def generate(numRows):

    l = [[1], [1, 1]]
    count = 0

    while count < numRows - 2:
        l2 = []
        for i in range(len(l[-1])-1):
            l2.append(l[-1][i] + l[-1][i + 1])
        l2 = [1] + l2 + [1]
        l.append(l2)
        count += 1

    return l[:numRows]


# 219. Contains Duplicate II
# Easy

# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

# Example 1:

# Input: nums = [1,2,3,1], k = 3
# Output: true

def containsNearbyDuplicate(nums, k):

    d = {}

    for i, num in enumerate(nums):
        if num in d:
            subt = abs(d[num] - i)
            if subt <= k:
                return True
            else:
                d[num] = i
        else:
            d[num] = i

    return False


# 228. Summary Ranges
# Easy
# You are given a sorted unique integer array nums.

# A range [a,b] is the set of all integers from a to b (inclusive).

# Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

# Each range [a,b] in the list should be output as:

#     "a->b" if a != b
#     "a" if a == b

# Example 1:

# Input: nums = [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
# Explanation: The ranges are:
# [0,2] --> "0->2"
# [4,5] --> "4->5"
# [7,7] --> "7"

def summaryRanges(nums):

    l = []
    res = []

    for i in range(len(nums)):
        l.append(nums[i])
        if nums[i] + 1 not in nums:
            if len(l) > 1:
                res.append(f"{l[0]}->{l[-1]}")
                l = []
            else:
                res.append(f"{l[0]}")
                l = []

    return res

# 414. Third Maximum Number
# Easy
# Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

# Example 1:

# Input: nums = [3,2,1]
# Output: 1
# Explanation:
# The first distinct maximum is 3.
# The second distinct maximum is 2.
# The third distinct maximum is 1.


def thirdMax(nums):
    nums = set(nums)
    nums = list(nums)
    nums = sorted(nums, reverse=True)

    if len(nums) >= 3:
        return nums[2]
    else:
        return nums[0]


# 242. Valid Anagram
# Easy

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true

def isAnagram(s, t):

    # if len(s) != len(t):
    #     return False

    # ds, dt = {}, {}

    # for i in range(len(s)):
    #     ds[s[i]]= ds.get(s[i], 0 ) + 1
    #     dt[t[i]]= dt.get(t[i], 0 ) + 1

    # for c in ds:
    #     if ds[c]!= dt.get(c, 0 ):
    #         return False

    # return True
    # return Counter(s) == Counter(t)

    if sorted(s) == sorted(t):
        return True

# 53. Maximum Subarray
# Medium

# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# A subarray is a contiguous part of an array.

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.


def maxSubArray(nums):

    res = nums[0]
    summ = 0

    for num in nums:
        if summ < 0:
            summ = 0
        summ += num
        res = max(res, summ)

    return res


# 167. Two Sum II - Input Array Is Sorted
# Medium

# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

# The tests are generated such that there is exactly one solution. You may not use the same element twice.

# Your solution must use only constant extra space.

def twoSum(nums, target):

    # d = {}

    # for i, n in enumerate(numbers):
    #     if (target - (n)) in d:
    #         return([d[target - n], i + 1])
    #     else:
    #         d[n] = d.get(n, i +1)

    # [1, 2, 3, 4, 5, 78, 90]  target = 10

    l = 0
    r = len(nums) - 1

    for num in nums:
        summ = nums[l] + nums[r]
        if summ < target:
            l += 1
        elif summ > target:
            r -= 1
        elif summ == target:
            return [l+1, r+1]

# 198. House Robber
# Medium

# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

# Example 1:

# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.


def rob(nums):

    # rob1, rob2 = 0, 0

    # for num in nums:
    #     temp = max(num + rob1, rob2)
    #     rob1 = rob2
    #     rob2 = temp
    # return rob2

    prev = 0
    curr = 0
    for x in nums:
        temp = prev
        prev = curr
        curr = max(x+temp, prev)
    return curr


# 1299. Replace Elements with Greatest Element on Right Side
# Easy

# Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

# After doing so, return the array.

# Example 1:

# Input: arr = [17,18,5,4,6,1]
# Output: [18,6,6,6,1,-1]


def replaceElements(arr):

    # for i in range(len(arr)):
    #     if i == len(arr) - 1:
    #         arr[i] = -1
    #     else:
    #         arr[i] = max(arr[i+1:])

    # return arr

    right_max = -1

    for i in range(len(arr)-1, -1, -1):
        new_max = max(right_max, arr[i])
        arr[i] = right_max
        right_max = new_max

    return arr


# 367. Valid Perfect Square
# Easy

# Given a positive integer num, write a function which returns True if num is a perfect square else False.

# Follow up: Do not use any built-in library function such as sqrt.

# Example 1:

# Input: num = 16
# Output: true


def isPerfectSquare(num):

    l, r = 0, num
    half_way = num // 2

    if num == 1:
        return True
    while l < num:
        res = half_way * half_way
        # print(res)
        if res > num:
            half_way = half_way // 2
        elif res == num:
            return True
        else:
            half_way += 1

        l += half_way

# 344. Reverse String
# Easy

# Write a function that reverses a string. The input string is given as an array of characters s.

# You must do this by modifying the input array in-place with O(1) extra memory.

# Example 1:

# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]


def reverseString(s):
    """
    Do not return anything, modify s in-place instead.
    """

    # for i in range(len(s)//2):
    #     s[i], s[-i - 1] = s[-i - 1], s[i]

    # return s

    # s[:] = s[::-1]

    # return s

    # j = []
    # for i in range(len(s)-1, -1, -1):
    #     j.append(s[i])

    # s[:] = j

    l, r = 0, len(s) - 1

    while l < (r):
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1


# 383. Ransom Note
# Easy

# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

# Example 1:

# Input: ransomNote = "a", magazine = "b"
# Output: false

def canConstruct(ransomNote, magazine):

    # d = dict(Counter(magazine))

    # for char in ransomNote:
    #     print(d)
    #     print(char)
    #     if char in d and d[char] > 0:
    #         d[char] = d[char] - 1

    #     elif char not in d or d[char] == 0:
    #         return False

    # return True

    # ransomNote = list(ransomNote)
    # magazine = list(magazine)

    # for char in ransomNote:
    #     if char in magazine:
    #         magazine.remove(char)
    #     else:
    #         return False

    # return True

    for char in ransomNote:
        if char in magazine:
            magazine = magazine.replace(char, " ", 1)
        else:
            return False
    return True

# 922. Sort Array By Parity II
# Easy

# Given an array of integers nums, half of the integers in nums are odd, and the other half are even.

# Sort the array so that whenever nums[i] is odd, i is odd, and whenever nums[i] is even, i is even.

# Return any answer array that satisfies this condition.

# Example 1:

# Input: nums = [4,2,5,7]
# Output: [4,5,2,7]
# Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.


def sortArrayByParityII(nums):

    l1 = []
    l2 = []

    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            l1.append(nums[i])
        else:
            l2.append(nums[i])

    for i in range(len(nums)):
        if i % 2 == 0:
            nums[i] = l1.pop()
        else:
            nums[i] = l2.pop()

    return nums


# 977. Squares of a Sorted Array
# Easy

# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

# Example 1:

# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].


def sortedSquares(nums):

    list_of_squares = []

    for num in nums:
        list_of_squares.append(num ** 2)

    list_of_squares.sort()

    return list_of_squares


# 1228. Missing Number In Arithmetic Progression
# Easy


# In some array arr, the values were in arithmetic progression: the values arr[i + 1] - arr[i] are all equal for every 0 <= i < arr.length - 1.

# A value from arr was removed that was not the first or last value in the array.

# Given arr, return the removed value.

# Example 1:

# Input: arr = [5,7,11,13]
# Output: 9
# Explanation: The previous array was [5,7,9,11,13].

def missingNumber(arr):

    arr = sorted(arr, reverse=True)
    l, r = 0, 1
    max_dif = min((arr[0] - arr[1]), (arr[-2] - arr[-1]))

    while r < len(arr) - 1:
        dif = arr[l] - arr[r]
        max_dif = min(max_dif, dif)
        r += 1
        l += 1

    for i in range(len(arr) - 1):
        if arr[i] - arr[i + 1] > max_dif:
            return arr[i] - max_dif

    return arr[0]

# 1342. Number of Steps to Reduce a Number to Zero
# Easy

# Given an integer num, return the number of steps to reduce it to zero.

# In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it

# Example 1:

# Input: num = 14
# Output: 6


def numberOfSteps(num):
    count = 0

    while num != 0:
        if num % 2 == 0:
            num = num // 2
        else:
            num = num - 1

        count += 1

    return count


# 1480. Running Sum of 1d Array
# Easy

# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

# Return the running sum of nums.

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

def runningSum(nums):

    lst = [nums[0]]
    r = 1

    while r < len(nums):
        lst.append(lst[-1] + nums[r])
        r += 1

    return lst

# 1672. Richest Customer Wealth
# Easy

# You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.

# A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.

# Example 1:

# Input: accounts = [[1,2,3],[3,2,1]]
# Output: 6
# Explanation:
# 1st customer has wealth = 1 + 2 + 3 = 6
# 2nd customer has wealth = 3 + 2 + 1 = 6
# Both customers are considered the richest with a wealth of 6 each, so return 6.


def maximumWealth(nums):

    # clients = len(accounts)

    # i = 0

    # money = []

    # while i < clients:
    #     sum = 0
    #     for j in range(len(accounts[i])):
    #         sum += accounts[i][j]
    #     i +=1
    #     money.append(sum)

    # return max(money)

    money = 0
    # for i in range(len(nums)):
    #     sum = 0
    #     for j in range(len(nums[i])):
    #         sum += nums[i][j]
    #     money = max(sum, money)

    # return money

    clients = len(nums)

    i = 0

    while i < clients:
        l, r = 1, len(nums[i])
        sum = nums[i][0]
        while l < r:
            sum += nums[i][l]
            l += 1
        money = max(money, sum)
        i += 1

    return money

# 2432. The Employee That Worked on the Longest Task

# There are n employees, each with a unique id from 0 to n - 1.

# You are given a 2D integer array logs where logs[i] = [idi, leaveTimei] where:

#     idi is the id of the employee that worked on the ith task, and
#     leaveTimei is the time at which the employee finished the ith task. All the values leaveTimei are unique.

# Note that the ith task starts the moment right after the (i - 1)th task ends, and the 0th task starts at time 0.

# Return the id of the employee that worked the task with the longest time. If there is a tie between two or more employees, return the smallest id among them.

# Example 1:

# Input: n = 10, logs = [[0,3],[2,5],[0,9],[1,15]]
# Output: 1
# Explanation:
# Task 0 started at 0 and ended at 3 with 3 units of times.
# Task 1 started at 3 and ended at 5 with 2 units of times.
# Task 2 started at 5 and ended at 9 with 4 units of times.
# Task 3 started at 9 and ended at 15 with 6 units of times.
# The task with the longest time is task 3 and the employee with id 1 is the one that worked on it, so we return 1.


def hardestWorker(n, logs):

    d = defaultdict(list)

    max_time = 0
    j = 0
    for i in range(len(logs)):
        if i == 0:
            time = logs[0][1] - 0
            d[logs[0][0]].append(time)
        else:
            time = logs[i][1] - logs[i - 1][1]
            d[logs[i][0]].append(time)

    l = []

    l1 = []

    for item, value in d.items():
        max_value = max(value)
        l1.append(max_value)

    max_value = max(l1)

    for item, value in d.items():
        if max_value in value:
            l.append(item)

    return min(l)

# 2441. Largest Positive Integer That Exists With Its Negative
# Easy

# Given an integer array nums that does not contain any zeros, find the largest positive integer k such that -k also exists in the array.

# Return the positive integer k. If there is no such integer, return -1.

# Example 1:

# Input: nums = [-1,2,-3,3]
# Output: 3
# Explanation: 3 is the only valid k we can find in the array.


def findMaxK(nums):
    maxi = 0

    for num in nums:
        if (num * -1) in nums:
            if abs(num * -1) > maxi:
                maxi = abs(num * -1)

    if maxi == 0:
        return -1
    else:
        return maxi

# 2437. Number of Valid Clock Times
# Easy

# You are given a string of length 5 called time, representing the current time on a digital clock in the format "hh:mm". The earliest possible time is "00:00" and the latest possible time is "23:59".

# In the string time, the digits represented by the ? symbol are unknown, and must be replaced with a digit from 0 to 9.

# Return an integer answer, the number of valid clock times that can be created by replacing every ? with a digit from 0 to 9.

# Example 1:

# Input: time = "?5:00"
# Output: 2
# Explanation: We can replace the ? with either a 0 or 1, producing "05:00" or "15:00". Note that we cannot replace it with a 2, since the time "25:00" is invalid. In total, we have two choices.


def countTime(time):

    res = 1

    if time[0] == "?":
        if time[0] == "?" and time[1] == "?":
            res *= 24
        elif time[0] == "?" and int(time[1]) >= 4:
            res *= 2
        elif time[0] == "?" and int(time[1]) < 4:
            res *= 3

    if time[0] == "?":
        for i in range(3, len(time)):
            if time[i] == "?":
                if i == 3:
                    res *= 6
                elif i == 4:
                    res *= 10
    else:
        for i in range(1, len(time)):
            if time[i] == "?":
                if i == 1 and int(time[0]) < 2:
                    res *= 10
                elif i == 1 and int(time[0]) == 2:
                    res *= 4
                elif i == 3:
                    res *= 6
                elif i == 4:
                    res *= 10

    return res

# 2427. Number of Common Factors
# Easy

# Given two positive integers a and b, return the number of common factors of a and b.

# An integer x is a common factor of a and b if x divides both a and b.

# Example 1:

# Input: a = 12, b = 6
# Output: 4
# Explanation: The common factors of 12 and 6 are 1, 2, 3, 6.


def commonFactors(a, b):

    count = 0

    min_num = min(a, b)

    for i in range(1, min_num + 1):
        if a % i == 0 and b % i == 0:
            count += 1

    return count


# 1647. Minimum Deletions to Make Character Frequencies Unique
# Medium

# A string s is called good if there are no two different characters in s that have the same frequency.

# Given a string s, return the minimum number of characters you need to delete to make s good.

# The frequency of a character in a string is the number of times it appears in the string. For example, in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.

# Example 1:

# Input: s = "aab"
# Output: 0
# Explanation: s is already good.

def minDeletions(self, s: str) -> int:
    """
    make a dictionary where key = char and value = frequency
    create a count variable
    create a list to store the frequency of every char
    create a set to store the seen chars
    loop over the list, if value in the set "seen", we will subtract one from value until not in seen,
    Increase count

    """

    d = dict(Counter(s))
    count = 0
    seen = set()
    l = []
    it_is_repetitive = False

    for value in d.values():
        if value not in seen:
            seen.add(value)
        else:
            while value in seen and value >= 1:
                value = value - 1
                count += 1
            seen.add(value)

    return count

# 2418. Sort the People
# Easy

# You are given an array of strings names, and an array heights that consists of distinct positive integers. Both arrays are of length n.

# For each index i, names[i] and heights[i] denote the name and height of the ith person.

# Return names sorted in descending order by the people's heights.

# Example 1:

# Input: names = ["Mary","John","Emma"], heights = [180,165,170]
# Output: ["Mary","Emma","John"]
# Explanation: Mary is the tallest, followed by Emma and John.


def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
    """

    create a dictionary where key = height and value = name
    crete a list that will be my output
    sort the array heights in reverse order
    loop over my dicitonary, comparing the sorted heights with the value of dicitonary
    """

    d = {}

    for i in range(len(names)):
        d[heights[i]] = names[i]

    output = []

    sorted_list = sorted(heights, reverse=True)

    for height in sorted_list:
        output.append(d[height])

    return output

# 35. Search Insert Position
# Easy

# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2


def searchInsert(self, nums: List[int], target: int) -> int:

    l, r = 0, len(nums) - 1

    while l <= r:
        mid = (l + r) // 2

        if nums[mid] == target:
            return mid

        elif nums[mid] > target:
            r = mid - 1

        elif nums[mid] < target:
            l = mid + 1

    return l

# 1046. Last Stone Weight
# Easy

# You are given an array of integers stones where stones[i] is the weight of the ith stone.

# We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

#     If x == y, both stones are destroyed, and
#     If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.

# At the end of the game, there is at most one stone left.

# Return the weight of the last remaining stone. If there are no stones left, return 0.

# Example 1:

# Input: stones = [2,7,4,1,8,1]
# Output: 1
# Explanation:
# We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
# we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
# we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
# we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.


def lastStoneWeight(self, stones: List[int]) -> int:

    # for i in range(len(stones)):
    #     stones = sorted(stones, reverse= True)
    #     if len(stones) >= 2:
    #         stone1= stones[0]
    #         stone2= stones[1]
    #         if stone1 == stone2 and len(stones) == 2:
    #             return 0
    #         elif stone1 == stone2:
    #             stones.pop(0)
    #             stones.pop(0)
    #         elif stone1 > stone2:
    #             stones[0] = stone1 - stone2
    #             stones.pop(1)
    #         elif stone1 < stone2:
    #             stones[1] = stone2 - stone1
    #             stones.pop(0)
    #     elif len(stones) == 1:
    #         return stones[0]

    for i in range(len(stones)):
        print(stones)
        if len(stones) >= 2:
            stone1 = max(stones)
            stones.remove(stone1)
            stone2 = max(stones)
            stones.remove(stone2)
            # print(stone1, stone2)

            if stone1 == stone2 and len(stones) == 0:
                return 0
            else:
                stones.append(abs(stone1 - stone2))
        elif len(stones) == 1:
            return stones[0]


# 1047. Remove All Adjacent Duplicates In String
# Easy

# You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.

# We repeatedly make duplicate removals on s until we no longer can.

# Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.


# Example 1:

# Input: s = "abbaca"
# Output: "ca"
# Explanation:
# For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".


def removeDuplicates(self, s: str) -> str:

    output = []

    for char in s:
        if len(output) > 0:
            if char == output[-1]:
                output.pop()
            else:
                output.append(char)
        else:
            output.append(char)

    return "".join(output)

# 1920. Build Array from Permutation
# Easy

# Given a zero-based permutation nums (0-indexed), build an array ans of the same length where ans[i] = nums[nums[i]] for each 0 <= i < nums.length and return it.

# A zero-based permutation nums is an array of distinct integers from 0 to nums.length - 1 (inclusive).

# Example 1:

# Input: nums = [0,2,1,5,3,4]
# Output: [0,1,2,4,5,3]
# Explanation: The array ans is built as follows:
# ans = [nums[nums[0]], nums[nums[1]], nums[nums[2]], nums[nums[3]], nums[nums[4]], nums[nums[5]]]
#     = [nums[0], nums[2], nums[1], nums[5], nums[3], nums[4]]
#     = [0,1,2,4,5,3]


def buildArray(self, nums: List[int]) -> List[int]:

    # nums = [0,2,1,5,3,4] - > output = nums[0], nums[2], nums[1] ...

    # create the output list
    # loop over nums
    # output[i] = nums[nums[i]]
    # return output

    output = []

    for num in nums:
        output.append(nums[num])

    return output

# 119. Remove Vowels from a String
# Easy

# Given a string s, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and return the new string.

# Example 1:

# Input: s = "leetcodeisacommunityforcoders"
# Output: "ltcdscmmntyfrcdrs"


def removeVowels(self, s: str) -> str:

    output = ""

    for char in s:
        if char not in "aeiou":
            output += char

    return output

# 263. Ugly Number
# Easy

# An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

# Given an integer n, return true if n is an ugly number.

# Example 1:

# Input: n = 6
# Output: true
# Explanation: 6 = 2 × 3


def isUgly(self, n: int) -> bool:

    if n == 0:
        return False

    while n % 2 == 0:
        n = n // 2

    while n % 3 == 0:
        n = n // 3

    while n % 5 == 0:
        n = n // 5

    if n != 1:
        return False

    return True


# 929. Unique Email Addresses
# Easy

# Every valid email consists of a local name and a domain name, separated by the '@' sign. Besides lowercase letters, the email may contain one or more '.' or '+'.

#     For example, in "alice@leetcode.com", "alice" is the local name, and "leetcode.com" is the domain name.

# If you add periods '.' between some characters in the local name part of an email address, mail sent there will be forwarded to the same address without dots in the local name. Note that this rule does not apply to domain names.

#     For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.

# If you add a plus '+' in the local name, everything after the first plus sign will be ignored. This allows certain emails to be filtered. Note that this rule does not apply to domain names.

#     For example, "m.y+name@email.com" will be forwarded to "my@email.com".

# It is possible to use both of these rules at the same time.

# Given an array of strings emails where we send one email to each emails[i], return the number of different addresses that actually receive mails.


# Example 1:

# Input: emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
# Output: 2
# Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails.

def numUniqueEmails(self, emails: List[str]) -> int:

    ans = set()

    for email in emails:
        index_at = email.index("@")
        s = ""
        for char in email[:index_at]:
            if char == "+":
                break
            if char != ".":
                s += char
        ans.add(s + email[index_at:])

    return len(ans)

# 1874. Minimize Product Sum of Two Arrays
# Medium

# The product sum of two equal-length arrays a and b is equal to the sum of a[i] * b[i] for all 0 <= i < a.length (0-indexed).

#     For example, if a = [1,2,3,4] and b = [5,2,3,1], the product sum would be 1*5 + 2*2 + 3*3 + 4*1 = 22.

# Given two arrays nums1 and nums2 of length n, return the minimum product sum if you are allowed to rearrange the order of the elements in nums1.

# Example 1:

# Input: nums1 = [5,3,4,2], nums2 = [4,2,2,5]
# Output: 40
# Explanation: We can rearrange nums1 to become [3,5,4,2]. The product sum of [3,5,4,2] and [4,2,2,5] is 3*4 + 5*2 + 4*2 + 2*5 = 40.


def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:

    nums1.sort()
    nums2.sort()
    s = 0

    # [2,3,4,5]
    # [5,4,2,2]

    for i in range(len(nums1)):
        res = nums1[i] * nums2[-i - 1]
        s += res

    return s

# 2235. Add Two Integers
# Easy

# Given two integers num1 and num2, return the sum of the two integers.

# Example 1:

# Input: num1 = 12, num2 = 5
# Output: 17
# Explanation: num1 is 12, num2 is 5, and their sum is 12 + 5 = 17, so 17 is returned.


def sum(self, num1: int, num2: int) -> int:

    return (num1 + num2)

# 1108. Defanging an IP Address
# Easy

# Given a valid (IPv4) IP address, return a defanged version of that IP address.

# A defanged IP address replaces every period "." with "[.]".

# Example 1:

# Input: address = "1.1.1.1"
# Output: "1[.]1[.]1[.]1"


def defangIPaddr(self, address: str) -> str:

    # return (address.replace(".", "[.]"))

    new_ip = ""

    for i in range(len(address)):
        if address[i] == ".":
            new_ip += "[.]"
        else:
            new_ip += address[i]

    return new_ip


# 2011. Final Value of Variable After Performing Operations
# Easy

# There is a programming language with only four operations and one variable X:

#     ++X and X++ increments the value of the variable X by 1.
#     --X and X-- decrements the value of the variable X by 1.

# Initially, the value of X is 0.

# Given an array of strings operations containing a list of operations, return the final value of X after performing all the operations.

# Example 1:

# Input: operations = ["--X", "X++", "X++"]
# Output: 1
# Explanation: The operations are performed as follows:
# Initially, X = 0.
# --X: X is decremented by 1, X = 0 - 1 = -1.
# X++: X is incremented by 1, X = -1 + 1 = 0.
# X++: X is incremented by 1, X = 0 + 1 = 1.


def finalValueAfterOperations(self, operations: List[str]) -> int:

    # output = 0

    # for item in operations:
    #     if item == "--X" or item == "X--":
    #         output -= 1
    #     else:
    #         output += 1

    # return output

    X = 0
    for op in operations:
        if "+" in op:
            X += 1
        elif "-" in op:
            X -= 1
    return X

# 1470. Shuffle the Array
# Easy

# Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

# Return the array in the form [x1,y1,x2,y2,...,xn,yn].

# Example 1:

# Input: nums = [2,5,1,3,4,7], n = 3
# Output: [2,3,5,4,1,7]
# Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].


def shuffle(self, nums: List[int], n: int) -> List[int]:

    arr1 = nums[:n]
    arr2 = nums[n:]
    output = []

    for i in range(n):
        output.extend([arr1[i], arr2[i]])

    return output

# 2114. Maximum Number of Words Found in Sentences
# Easy

# A sentence is a list of words that are separated by a single space with no leading or trailing spaces.

# You are given an array of strings sentences, where each sentences[i] represents a single sentence.

# Return the maximum number of words that appear in a single sentence.

# Example 1:

# Input: sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
# Output: 6
# Explanation:
# - The first sentence, "alice and bob love leetcode", has 5 words in total.
# - The second sentence, "i think so too", has 4 words in total.
# - The third sentence, "this is great thanks very much", has 6 words in total.
# Thus, the maximum number of words in a single sentence comes from the third sentence, which has 6 words.


def mostWordsFound(self, sentences: List[str]) -> int:

    max_nums_of_words = 0

    for sentence in sentences:
        sentence = sentence.split(" ")
        sentence_len = len(sentence)
        if sentence_len > max_nums_of_words:
            max_nums_of_words = sentence_len

    return max_nums_of_words

# 1512. Number of Good Pairs
# Easy

# Given an array of integers nums, return the number of good pairs.

# A pair (i, j) is called good if nums[i] == nums[j] and i < j.

# Example 1:

# Input: nums = [1,2,3,1,1,3]
# Output: 4
# Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.


def numIdenticalPairs(self, nums: List[int]) -> int:

    counter = 0

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                counter += 1

    return counter

# 2160. Minimum Sum of Four Digit Number After Splitting Digits
# Easy

# You are given a positive integer num consisting of exactly four digits. Split num into two new integers new1 and new2 by using the digits found in num. Leading zeros are allowed in new1 and new2, and all the digits found in num must be used.

#     For example, given num = 2932, you have the following digits: two 2's, one 9 and one 3. Some of the possible pairs [new1, new2] are [22, 93], [23, 92], [223, 9] and [2, 329].

# Return the minimum possible sum of new1 and new2.

# Example 1:

# Input: num = 2932
# Output: 52
# Explanation: Some possible pairs [new1, new2] are [29, 23], [223, 9], etc.
# The minimum sum can be obtained by the pair [29, 23]: 29 + 23 = 52.


def minimumSum(self, num: int) -> int:

    num = [int(x) for x in str(num)]
    num.sort()
    new1 = str(num[0]) + str(num[2])
    new2 = str(num[1]) + str(num[3])

    return (int(new1) + int(new2))


# 2413. Smallest Even Multiple
# Easy
# Given a positive integer n, return the smallest positive integer that is a multiple of both 2 and n.

# Example 1:

# Input: n = 5
# Output: 10
# Explanation: The smallest multiple of both 5 and 2 is 10.

def smallestEvenMultiple(self, n: int) -> int:

    if n % 2 == 0:
        return n

    for num in range(n, 308, n):
        if num % 2 == 0:
            return num

# 771. Jewels and Stones
# Easy

# You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

# Letters are case sensitive, so "a" is considered a different type of stone from "A".


# Example 1:

# Input: jewels = "aA", stones = "aAAbbbb"
# Output: 3

def numJewelsInStones(self, jewels: str, stones: str) -> int:

    total = 0

    for char in set(stones):
        if char in jewels:
            total += stones.count(char)

    return total

    total = 0
    my_stones = Counter(stones)

    for stone in my_stones:
        if stone in jewels:
            total += my_stones[stone]

    return total


# 1431. Kids With the Greatest Number of Candies
# Easy

# There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.

# Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.

# Note that multiple kids can have the greatest number of candies.


# Example 1:

# Input: candies = [2,3,5,1,3], extraCandies = 3
# Output: [true,true,true,false,true]
# Explanation: If you give all extraCandies to:
# - Kid 1, they will have 2 + 3 = 5 candies, which is the greatest among the kids.
# - Kid 2, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
# - Kid 3, they will have 5 + 3 = 8 candies, which is the greatest among the kids.
# - Kid 4, they will have 1 + 3 = 4 candies, which is not the greatest among the kids.
# - Kid 5, they will have 3 + 3 = 6 candies, which is the greatest among the kids.

def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

    max_candy = max(candies)
    output = []

    for kid in candies:
        total = kid + extraCandies
        if total >= max_candy:
            output.append(True)
        else:
            output.append(False)

    return output


# 1281. Subtract the Product and Sum of Digits of an Integer
# Easy

# Given an integer number n, return the difference between the product of its digits and the sum of its digits.

# Example 1:

# Input: n = 234
# Output: 15
# Explanation:
# Product of digits = 2 * 3 * 4 = 24
# Sum of digits = 2 + 3 + 4 = 9
# Result = 24 - 9 = 15

def subtractProductAndSum(self, n: int) -> int:

    # n % 10 -> last digit
    #  n // 10 -> takes the last digit away

    mult = 1
    summ = 0

    while n != 0:
        last = n % 10
        summ += last
        mult *= last
        n = n // 10

    return (mult - summ)

# 1678. Goal Parser Interpretation
# Easy

# You own a Goal Parser that can interpret a string command. The command consists of an alphabet of "G", "()" and/or "(al)" in some order. The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al". The interpreted strings are then concatenated in the original order.

# Given the string command, return the Goal Parser's interpretation of command.


# Example 1:

# Input: command = "G()(al)"
# Output: "Goal"
# Explanation: The Goal Parser interprets the command as follows:
# G -> G
# () -> o
# (al) -> al
# The final concatenated result is "Goal".

def interpret(self, command: str) -> str:

    return command.replace("()", "o").replace("(al)", "al")


# 1313. Decompress Run-Length Encoded List
# Easy

# We are given a list nums of integers representing a list compressed with run-length encoding.

# Consider each adjacent pair of elements [freq, val] = [nums[2*i], nums[2*i+1]] (with i >= 0).  For each such pair, there are freq elements with value val concatenated in a sublist. Concatenate all the sublists from left to right to generate the decompressed list.

# Return the decompressed list.


# Example 1:

# Input: nums = [1,2,3,4]
# Output: [2,4,4,4]
# Explanation: The first pair [1,2] means we have freq = 1 and val = 2 so we generate the array [2].
# The second pair [3,4] means we have freq = 3 and val = 4 so we generate [4,4,4].
# At the end the concatenation [2] + [4,4,4] is [2,4,4,4].


def decompressRLElist(self, nums: List[int]) -> List[int]:

    output = []

    for i in range(0, len(nums), 2):
        output.extend((nums[i] * [nums[i + 1]]))

    return output


# 43. String Compression
# Medium

# Given an array of characters chars, compress it using the following algorithm:

# Begin with an empty string s. For each group of consecutive repeating characters in chars:

#     If the group's length is 1, append the character to s.
#     Otherwise, append the character followed by the group's length.

# The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

# After you are done modifying the input array, return the new length of the array.

# You must write an algorithm that uses only constant extra space.


# Example 1:

# Input: chars = ["a","a","b","b","c","c","c"]
# Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
# Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".

def compress(self, chars: List[str]) -> int:

    # if len(chars) == 1: return 1
    # start looping over second element -> if there is more than one element. loop over entire list
    # count = 1
    # is element == output[-1] ? YES -> count +=1, NO -> add count, add element to output, count == 1
    # if element is the last one, add count if is > 1
    # return len(output)

    if len(chars) == 1:
        return 1

    output = [chars[0]]
    count = 1

    for i in range(1, len(chars)):
        if chars[i] == output[-1]:
            count += 1
        else:
            if count > 1:
                output.extend(list(str(count)) + [chars[i]])
                count = 1
            else:
                output.append(chars[i])
        if i == len(chars) - 1 and count > 1:
            output.extend(list(str(count)))

    chars[:] = output

    return len(output)

# 1389. Create Target Array in the Given Order
# Easy

# Given two arrays of integers nums and index. Your task is to create target array under the following rules:

#     Initially target array is empty.
#     From left to right read nums[i] and index[i], insert at index index[i] the value nums[i] in target array.
#     Repeat the previous step until there are no elements to read in nums and index.

# Return the target array.

# It is guaranteed that the insertion operations will be valid.

# Example 1:

# Input: nums = [0,1,2,3,4], index = [0,1,2,2,1]
# Output: [0,4,1,3,2]
# Explanation:
# nums       index     target
# 0            0        [0]
# 1            1        [0,1]
# 2            2        [0,1,2]
# 3            2        [0,1,3,2]
# 4            1        [0,4,1,3,2]


def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:

    #     output = []

    #     for i in range(len(nums)):
    #         output.insert(index[i], nums[i] )

    #     return output
    """
    nums = [0,1,2,3,4], index = [0,1,2,2,1] - 0, 1, 2
                        0:[0]
                        1: [ 4, 1]
                        2: [3, 2]

                        - [0, 4, 1, 3 , 2 ]


    """
    arr = []

    for n, i in zip(nums, index):
        arr[i:i] = [n]
    return arr

# 1528. Shuffle String
# Easy

# You are given a string s and an integer array indices of the same length. The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.

# Return the shuffled string.

# Example 1:

# Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
# Output: "leetcode"
# Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.


def restoreString(self, s: str, indices: List[int]) -> str:

    # c = list(zip(indices, s))
    # c.sort(key=lambda item: item[0])

    # # output = ""

    # # for  i, char in c:
    # #     output += char

    # return "".join(list(map(lambda item:item[1], c)))

    # dct = {}

    # for i, char in zip(indices, s):
    #     dct[i] = char

    # res= ""
    # for i in range(len(s)):
    #     res += dct[i]

    # return res

    res = ""
    for i in range(len(s)):
        index = indices.index(i)
        res += s[index]

    return res


# 1636. Sort Array by Increasing Frequency
# Easy

# Given an array of integers nums, sort the array in increasing order based on the frequency of the values. If multiple values have the same frequency, sort them in decreasing order.

# Return the sorted array.

# Example 1:

# Input: nums = [1,1,2,2,2,3]
# Output: [3,1,1,2,2,2]
# Explanation: '3' has a frequency of 1, '1' has a frequency of 2, and '2' has a frequency of 3.

def frequencySort(self, nums: List[int]) -> List[int]:

    # nums = [1,1,2,2,2,3] -> sort in increasing order based on frequency
    #                         -> if tied, sort tied nums in decreasing order

    # nums= [2, 3, 3, 1, 1, 1] - > [2, 3, 3, 1, 1, 1]
    # nums = [1,1,1, 2, 2, 3, 3] -> [ 3, 3, 2, 2, 1, 1, 1]

    dct = defaultdict(list)

    for num in nums:
        dct[nums.count(num)].append(num)

    output = []

    for num in sorted(dct.keys()):
        output.extend(sorted(dct[num], reverse=True))

    return output

    r = Counter(nums).most_common()

    r.sort(key=lambda item: item[0], reverse=True)
    r.sort(key=lambda item: item[1])

    output = []

    for num, freq in r:
        output.extend(freq * [num])
    return output


# 2325. Decode the Message
# Easy

# You are given the strings key and message, which represent a cipher key and a secret message, respectively. The steps to decode message are as follows:

#     Use the first appearance of all 26 lowercase English letters in key as the order of the substitution table.
#     Align the substitution table with the regular English alphabet.
#     Each letter in message is then substituted using the table.
#     Spaces ' ' are transformed to themselves.

#     For example, given key = "happy boy" (actual key would have at least one instance of each letter in the alphabet), we have the partial substitution table of ('h' -> 'a', 'a' -> 'b', 'p' -> 'c', 'y' -> 'd', 'b' -> 'e', 'o' -> 'f').

def decodeMessage(self, key: str, message: str) -> str:

    # seen = set()
    # new_s = ""

    # d = {" ": " "}

    alphabet = list("abcdefghijklmnopqrstuvwxyz")

    # for char in key:
    #     if char not in seen and char != " ":
    #         new_s += char
    #     seen.add(char)

    # for i in range(len(new_s)):
    #     d[new_s[i]] = alphabet[i]

    final = ""
    # for char in message:
    #     final += d[char]

    # return final

    d = {" ": " "}
    i = 0

    for char in key:
        if char not in d:
            d[char] = alphabet[i]
            i += 1

    for char in message:
        final += d[char]

    return final

# 1221. Split a String in Balanced Strings
# Easy

# Balanced strings are those that have an equal quantity of 'L' and 'R' characters.

# Given a balanced string s, split it into some number of substrings such that:

# Each substring is balanced.

# Return the maximum number of balanced strings you can obtain.

# Example 1:

# Input: s = "RLRRLLRLRL"
# Output: 4
# Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.


def balancedStringSplit(self, s: str) -> int:

    l, r = 0, 0
    count = 0

    for char in s:
        if char == "R":
            r += 1
        elif char == "L":
            l += 1
        if r == l:
            count += 1
            l, r = 0, 0

    return count

# 1859. Sorting the Sentence
# Easy
# A sentence is a list of words that are separated by a single space with no leading or trailing spaces. Each word consists of lowercase and uppercase English letters.

# A sentence can be shuffled by appending the 1-indexed word position to each word then rearranging the words in the sentence.

#     For example, the sentence "This is a sentence" can be shuffled as "sentence4 a3 is2 This1" or "is2 sentence4 This1 a3".

# Given a shuffled sentence s containing no more than 9 words, reconstruct and return the original sentence.

# Example 1:

# Input: s = "is2 sentence4 This1 a3"
# Output: "This is a sentence"
# Explanation: Sort the words in s to their original positions "This1 is2 a3 sentence4", then remove the numbers.


def sortSentence(self, s: str) -> str:

    split_s = s.split(" ")
    new_string = list("a" * len(split_s))

    for word in split_s:
        index = int(word[-1]) - 1
        new_string[index] = word[:-1]

    return " ".join(new_string)

# 1773. Count Items Matching a Rule
# Easy

# You are given an array items, where each items[i] = [typei, colori, namei] describes the type, color, and name of the ith item. You are also given a rule represented by two strings, ruleKey and ruleValue.

# The ith item is said to match the rule if one of the following is true:

#     ruleKey == "type" and ruleValue == typei.
#     ruleKey == "color" and ruleValue == colori.
#     ruleKey == "name" and ruleValue == namei.

# Return the number of items that match the given rule.

# Example 1:

# Input: items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], ruleKey = "color", ruleValue = "silver"
# Output: 1
# Explanation: There is only one item matching the given rule, which is ["computer","silver","lenovo"].


def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:

    # items = [["boots", "orange", "jim"], ["computer", "black", "ana"], ["boots", "yellow", "emma"]], rulekey = "type", rulevalue = "computer" -> 1
    """

    find the index of the rulekey, type = 0, color= 1, name= 2
    create a count varaible
    loop over items list, but loop over the index found at rulekey
    check if that item is is ruleValue
    if it is, count +=1
    """

    # if ruleKey == "type":
    #     indexkey = 0
    # elif ruleKey == "color":
    #     indexkey = 1
    # else:
    #     indexkey= 2

    # count = 0

    # for item in items:
    #     if item[indexkey] == ruleValue:
    #         count += 1

    # return count

    d = {"type": 0, "color": 1, "name": 2}

    # count = 0
    # for item in items:
    #     if item[d[ruleKey]] == ruleValue:
    #         count +=1

    # return count

    return sum(1 for item in items if item[d[ruleKey]] == ruleValue)

# 1832. Check if the Sentence Is Pangram
# Easy

# A pangram is a sentence where every letter of the English alphabet appears at least once.

# Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.


# Example 1:

# Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
# Output: true
# Explanation: sentence contains at least one of every letter of the English alphabet.


def checkIfPangram(self, sentence: str) -> bool:

    seen = set()

    for char in sentence:
        if char not in seen:
            seen.add(char)

    if len(seen) == 26:
        return True


# 2367. Number of Arithmetic Triplets
# Easy

# You are given a 0-indexed, strictly increasing integer array nums and a positive integer diff. A triplet (i, j, k) is an arithmetic triplet if the following conditions are met:

#     i < j < k,
#     nums[j] - nums[i] == diff, and
#     nums[k] - nums[j] == diff.

# Return the number of unique arithmetic triplets.

# Example 1:

# Input: nums = [0,1,4,6,7,10], diff = 3
# Output: 2
# Explanation:
# (1, 2, 4) is an arithmetic triplet because both 7 - 4 == 3 and 4 - 1 == 3.
# (2, 4, 5) is an arithmetic triplet because both 10 - 7 == 3 and 7 - 4 == 3.

def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
    """
    loop over in reverse order,
    item - diff in array?
    if yes, again... found number - diff in array?
    if yes, count += 1
    """

    count = 0

    for i in range(len(nums) - 1, -1, -1):
        if nums[i] - diff in nums:
            if (nums[i] - diff) - diff in nums:
                count += 1

    return count


# 1588. Sum of All Odd Length Subarrays
# Easy

# Given an array of positive integers arr, return the sum of all possible odd-length subarrays of arr.

# A subarray is a contiguous subsequence of the array.

# Example 1:

# Input: arr = [1,4,2,5,3]
# Output: 58
# Explanation: The odd-length subarrays of arr and their sums are:
# [1] = 1
# [4] = 4
# [2] = 2
# [5] = 5
# [3] = 3
# [1,4,2] = 7
# [4,2,5] = 11
# [2,5,3] = 10
# [1,4,2,5,3] = 15
# If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58

def sumOddLengthSubarrays(self, arr: List[int]) -> int:

    # [1,4,2,5,3]

    res = 0
    for i in range(len(arr)):
        s = 0
        for j in range(i, len(arr)):
            s += arr[j]
            if (j-i) % 2 == 0:  # checking even because indexes starts from 0 as its even
                res += s
    return res


# 1662. Check If Two String Arrays are Equivalent
# Easy

# Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

# A string is represented by an array if the array elements concatenated in order forms the string.

# Example 1:

# Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
# Output: true
# Explanation:
# word1 represents string "ab" + "c" -> "abc"
# word2 represents string "a" + "bc" -> "abc"
# The strings are the same, so return true.

def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:

    return True if "".join(word1) == "".join(word2) else False


# 804. Unique Morse Code Words
# Easy
# International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows:

#     'a' maps to ".-",
#     'b' maps to "-...",
#     'c' maps to "-.-.", and so on.

# For convenience, the full table for the 26 letters of the English alphabet is given below:

# [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

# Given an array of strings words where each word can be written as a concatenation of the Morse code of each letter.

#     For example, "cab" can be written as "-.-..--...", which is the concatenation of "-.-.", ".-", and "-...". We will call such a concatenation the transformation of a word.

# Return the number of different transformations among all words we have.

# Example 1:

# Input: words = ["gin","zen","gig","msg"]
# Output: 2
# Explanation: The transformation of each word is:
# "gin" -> "--...-."
# "zen" -> "--...-."
# "gig" -> "--...--."
# "msg" -> "--...--."
# There are 2 different transformations: "--...-." and "--...--.".

def uniqueMorseRepresentations(self, words: List[str]) -> int:
    """
    create a dict with key = english letter, value = morse code
    loop over every item in words
    loop over every char in item
    tranform char in code morse
    when loops are over, add word in code morse version to our set
    return lengh of set
    """

    # d = {"a":".-","b":"-...","c":"-.-.","d":"-..","e":".","f":"..-.","g":"--.","h":"....","i":"..","j":".---","k":"-.-","l":".-..","m":"--","n":"-.","o":"---","p":".--.","q":"--.-","r":".-.","s":"...","t":"-","u":"..-","v":"...-","w":".--","x":"-..-","y":"-.--","z":"--.."}

    # seen = set()

    # for item in words:
    #     translation = ""
    #     for char in item:
    #         translation += d[char]
    #     seen.add(translation)

    # return len(seen)

    codem = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
             "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
    alpha = "abcdefghijklmnopqrstuvwxyz"

    d = {}
    seen = set()

    for i in range(len(alpha)):
        d[alpha[i]] = codem[i]

    for item in words:
        translation = ""
        for char in item:
            translation += d[char]
        seen.add(translation)

    return len(seen)


# 760. Find Anagram Mappings
# Easy
# You are given two integer arrays nums1 and nums2 where nums2 is an anagram of nums1. Both arrays may contain duplicates.

# Return an index mapping array mapping from nums1 to nums2 where mapping[i] = j means the ith element in nums1 appears in nums2 at index j. If there are multiple answers, return any of them.

# An array a is an anagram of an array b means b is made by randomizing the order of the elements in a.

# Example 1:

# Input: nums1 = [12,28,46,32,50], nums2 = [50,12,32,46,28]
# Output: [1,4,3,2,0]
# Explanation: As mapping[0] = 1 because the 0th element of nums1 appears at nums2[1], and mapping[1] = 4 because the 1st element of nums1 appears at nums2[4], and so on.


def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
    """
    create res list
    loop over nums1
    use find built in funct to find index of num in nums1 in nums2
    append the found index in res list
    return rest list

    """

    res = []

    for num in nums1:
        index = nums2.index(num)
        res.append(index)

    return res


1323. Maximum 69 Number
# Easy
# You are given a positive integer num consisting only of digits 6 and 9.

# Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).

# Example 1:

# Input: num = 9669
# Output: 9969
# Explanation:
# Changing the first digit results in 6669.
# Changing the second digit results in 9969.
# Changing the third digit results in 9699.
# Changing the fourth digit result


def maximum69Number(self, num: int) -> int:
    """

    create a list, where i will store all the possible combonations, add original num in the list
    loop over every num in num -> convert num in str
    if num is 6 -> 9
    if num is 9 -> 6
    add new num in the list

    """
    # num = str(num)
    # comb = [num]

    # for i in range(len(num)):
    #     if num[i] == "6":
    #         comb.append(num[:i] + "9" + num[i + 1:])
    #     elif num[i] == "9":
    #         comb.append(num[:i] + "6" + num[i + 1:])

    # return max(comb)

    num = list(str(num))

    if "6" in num:
        i = num.index("6")
        num[i] = "9"

    return "".join(num)

# 557. Reverse Words in a String III
# Easy

# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

# Example 1:

# Input: s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"


def reverseWords(self, s: str) -> str:

    t = s.split(" ")
    r = []

    for item in t:
        r.append(item[::-1])

    return " ".join(r)

# 1534. Count Good Triplets
# Easy
# Given an array of integers arr, and three integers a, b and c. You need to find the number of good triplets.

# A triplet (arr[i], arr[j], arr[k]) is good if the following conditions are true:

#     0 <= i < j < k < arr.length
#     |arr[i] - arr[j]| <= a
#     |arr[j] - arr[k]| <= b
#     |arr[i] - arr[k]| <= c

# Where |x| denotes the absolute value of x.

# Return the number of good triplets.

# Example 1:

# Input: arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3
# Output: 4
# Explanation: There are 4 good triplets: [(3,0,1), (3,0,1), (3,1,1), (0,1,1)].


def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:

    count = 0
    for i in range(len(arr) - 2):
        for j in range(i + 1, len(arr) - 1):
            if abs(arr[i] - arr[j]) <= a:
                for k in range(j + 1, len(arr)):
                    if abs(arr[k] - arr[j]) <= b and abs(arr[i] - arr[k]) <= c:
                        count += 1

    return count

# Given an n x n binary matrix image, flip the image horizontally, then invert it, and return the resulting image.

# To flip an image horizontally means that each row of the image is reversed.

#     For example, flipping [1,1,0] horizontally results in [0,1,1].

# To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.

#     For example, inverting [0,1,1] results in [1,0,0].

# Example 1:

# Input: image = [[1,1,0],[1,0,1],[0,0,0]]
# Output: [[1,0,0],[0,1,0],[1,1,1]]
# Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
# Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]


def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:

    for i in range(len(image)):
        image[i] = image[i][::-1]

    for item in image:
        for i in range(len(item)):
            if item[i] == 1:
                item[i] = 0
            else:
                item[i] = 1

    return image


# 2089. Find Target Indices After Sorting Array
# Easy

# You are given a 0-indexed integer array nums and a target element target.

# A target index is an index i such that nums[i] == target.

# Return a list of the target indices of nums after sorting nums in non-decreasing order. If there are no target indices, return an empty list. The returned list must be sorted in increasing order.

# Example 1:

# Input: nums = [1,2,5,2,3], target = 2
# Output: [1,2]
# Explanation: After sorting, nums is [1,2,2,3,5].
# The indices where nums[i] == 2 are 1 and 2.

def targetIndices(self, nums: List[int], target: int) -> List[int]:

    l = []
    nums.sort()
    for i in range(len(nums)):
        if nums[i] == target:
            l.append(i)

    return l


# 2469. Convert the Temperature
# Easy

# You are given a non-negative floating point number rounded to two decimal places celsius, that denotes the temperature in Celsius.

# You should convert Celsius into Kelvin and Fahrenheit and return it as an array ans = [kelvin, fahrenheit].

# Return the array ans. Answers within 10-5 of the actual answer will be accepted.

# Note that:

    # Kelvin = Celsius + 273.15
    # Fahrenheit = Celsius * 1.80 + 32.00
def convertTemperature(self, celsius: float) -> List[float]:

    return [celsius + 273.15, celsius * 1.80 + 32.00]

# 1720. Decode XORed Array
# Easy

# There is a hidden integer array arr that consists of n non-negative integers.

# It was encoded into another integer array encoded of length n - 1, such that encoded[i] = arr[i] XOR arr[i + 1]. For example, if arr = [1,0,2,1], then encoded = [1,2,3].

# You are given the encoded array. You are also given an integer first, that is the first element of arr, i.e. arr[0].

# Return the original array arr. It can be proved that the answer exists and is unique.


# Example 1:

# Input: encoded = [1,2,3], first = 1
# Output: [1,0,2,1]
# Explanation: If arr = [1,0,2,1], then first = 1 and encoded = [1 XOR 0, 0 XOR 2, 2 XOR 1] = [1,2,3]


def decode(self, encoded: List[int], first: int) -> List[int]:

    res = [first]

    for num in encoded:
        temp = num ^ first
        res.append(temp)
        first = temp

    return res

# 2006. Count Number of Pairs With Absolute Difference K
# Easy

# Given an integer array nums and an integer k, return the number of pairs (i, j) where i < j such that |nums[i] - nums[j]| == k.

# The value of |x| is defined as:

#     x if x >= 0.
#     -x if x < 0.

# Example 1:

# Input: nums = [1,2,2,1], k = 1
# Output: 4
# Explanation: The pairs with an absolute difference of 1 are:
# - [1,2,2,1]
# - [1,2,2,1]
# - [1,2,2,1]
# - [1,2,2,1]


def countKDifference(self, nums: List[int], k: int) -> int:

    res = 0

    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if abs(nums[i] - nums[j]) == k:
                res += 1

    return res


# 2315. Count Asterisks
# Easy

# You are given a string s, where every two consecutive vertical bars '|' are grouped into a pair. In other words, the 1st and 2nd '|' make a pair, the 3rd and 4th '|' make a pair, and so forth.

# Return the number of '*' in s, excluding the '*' between each pair of '|'.

# Note that each '|' will belong to exactly one pair.

# Example 1:

# Input: s = "l|*e*et|c**o|*de|"
# Output: 2
# Explanation: The considered characters are underlined: "l|*e*et|c**o|*de|".
# The characters between the first and second '|' are excluded from the answer.
# Also, the characters between the third and fourth '|' are excluded from the answer.
# There are 2 asterisks considered. Therefore, we return 2.

def countAsterisks(self, s: str) -> int:
    output = 0

    split_s = s.split("|")
    for i in range(0, len(split_s), 2):
        output += split_s[i].count("*")

    return output


# 1688. Count of Matches in Tournament
# Easy

# You are given an integer n, the number of teams in a tournament that has strange rules:

#     If the current number of teams is even, each team gets paired with another team. A total of n / 2 matches are played, and n / 2 teams advance to the next round.
#     If the current number of teams is odd, one team randomly advances in the tournament, and the rest gets paired. A total of (n - 1) / 2 matches are played, and (n - 1) / 2 + 1 teams advance to the next round.

# Return the number of matches played in the tournament until a winner is decided.

def numberOfMatches(self, n: int) -> int:

    res = 0

    while True:
        if n % 2 == 0:
            team = n // 2
        else:
            team = (n // 2) + 1
        matches = n // 2
        res += matches
        n = team
        if n == 1:
            break

    return res


# 1486. XOR Operation in an Array
# Easy

# You are given an integer n and an integer start.

# Define an array nums where nums[i] = start + 2 * i (0-indexed) and n == nums.length.

# Return the bitwise XOR of all elements of nums.


# Example 1:

# Input: n = 5, start = 0
# Output: 8
# Explanation: Array nums is equal to [0, 2, 4, 6, 8] where (0 ^ 2 ^ 4 ^ 6 ^ 8) = 8.
# Where "^" corresponds to bitwise XOR operator.

def xorOperation(self, n: int, start: int) -> int:

    res = start + 2 * 0

    for i in range(1, n):
        res ^= start + 2 * i

    return res


# 1614. Maximum Nesting Depth of the Parentheses
# Easy

# Example 1:

# Input: s = "(1+(2*3)+((8)/4))+1"
# Output: 3
# Explanation: Digit 8 is inside of 3 nested parentheses in the string.


def maxDepth(self, s: str) -> int:

    stack = []
    maximum = 0
    for i in s:
        if i == '(':
            stack.append(i)
        elif i == ')':
            maximum = max(maximum, len(stack))
            stack.pop()
    return maximum

# 1304. Find N Unique Integers Sum up to Zero
# Easy

# Given an integer n, return any array containing n unique integers such that they add up to 0.

# Example 1:

# Input: n = 5
# Output: [-7,-1,1,3,4]
# Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].


def sumZero(self, n: int) -> List[int]:

    if n % 2 == 0:
        res = []
    else:
        res = [0]

    for i in range(1, (n//2) + 1):
        res.extend([i, -i])

    return res
    # or
    return range(1 - n, n, 2)


# 2037. Minimum Number of Moves to Seat Everyone
# Easy

# There are n seats and n students in a room. You are given an array seats of length n, where seats[i] is the position of the ith seat. You are also given the array students of length n, where students[j] is the position of the jth student.

# You may perform the following move any number of times:

#     Increase or decrease the position of the ith student by 1 (i.e., moving the ith student from position x to x + 1 or x - 1)

# Return the minimum number of moves required to move each student to a seat such that no two students are in the same seat.

# Note that there may be multiple seats or students in the same position at the beginning.

# Example 1:

# Input: seats = [3,1,5], students = [2,7,4]
# Output: 4
# Explanation: The students are moved as follows:
# - The first student is moved from from position 2 to position 1 using 1 move.
# - The second student is moved from from position 7 to position 5 using 2 moves.
# - The third student is moved from from position 4 to position 3 using 1 move.
# In total, 1 + 2 + 1 = 4 moves were used.

def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:

    seats.sort()
    students.sort()

    count = 0

    for i in range(len(seats)):
        count += abs(seats[i] - students[i])

    return count

# 709. To Lower Case
# Easy

# Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.


def toLowerCase(self, s: str) -> str:

    return s.lower()

# 1464. Maximum Product of Two Elements in an Array
# Easy

# Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).


# Example 1:

# Input: nums = [3,4,5,2]
# Output: 12
# Explanation: If you choose the indices i=1 and j=2 (indexed from 0), you will get the maximum value, that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12.

def maxProduct(self, nums: List[int]) -> int:

    nums.sort()

    return ((nums[-1] - 1) * (nums[-2] - 1))


# 2176. Count Equal and Divisible Pairs in an Array
# Easy

# Given a 0-indexed integer array nums of length n and an integer k, return the number of pairs (i, j) where 0 <= i < j < n, such that nums[i] == nums[j] and (i * j) is divisible by k.


# Example 1:

# Input: nums = [3,1,2,2,2,1,3], k = 2
# Output: 4
# Explanation:
# There are 4 pairs that meet all the requirements:
# - nums[0] == nums[6], and 0 * 6 == 0, which is divisible by 2.
# - nums[2] == nums[3], and 2 * 3 == 6, which is divisible by 2.
# - nums[2] == nums[4], and 2 * 4 == 8, which is divisible by 2.
# - nums[3] == nums[4], and 3 * 4 == 12, which is divisible by 2.

def countPairs(self, nums: List[int], k: int) -> int:

    count = 0
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j] and (i * j) % k == 0:
                count += 1

    return count


# 1844. Replace All Digits with Characters
# Easy

# You are given a 0-indexed string s that has lowercase English letters in its even indices and digits in its odd indices.

# There is a function shift(c, x), where c is a character and x is a digit, that returns the xth character after c.

#     For example, shift('a', 5) = 'f' and shift('x', 0) = 'x'.

# For every odd index i, you want to replace the digit s[i] with shift(s[i-1], s[i]).

# Return s after replacing all digits. It is guaranteed that shift(s[i-1], s[i]) will never exceed 'z'.

# Example 1:

# Input: s = "a1c1e1"
# Output: "abcdef"
# Explanation: The digits are replaced as follows:
# - s[1] -> shift('a',1) = 'b'
# - s[3] -> shift('c',1) = 'd'
# - s[5] -> shift('e',1) = 'f'

def replaceDigits(self, s: str) -> str:

    alpha = "abcdefghijklmnopqrstuvwxyz"

    new_s = ""

    for i in range(len(s)):
        if s[i].isnumeric():
            find_index = alpha.find(new_s[-1])
            correct_char = alpha[find_index + int(s[i])]
            new_s += correct_char

        else:
            new_s += s[i]

    s = new_s

    return s

# 1913. Maximum Product Difference Between Two Pairs
# Easy

# The product difference between two pairs (a, b) and (c, d) is defined as (a * b) - (c * d).

#     For example, the product difference between (5, 6) and (2, 7) is (5 * 6) - (2 * 7) = 16.

# Given an integer array nums, choose four distinct indices w, x, y, and z such that the product difference between pairs (nums[w], nums[x]) and (nums[y], nums[z]) is maximized.

# Return the maximum such product difference.

# Example 1:

# Input: nums = [5,6,2,7,4]
# Output: 34
# Explanation: We can choose indices 1 and 3 for the first pair (6, 7) and indices 2 and 4 for the second pair (2, 4).
# The product difference is (6 * 7) - (2 * 4) = 34.


def maxProductDifference(self, nums: List[int]) -> int:

    nums.sort()

    return abs((nums[0] * nums[1]) - (nums[-2] * nums[-1]))

# 1213. Intersection of Three Sorted Arrays
# Easy

# Given three integer arrays arr1, arr2 and arr3 sorted in strictly increasing order, return a sorted array of only the integers that appeared in all three arrays.

# Example 1:

# Input: arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]
# Output: [1,5]
# Explanation: Only 1 and 5 appeared in the three arrays.


def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:

    output = []

    for num in arr1:
        if num in arr2 and num in arr3:
            output.append(num)

    return output

# 1684. Count the Number of Consistent Strings
# Easy

# You are given a string allowed consisting of distinct characters and an array of strings words. A string is consistent if all characters in the string appear in the string allowed.

# Return the number of consistent strings in the array words.


# Example 1:

# Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
# Output: 2
# Explanation: Strings "aaab" and "baa" are consistent since they only contain characters 'a' and 'b'.

def countConsistentStrings(self, allowed: str, words: List[str]) -> int:

    count = 0

    for word in words:
        count += 1
        for char in word:
            if char not in allowed:
                count -= 1
                break

    return count

# 1967. Number of Strings That Appear as Substrings in Word
# Easy

# Given an array of strings patterns and a string word, return the number of strings in patterns that exist as a substring in word.

# A substring is a contiguous sequence of characters within a string.

# Example 1:

# Input: patterns = ["a","abc","bc","d"], word = "abc"
# Output: 3
# Explanation:
# - "a" appears as a substring in "abc".
# - "abc" appears as a substring in "abc".
# - "bc" appears as a substring in "abc".
# - "d" does not appear as a substring in "abc".
# 3 of the strings in patterns appear as a substring in word.


def numOfStrings(self, patterns: List[str], word: str) -> int:

    count = 0

    for w in patterns:
        if w in word:
            count += 1
    return count

# 1309. Decrypt String from Alphabet to Integer Mapping
# Easy

# You are given a string s formed by digits and '#'. We want to map s to English lowercase characters as follows:

#     Characters ('a' to 'i') are represented by ('1' to '9') respectively.
#     Characters ('j' to 'z') are represented by ('10#' to '26#') respectively.

# Return the string formed after mapping.

# The test cases are generated so that a unique mapping will always exist.

# Example 1:

# Input: s = "10#11#12"
# Output: "jkab"
# Explanation: "j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".


def freqAlphabets(s):
    output = ""
    d = {
        1: "a", 2: "b", 3: "c", 4: "d", 5: "e", 6: "f", 7: "g", 8: "h", 9: "i", 10: "j", 11: "k", 12: "l",
        13: "m", 14: "n", 15: "o", 16: "p", 17: "q", 18: "r", 19: "s", 20: "t", 21: "u", 22: "v", 23: "w",
        24: "x", 25: "y", 26: "z",
    }

    j = len(s) - 1
    while j >= 0:
        if s[j] == "#":
            num = s[j - 2: j]
            print(num)
            output += d[int(num)]
            j -= 3
        else:
            print(s[j])
            output += d[int(s[j])]
            j -= 1

    return output[::-1]

# 1732. Find the Highest Altitude
# Easy

# There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. The biker starts his trip on point 0 with altitude equal 0.

# You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i​​​​​​ and i + 1 for all (0 <= i < n). Return the highest altitude of a point.

# Example 1:

# Input: gain = [-5,1,5,0,-7]
# Output: 1
# Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.


def largestAltitude(self, gain: List[int]) -> int:

    last = gain[0]
    res = max(0, last)

    for i in range(1, len(gain)):

        if (last + gain[i]) > res:
            res = (last + gain[i])
        last = (last + gain[i])

    return res

# 1816. Truncate Sentence
# Easy

# A sentence is a list of words that are separated by a single space with no leading or trailing spaces. Each of the words consists of only uppercase and lowercase English letters (no punctuation).

#     For example, "Hello World", "HELLO", and "hello world hello world" are all sentences.

# You are given a sentence s​​​​​​ and an integer k​​​​​​. You want to truncate s​​​​​​ such that it contains only the first k​​​​​​ words. Return s​​​​​​ after truncating it.

# Example 1:

# Input: s = "Hello how are you Contestant", k = 4
# Output: "Hello how are you"
# Explanation:
# The words in s are ["Hello", "how" "are", "you", "Contestant"].
# The first 4 words are ["Hello", "how", "are", "you"].
# Hence, you should return "Hello how are you".


def truncateSentence(self, s: str, k: int) -> str:

    s_split = s.split(" ")
    output = []

    for i in range(k):
        output.append(s_split[i])

    return " ".join(output)


# 2103. Rings and Rods
# Easy

# There are n rings and each ring is either red, green, or blue. The rings are distributed across ten rods labeled from 0 to 9.

# You are given a string rings of length 2n that describes the n rings that are placed onto the rods. Every two characters in rings forms a color-position pair that is used to describe each ring where:

#     The first character of the ith pair denotes the ith ring's color ('R', 'G', 'B').
#     The second character of the ith pair denotes the rod that the ith ring is placed on ('0' to '9').

# For example, "R3G2B1" describes n == 3 rings: a red ring placed onto the rod labeled 3, a green ring placed onto the rod labeled 2, and a blue ring placed onto the rod labeled 1.

# Return the number of rods that have all three colors of rings on them.

def countPoints(self, rings: str) -> int:

    d = defaultdict(set)

    for i in range(1, len(rings), 2):
        print(i)
        if rings[i - 1] == "B":
            d[rings[i]].add("B")
        elif rings[i - 1] == "G":
            d[rings[i]].add("G")
        elif rings[i - 1] == "R":
            d[rings[i]].add("R")

    count = 0

    for value in d.values():
        if len(value) == 3:
            count += 1

    return count


# 2485. Find the Pivot Integer
# Easy

# Given a positive integer n, find the pivot integer x such that:

# The sum of all elements between 1 and x inclusively equals the sum of all elements between x and n inclusively.

# Return the pivot integer x. If no such integer exists, return -1. It is guaranteed that there will be at most one pivot index for the given input.

# Example 1:

# Input: n = 8
# Output: 6
# Explanation: 6 is the pivot integer since: 1 + 2 + 3 + 4 + 5 + 6 = 6 + 7 + 8 = 21.

def pivotInteger(self, n: int) -> int:

    l = [x for x in range(1, n + 1)]

    res = -1
    for i in range(len(l) + 1):
        if sum(l[0:i + 1]) == sum(l[i:]):
            res = l[i]

    return res


# 1021. Remove Outermost Parentheses
# Easy

# A valid parentheses string is either empty "", "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.

#     For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.

# A valid parentheses string s is primitive if it is nonempty, and there does not exist a way to split it into s = A + B, with A and B nonempty valid parentheses strings.

# Given a valid parentheses string s, consider its primitive decomposition: s = P1 + P2 + ... + Pk, where Pi are primitive valid parentheses strings.

# Return s after removing the outermost parentheses of every primitive string in the primitive decomposition of s.

# Example 1:

# Input: s = "(()())(())"
# Output: "()()()"
# Explanation:
# The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
# After removing outer parentheses of each part, this is "()()" + "()" = "()()()".


def removeOuterParentheses(self, s: str) -> str:

    l, r = 0, 0
    cur = ""
    res = ""

    for char in s:
        cur += char
        if char == "(":
            l += 1
        elif char == ")":
            r += 1

        if l == r:
            res += cur[1:-1]
            cur = ""

    return res


# 1180. Count Substrings with Only One Distinct Letter
# Easy

# Given a string s, return the number of substrings that have only one distinct letter.

# Example 1:

# Input: s = "aaaba"
# Output: 8
# Explanation: The substrings with one distinct letter are "aaa", "aa", "a", "b".
# "aaa" occurs 1 time.
# "aa" occurs 2 times.
# "a" occurs 4 times.
# "b" occurs 1 time.
# So the answer is 1 + 2 + 4 + 1 = 8.

def countLetters(self, s: str) -> int:

    count = 0

    for i in range(len(s)):
        sub = ""
        for j in range(i, len(s)):
            sub += s[j]
            if len(set(list(sub))) == 1:
                count += 1

    return count

# 728. Self Dividing Numbers
# Easy

# A self-dividing number is a number that is divisible by every digit it contains.

#     For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

# A self-dividing number is not allowed to contain the digit zero.

# Given two integers left and right, return a list of all the self-dividing numbers in the range [left, right].

# Example 1:

# Input: left = 1, right = 22
# Output: [1,2,3,4,5,6,7,8,9,11,12,15,22]


def selfDividingNumbers(self, left: int, right: int) -> List[int]:

    l = []
    divisible = False
    for num in range(left, right + 1):
        l_num = list(str(num))
        for n in l_num:
            if "0" in n or num % int(n) != 0:
                divisible = False
            elif num % int(n) == 0:
                divisible = True
            if divisible == False:
                break
        if divisible == True:
            l.append(num)

    return l

# 1295. Find Numbers with Even Number of Digits
# Easy

# Given an array nums of integers, return how many of them contain an even number of digits.

# Example 1:

# Input: nums = [12,345,2,6,7896]
# Output: 2
# Explanation:
# 12 contains 2 digits (even number of digits).
# 345 contains 3 digits (odd number of digits).
# 2 contains 1 digit (odd number of digits).
# 6 contains 1 digit (odd number of digits).
# 7896 contains 4 digits (even number of digits).
# Therefore only 12 and 7896 contain an even number of digits.


def findNumbers(self, nums: List[int]) -> int:

    count = 0

    for num in nums:
        if len(str(num)) % 2 == 0:
            count += 1

    return count

# 942. DI String Match
# Easy

# A permutation perm of n + 1 integers of all the integers in the range [0, n] can be represented as a string s of length n where:

#     s[i] == 'I' if perm[i] < perm[i + 1], and
#     s[i] == 'D' if perm[i] > perm[i + 1].

# Given a string s, reconstruct the permutation perm and return it. If there are multiple valid permutations perm, return any of them.

# Example 1:

# Input: s = "IDID"
# Output: [0,4,1,3,2]


def diStringMatch(self, s: str) -> List[int]:

    l, r = 0, len(s)
    res = []
    i = 0

    while l != r:
        if s[i] == "I":
            res.append(l)
            l += 1
        elif s[i] == "D":
            res.append(r)
            r -= 1
        i += 1

    res.append(l)
    return res

# 2500. Delete Greatest Value in Each Row
# Easy

# You are given an m x n matrix grid consisting of positive integers.

# Perform the following operation until grid becomes empty:

#     Delete the element with the greatest value from each row. If multiple such elements exist, delete any of them.
#     Add the maximum of deleted elements to the answer.

# Note that the number of columns decreases by one after each operation.

# Return the answer after performing the operations described above.

# Example 1:

# Input: grid = [[1,2,4],[3,3,1]]
# Output: 8
# Explanation: The diagram above shows the removed values in each step.
# - In the first operation, we remove 4 from the first row and 3 from the second row (notice that, there are two cells with value 3 and we can remove any of them). We add 4 to the answer.
# - In the second operation, we remove 2 from the first row and 3 from the second row. We add 3 to the answer.
# - In the third operation, we remove 1 from the first row and 1 from the second row. We add 1 to the answer.
# The final answer = 4 + 3 + 1 = 8.


def deleteGreatestValue(self, grid: List[List[int]]) -> int:

    total = 0

    for lst in grid:
        lst.sort()
        lst.reverse()

    for i in range(len(grid[0])):
        max_n = 0
        for j in range(len(grid)):
            max_n = max(max_n, grid[j][i])
        total += max_n

    return total


# 2108. Find First Palindromic String in the Array
# Easy

# Given an array of strings words, return the first palindromic string in the array. If there is no such string, return an empty string "".

# A string is palindromic if it reads the same forward and backward.

# Example 1:

# Input: words = ["abc","car","ada","racecar","cool"]
# Output: "ada"
# Explanation: The first string that is palindromic is "ada".
# Note that "racecar" is also palindromic, but it is not the first.

def firstPalindrome(self, words: List[str]) -> str:

    for word in words:
        if word == word[::-1]:
            return word

    return ""

# 1374. Generate a String With Characters That Have Odd Counts
# Easy

# Given an integer n, return a string with n characters such that each character in such string occurs an odd number of times.

# The returned string must contain only lowercase English letters. If there are multiples valid strings, return any of them.

# Example 1:

# Input: n = 4
# Output: "pppz"
# Explanation: "pppz" is a valid string since the character 'p' occurs three times and the character 'z' occurs once. Note that there are many other valid strings such as "ohhh" and "love".


def generateTheString(self, n: int) -> str:

    if n % 2 != 0:
        return "a" * n
    else:
        s = ("a" * (n - 1)) + "b"
        return s

# 2000. Reverse Prefix of Word
# Easy

# Given a 0-indexed string word and a character ch, reverse the segment of word that starts at index 0 and ends at the index of the first occurrence of ch (inclusive). If the character ch does not exist in word, do nothing.

#     For example, if word = "abcdefd" and ch = "d", then you should reverse the segment that starts at 0 and ends at 3 (inclusive). The resulting string will be "dcbaefd".

# Return the resulting string.

# Example 1:

# Input: word = "abcdefd", ch = "d"
# Output: "dcbaefd"
# Explanation: The first occurrence of "d" is at index 3.
# Reverse the part of word from 0 to 3 (inclusive), the resulting string is "dcbaefd".


def reversePrefix(self, word: str, ch: str) -> str:

    if ch in word:
        i = word.find(ch)
        return word[:i + 1][::-1] + word[i + 1:]
    return word


# 1827. Minimum Operations to Make the Array Increasing
# Easy
# 844
# 39
# Companies

# You are given an integer array nums (0-indexed). In one operation, you can choose an element of the array and increment it by 1.

#     For example, if nums = [1,2,3], you can choose to increment nums[1] to make nums = [1,3,3].

# Return the minimum number of operations needed to make nums strictly increasing.

# An array nums is strictly increasing if nums[i] < nums[i+1] for all 0 <= i < nums.length - 1. An array of length 1 is trivially strictly increasing.

# Example 1:

# Input: nums = [1,1,1]
# Output: 3
# Explanation: You can do the following operations:
# 1) Increment nums[2], so nums becomes [1,1,2].
# 2) Increment nums[1], so nums becomes [1,2,2].
# 3) Increment nums[2], so nums becomes [1,2,3].

 def minOperations(self, nums: List[int]) -> int:

        res =0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i- 1]:
                subt = (nums[i - 1] + 1) - nums[i] 
                res += subt
                nums[i] = (nums[i - 1] + 1)

        return res

# 2185. Counting Words With a Given Prefix

# You are given an array of strings words and a string pref.

# Return the number of strings in words that contain pref as a prefix.

# A prefix of a string s is any leading contiguous substring of s.

 

# Example 1:

# Input: words = ["pay","attention","practice","attend"], pref = "at"
# Output: 2
# Explanation: The 2 strings that contain "at" as a prefix are: "attention" and "attend".

def prefixCount(self, words: List[str], pref: str) -> int:

    count = 0
    n = len(pref)

    for word in words:
        if pref == word[:n]:
            count += 1

    return count

# 1979. Find Greatest Common Divisor of Array
# Given an integer array nums, return the greatest common divisor of the smallest number and largest number in nums.

# The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.

# Example 1:

# Input: nums = [2,5,6,9,10]
# Output: 2
# Explanation:
# The smallest number in nums is 2.
# The largest number in nums is 10.
# The greatest common divisor of 2 and 10 is 2.

def findGCD(self, nums: List[int]) -> int:


    min_n = min(nums)
    max_n = max(nums)

    divisor = 1

    for i in range(max_n  + 1, 1, -1):
        if min_n % i == 0 and max_n  % i == 0:
            return i

    return divisor

# 1941. Check if All Characters Have Equal Number of Occurrences
# Easy

# Given a string s, return true if s is a good string, or false otherwise.

# A string s is good if all the characters that appear in s have the same number of occurrences (i.e., the same frequency).

# Example 1:

# Input: s = "abacbc"
# Output: true
# Explanation: The characters that appear in s are 'a', 'b', and 'c'. All characters occur 2 times in s.

# Example 2:

# Input: s = "aaabb"
# Output: false
# Explanation: The characters that appear in s are 'a' and 'b'.
# 'a' occurs 3 times while 'b' occurs 2 times, which is not the same number of times.

def areOccurrencesEqual(self, s: str) -> bool:

    d = Counter(s)    
    set_d = set()
    set_d.add(d[s[0]])

    for value in d.values():
        if value not in set_d:
            return False

    return True


# 1768. Merge Strings Alternately
# Easy

# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

# Return the merged string.

# Example 1:

# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"

def mergeAlternately(self, word1: str, word2: str) -> str:
        
    min_len = min(len(word1), len(word2))
    res = ""
    
    for i in range(min_len):
        res += word1[i] + word2[i]

    if len(word1) > len(word2):
        res += word1[min_len:]
    elif len(word2) > len(word1):
        res += word2[min_len:]
    
    return res

# 2341. Maximum Number of Pairs in Array

# You are given a 0-indexed integer array nums. In one operation, you may do the following:

#     Choose two integers in nums that are equal.
#     Remove both integers from nums, forming a pair.

# The operation is done on nums as many times as possible.

# Return a 0-indexed integer array answer of size 2 where answer[0] is the number of pairs that are formed and answer[1] is the number of leftover integers in nums after doing the operation as many times as possible.

# Example 1:

# Input: nums = [1,3,2,1,3,2,2]
# Output: [3,1]
# Explanation:
# Form a pair with nums[0] and nums[3] and remove them from nums. Now, nums = [3,2,3,2,2].
# Form a pair with nums[0] and nums[2] and remove them from nums. Now, nums = [2,2,2].
# Form a pair with nums[0] and nums[1] and remove them from nums. Now, nums = [2].
# No more pairs can be formed. A total of 3 pairs have been formed, and there is 1 number leftover in nums.

def numberOfPairs(self, nums: List[int]) -> List[int]:
        
    d = Counter(nums)

    pairs = 0
    leftover = 0

    for value in d.values():
        pairs += value // 2
        leftover += value % 2 
    
    return [pairs, leftover]

# 2119. A Number After a Double Reversal

# Reversing an integer means to reverse all its digits.

#     For example, reversing 2021 gives 1202. Reversing 12300 gives 321 as the leading zeros are not retained.

# Given an integer num, reverse num to get reversed1, then reverse reversed1 to get reversed2. Return true if reversed2 equals num. Otherwise return false.

# Example 1:

# Input: num = 526
# Output: true

def isSameAfterReversals(self, num: int) -> bool:

    num = str(num)

    if len(num) > 1 and num[-1] == "0":
        return False
    return True


# 2351. First Letter to Appear Twice

# Given a string s consisting of lowercase English letters, return the first letter to appear twice.

# Note:

#     A letter a appears twice before another letter b if the second occurrence of a is before the second occurrence of b.
#     s will contain at least one letter that appears twice.

# Example 1:

# Input: s = "abccbaacz"
# Output: "c"
# Explanation:
# The letter 'a' appears on the indexes 0, 5 and 6.
# The letter 'b' appears on the indexes 1 and 4.
# The letter 'c' appears on the indexes 2, 3 and 7.
# The letter 'z' appears on the index 8.
# The letter 'c' is the first letter to appear twice, because out of all the letters the index of its second occurrence is the smallest.

def repeatedCharacter(self, s: str) -> str:

    seen = set()

    for char in s:
        if char in seen:
            return char
        seen.add(char)
            

# 1704. Determine if String Halves Are Alike

# You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first half and b be the second half.

# Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowercase letters.

# Return true if a and b are alike. Otherwise, return false.

# Example 1:

# Input: s = "book"
# Output: true
# Explanation: a = "bo" and b = "ok". a has 1 vowel and b has 1 vowel. Therefore, they are alike.

def halvesAreAlike(self, s: str) -> bool:

    
        def is_vowel(s):

            count = 0
            for char in s:
                if char.lower() in "aeiou":
                    count +=1
            
            return count

        c1 = is_vowel(s[:len(s)//2])
        c2 = is_vowel(s[len(s)//2:])

        if c1 == c2:
            return True

# 1812. Determine Color of a Chessboard Square

# You are given coordinates, a string that represents the coordinates of a square of the chessboard. Below is a chessboard for your reference.

# Return true if the square is white, and false if the square is black.

# The coordinate will always represent a valid chessboard square. The coordinate will always have the letter first, and the number second.

# Example 1:

# Input: coordinates = "a1"
# Output: false
# Explanation: From the chessboard above, the square with coordinates "a1" is black, so return false.

def squareIsWhite(self, coordinates: str) -> bool:

    alpha = "abcdefghijklmnopqrstuvwxyz"
    find_indx = alpha.index(coordinates[0])

    if find_indx % 2 == 0 and int(coordinates[1]) % 2 == 0:
        return True
    elif find_indx % 2 != 0 and int(coordinates[1]) % 2 != 0:
        return True
    else:
        False


# 2278. Percentage of Letter in String

# Given a string s and a character letter, return the percentage of characters in s that equal letter rounded down to the nearest whole percent.

# Example 1:

# Input: s = "foobar", letter = "o"
# Output: 33
# Explanation:
# The percentage of characters in s that equal the letter 'o' is 2 / 6 * 100% = 33% when rounded down, so we return 33.

def percentageLetter(self, s: str, letter: str) -> int:

        lst_s = list(s)
        frequency = lst_s.count(letter)
        return int(frequency / len(s) * 100)

# 1748. Sum of Unique Elements

# You are given an integer array nums. The unique elements of an array are the elements that appear exactly once in the array.

# Return the sum of all the unique elements of nums.
 
# Example 1:

# Input: nums = [1,2,3,2]
# Output: 4
# Explanation: The unique elements are [1,3], and the sum is 4.

def sumOfUnique(self, nums: List[int]) -> int:

    seen = set()
    unique = []

    for num in nums:
        if num not in seen:
            unique.append(num)
            seen.add(num)
        elif num in seen and num in unique:
            unique.remove(num)
        
    return sum(unique)  

# 1450. Number of Students Doing Homework at a Given Time

# Given two integer arrays startTime and endTime and given an integer queryTime.

# The ith student started doing their homework at the time startTime[i] and finished it at time endTime[i].

# Return the number of students doing their homework at time queryTime. More formally, return the number of students where queryTime lays in the interval [startTime[i], endTime[i]] inclusive.

# Example 1:

# Input: startTime = [1,2,3], endTime = [3,2,7], queryTime = 4
# Output: 1
# Explanation: We have 3 students where:
# The first student started doing homework at time 1 and finished at time 3 and wasn't doing anything at time 4.
# The second student started doing homework at time 2 and finished at time 2 and also wasn't doing anything at time 4.
# The third student started doing homework at time 3 and finished at time 7 and was the only student doing homework at time 4.

def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:

    count = 0
    for i in range(len(startTime)):
        if queryTime in range(startTime[i],endTime[i] + 1):
            count += 1

    return count

# 2169. Count Operations to Obtain Zero

# You are given two non-negative integers num1 and num2.

# In one operation, if num1 >= num2, you must subtract num2 from num1, otherwise subtract num1 from num2.

#     For example, if num1 = 5 and num2 = 4, subtract num2 from num1, thus obtaining num1 = 1 and num2 = 4. However, if num1 = 4 and num2 = 5, after one operation, num1 = 4 and num2 = 1.

# Return the number of operations required to make either num1 = 0 or num2 = 0.

# Example 1:

# Input: num1 = 2, num2 = 3
# Output: 3
# Explanation: 
# - Operation 1: num1 = 2, num2 = 3. Since num1 < num2, we subtract num1 from num2 and get num1 = 2, num2 = 3 - 2 = 1.
# - Operation 2: num1 = 2, num2 = 1. Since num1 > num2, we subtract num2 from num1.
# - Operation 3: num1 = 1, num2 = 1. Since num1 == num2, we subtract num2 from num1.
# Now num1 = 0 and num2 = 1. Since num1 == 0, we do not need to perform any further operations.
# So the total number of operations required is 3.

def countOperations(self, num1: int, num2: int) -> int:

    count = 0

    while True:
        if num1 == 0 or num2 == 0:
            break
        elif num1 >= num2:
            num1 = num1 - num2
        else:
            num2 = num2 - num1
        count +=1
    
    return count


# 2535. Difference Between Element Sum and Digit Sum of an Array

# You are given a positive integer array nums.

#     The element sum is the sum of all the elements in nums.
#     The digit sum is the sum of all the digits (not necessarily distinct) that appear in nums.

# Return the absolute difference between the element sum and digit sum of nums.

# Note that the absolute difference between two integers x and y is defined as |x - y|.

# Example 1:

# Input: nums = [1,15,6,3]
# Output: 9
# Explanation: 
# The element sum of nums is 1 + 15 + 6 + 3 = 25.
# The digit sum of nums is 1 + 1 + 5 + 6 + 3 = 16.
# The absolute difference between the element sum and digit sum is |25 - 16| = 9.

def differenceOfSum(self, nums: List[int]) -> int:

    sum1 = sum(nums)

    summing = 0
    for num in nums:
        if len(str(num)) > 1:
            for n in (list(str(num))):
                summing += int(n)
        else:
            summing += num
        
    return sum1 - summing


# 2535. Difference Between Element Sum and Digit Sum of an Array

# You are given a positive integer array nums.

#     The element sum is the sum of all the elements in nums.
#     The digit sum is the sum of all the digits (not necessarily distinct) that appear in nums.

# Return the absolute difference between the element sum and digit sum of nums.

# Note that the absolute difference between two integers x and y is defined as |x - y|.

# Example 1:

# Input: nums = [1,15,6,3]
# Output: 9
# Explanation: 
# The element sum of nums is 1 + 15 + 6 + 3 = 25.
# The digit sum of nums is 1 + 1 + 5 + 6 + 3 = 16.
# The absolute difference between the element sum and digit sum is |25 - 16| = 9.

def differenceOfSum(self, nums: List[int]) -> int:

    sum1 = sum(nums)

    sum2 = sum(map(int,list("".join(map(str,nums)))))

    return sum1 - sum2



# 2357. Make Array Zero by Subtracting Equal Amounts

# You are given a non-negative integer array nums. In one operation, you must:

#     Choose a positive integer x such that x is less than or equal to the smallest non-zero element in nums.
#     Subtract x from every positive element in nums.

# Return the minimum number of operations to make every element in nums equal to 0.

# Example 1:

# Input: nums = [1,5,0,3,5]
# Output: 3
# Explanation:
# In the first operation, choose x = 1. Now, nums = [0,4,0,2,4].
# In the second operation, choose x = 2. Now, nums = [0,2,0,0,2].
# In the third operation, choose x = 2. Now, nums = [0,0,0,0,0].

def minimumOperations(self, nums: List[int]) -> int:

    set_nums = set(nums)

    if 0 in set_nums:
        return len(set_nums) - 1
    else:
        return len(set_nums)


# 1460. Make Two Arrays Equal by Reversing Subarrays

# You are given two integer arrays of equal length target and arr. In one step, you can select any non-empty subarray of arr and reverse it. You are allowed to make any number of steps.

# Return true if you can make arr equal to target or false otherwise.

# Example 1:

# Input: target = [1,2,3,4], arr = [2,4,1,3]
# Output: true
# Explanation: You can follow the next steps to convert arr to target:
# 1- Reverse subarray [2,4,1], arr becomes [1,4,2,3]
# 2- Reverse subarray [4,2], arr becomes [1,2,4,3]
# 3- Reverse subarray [4,3], arr becomes [1,2,3,4]
# There are multiple ways to convert arr to target, this is not the only way to do so.

def canBeEqual(self, target: List[int], arr: List[int]) -> bool:

    target.sort()
    arr.sort()

    if target == arr:
        return True
    else:
        return False

# 1974. Minimum Time to Type Word Using Special Typewriter

# There is a special typewriter with lowercase English letters 'a' to 'z' arranged in a circle with a pointer. A character can only be typed if the pointer is pointing to that character. The pointer is initially pointing to the character 'a'.

# Each second, you may perform one of the following operations:

#     Move the pointer one character counterclockwise or clockwise.
#     Type the character the pointer is currently on.

# Given a string word, return the minimum number of seconds to type out the characters in word.

# Example 1:

# Input: word = "abc"
# Output: 5
# Explanation: 
# The characters are printed as follows:
# - Type the character 'a' in 1 second since the pointer is initially on 'a'.
# - Move the pointer clockwise to 'b' in 1 second.
# - Type the character 'b' in 1 second.
# - Move the pointer clockwise to 'c' in 1 second.
# - Type the character 'c' in 1 second.

def minTimeToType(self, word: str) -> int:

    ans = len(word)
    prev = "a"
    for ch in word: 
        val = (ord(ch) - ord(prev)) % 26 
        ans += min(val, 26 - val)
        prev = ch
    return ans 

# 2389. Longest Subsequence With Limited Sum

# You are given an integer array nums of length n, and an integer array queries of length m.

# Return an array answer of length m where answer[i] is the maximum size of a subsequence that you can take from nums such that the sum of its elements is less than or equal to queries[i].

# A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.


# Example 1:

# Input: nums = [4,5,2,1], queries = [3,10,21]
# Output: [2,3,4]
# Explanation: We answer the queries as follows:
# - The subsequence [2,1] has a sum less than or equal to 3. It can be proven that 2 is the maximum size of such a subsequence, so answer[0] = 2.
# - The subsequence [4,5,1] has a sum less than or equal to 10. It can be proven that 3 is the maximum size of such a subsequence, so answer[1] = 3.
# - The subsequence [4,5,2,1] has a sum less than or equal to 21. It can be proven that 4 is the maximum size of such a subsequence, so answer[2] = 4.

def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:

    ans=[]
    nums.sort()
    for q in queries:
        s=0 #sum of subsequence
        l=0 #length of subsequence
        for i in nums:
            if s+i<=q: #check before adding the element.
                s+=i
                l+=1
            else:
                break
        ans.append(l)
    return ans


# 1337. The K Weakest Rows in a Matrix

# You are given an m x n binary matrix mat of 1's (representing soldiers) and 0's (representing civilians). The soldiers are positioned in front of the civilians. That is, all the 1's will appear to the left of all the 0's in each row.

# A row i is weaker than a row j if one of the following is true:

#     The number of soldiers in row i is less than the number of soldiers in row j.
#     Both rows have the same number of soldiers and i < j.

# Return the indices of the k weakest rows in the matrix ordered from weakest to strongest.

# Example 1:

# Input: mat = 
# [[1,1,0,0,0],
#  [1,1,1,1,0],
#  [1,0,0,0,0],
#  [1,1,0,0,0],
#  [1,1,1,1,1]], 
# k = 3
# Output: [2,0,3]
# Explanation: 
# The number of soldiers in each row is: 
# - Row 0: 2 
# - Row 1: 4 
# - Row 2: 1 
# - Row 3: 2 
# - Row 4: 5 
# The rows ordered from weakest to strongest are [2,0,3,1,4].

def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:

    pairs = []

    for i in range(len(mat)):
        sum_el = sum(mat[i])
        pairs.append((i, sum_el))

    pairs.sort(key=lambda item:item[1])
    
    output = []
    count = 0

    for index, soldier in pairs:
        if count < k:
            output.append(index)
            count += 1


    return output

    return sorted(range(len(mat)), key=lambda x: sum(mat[x]))[:k]

# 2053. Kth Distinct String in an Array

# A distinct string is a string that is present only once in an array.

# Given an array of strings arr, and an integer k, return the kth distinct string present in arr. If there are fewer than k distinct strings, return an empty string "".

# Note that the strings are considered in the order in which they appear in the array.

# Example 1:

# Input: arr = ["d","b","c","b","c","a"], k = 2
# Output: "a"
# Explanation:
# The only distinct strings in arr are "d" and "a".
# "d" appears 1st, so it is the 1st distinct string.
# "a" appears 2nd, so it is the 2nd distinct string.
# Since k == 2, "a" is returned. 

def kthDistinct(self, arr: List[str], k: int) -> str:

    d = Counter(arr)
    distincts = []

    for word in arr:
        if d[word] == 1:
            distincts.append(word)

    if len(distincts) >= k:
        return distincts[k - 1]
    else:
        return ""

# 2496. Maximum Value of a String in an Array

# The value of an alphanumeric string can be defined as:

#     The numeric representation of the string in base 10, if it comprises of digits only.
#     The length of the string, otherwise.

# Given an array strs of alphanumeric strings, return the maximum value of any string in strs.

# Example 1:

# Input: strs = ["alic3","bob","3","4","00000"]
# Output: 5
# Explanation: 
# - "alic3" consists of both letters and digits, so its value is its length, i.e. 5.
# - "bob" consists only of letters, so its value is also its length, i.e. 3.
# - "3" consists only of digits, so its value is its numeric equivalent, i.e. 3.
# - "4" also consists only of digits, so its value is 4.
# - "00000" consists only of digits, so its value is 0.
# Hence, the maximum value is 5, of "alic3".

def maximumValue(self, strs: List[str]) -> int:
        
    output = []
    for s in strs:
        if s.isdigit():
            output.append(int(s))
        elif s.isalnum():
            output.append(len(s))
    
    return max(output)

# 1403. Minimum Subsequence in Non-Increasing Order

# Given the array nums, obtain a subsequence of the array whose sum of elements is strictly greater than the sum of the non included elements in such subsequence. 

# If there are multiple solutions, return the subsequence with minimum size and if there still exist multiple solutions, return the subsequence with the maximum total sum of all its elements. A subsequence of an array can be obtained by erasing some (possibly zero) elements from the array. 

# Note that the solution with the given constraints is guaranteed to be unique. Also return the answer sorted in non-increasing order.

# Example 1:

# Input: nums = [4,3,10,9,8]
# Output: [10,9] 
# Explanation: The subsequences [10,9] and [10,8] are minimal such that the sum of their elements is strictly greater than the sum of elements not included. However, the subsequence [10,9] has the maximum total sum of its elements. 

def minSubsequence(self, nums: List[int]) -> List[int]:
        
    nums.sort(reverse=True)
    total = sum(nums)
    for i in range(len(nums)):
        if sum(nums[:i+1]) > total - sum(nums[:i+1]):
            return nums[:i+1]

# 37. Average of Levels in Binary Tree

# Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.

# Example 1:

# Input: root = [3,9,20,null,null,15,7]
# Output: [3.00000,14.50000,11.00000]
# Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
# Hence return [3, 14.5, 11].

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        if not root:
            return []

        result = []
        queue = deque([root])
        while queue:
            level_size = len(queue)
            level_sum = 0
            for i in range(level_size):
                node = queue.popleft()
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level_sum / level_size)

        return result

# 1475. Final Prices With a Special Discount in a Shop

# You are given an integer array prices where prices[i] is the price of the ith item in a shop.

# There is a special discount for items in the shop. If you buy the ith item, then you will receive a discount equivalent to prices[j] where j is the minimum index such that j > i and prices[j] <= prices[i]. Otherwise, you will not receive any discount at all.

# Return an integer array answer where answer[i] is the final price you will pay for the ith item of the shop, considering the special discount.

# Example 1:

# Input: prices = [8,4,6,2,3]
# Output: [4,2,4,2,3]
# Explanation: 
# For item 0 with price[0]=8 you will receive a discount equivalent to prices[1]=4, therefore, the final price you will pay is 8 - 4 = 4.
# For item 1 with price[1]=4 you will receive a discount equivalent to prices[3]=2, therefore, the final price you will pay is 4 - 2 = 2.
# For item 2 with price[2]=6 you will receive a discount equivalent to prices[3]=2, therefore, the final price you will pay is 6 - 2 = 4.
# For items 3 and 4 you will not receive any discount at all.

def finalPrices(self, prices: List[int]) -> List[int]:

    output = []

    for i in range(len(prices) - 1):
        for j in range(i  + 1, len(prices)):
            if prices[i] >= prices[j]:
                output.append(prices[i] - prices[j])
                break
            if j == len(prices) - 1:
                output.append(prices[i])

    output.append(prices[-1])

    return output

# 2363. Merge Similar Items

# You are given two 2D integer arrays, items1 and items2, representing two sets of items. Each array items has the following properties:

#     items[i] = [valuei, weighti] where valuei represents the value and weighti represents the weight of the ith item.
#     The value of each item in items is unique.

# Return a 2D integer array ret where ret[i] = [valuei, weighti], with weighti being the sum of weights of all items with value valuei.

# Note: ret should be returned in ascending order by value.

# Example 1:

# Input: items1 = [[1,1],[4,5],[3,8]], items2 = [[3,1],[1,5]]
# Output: [[1,6],[3,9],[4,5]]
# Explanation: 
# The item with value = 1 occurs in items1 with weight = 1 and in items2 with weight = 5, total weight = 1 + 5 = 6.
# The item with value = 3 occurs in items1 with weight = 8 and in items2 with weight = 1, total weight = 8 + 1 = 9.
# The item with value = 4 occurs in items1 with weight = 5, total weight = 5.  
# Therefore, we return [[1,6],[3,9],[4,5]].

def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:

    d = {}
    items3 = items1 + items2
    
    for value, weight in items3:
    d[value] = d.get(value, 0 ) + weight

    output = []

    for value, weight in d.items():
        output.append([value, weight])

    output = sorted(output, key=lambda item:item[0])
    
    return output

# 2032. Two Out of Three

# Given three integer arrays nums1, nums2, and nums3, return a distinct array containing all the values that are present in at least two out of the three arrays. You may return the values in any order.


# Example 1:

# Input: nums1 = [1,1,3,2], nums2 = [2,3], nums3 = [3]
# Output: [3,2]
# Explanation: The values that are present in at least two arrays are:
# - 3, in all three arrays.
# - 2, in nums1 and nums2.

# Example 2:

# Input: nums1 = [3,1], nums2 = [2,3], nums3 = [1,2]
# Output: [2,3,1]
# Explanation: The values that are present in at least two arrays are:
# - 2, in nums2 and nums3.
# - 3, in nums1 and nums2.
# - 1, in nums1 and nums3.

# Example 3:

# Input: nums1 = [1,2,2], nums2 = [4,3,3], nums3 = [5]
# Output: []
# Explanation: No value is present in at least two arrays.

def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:

    total_nums= list(set(nums1)) + list(set(nums2)) + list(set(nums3))

    d = Counter(total_nums)
    output = []

    for key, value in d.items():
        if value >= 2:
            output.append(key)

    return output

# 1207. Unique Number of Occurrences
# Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

# Example 1:

# Input: arr = [1,2,2,1,1,3]
# Output: true
# Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.

def uniqueOccurrences(self, arr: List[int]) -> bool:

    d = Counter(arr)
    set_occurrences = set()

    for value in d.values():
        if value in set_occurrences:
            return False
        else:
            set_occurrences.add(value)

    return True

# 2206. Divide Array Into Equal Pairs

# You are given an integer array nums consisting of 2 * n integers.

# You need to divide nums into n pairs such that:

#     Each element belongs to exactly one pair.
#     The elements present in a pair are equal.

# Return true if nums can be divided into n pairs, otherwise return false.


# Example 1:

# Input: nums = [3,2,3,2,2,2]
# Output: true
# Explanation: 
# There are 6 elements in nums, so they should be divided into 6 / 2 = 3 pairs.
# If nums is divided into the pairs (2, 2), (3, 3), and (2, 2), it will satisfy all the conditions.

def divideArray(self, nums: List[int]) -> bool:

    d = Counter(nums)

    for value in d.values():
        if value % 2 != 0:
            return False

    return True

# 387. First Unique Character in a String

# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.


# Example 1:

# Input: s = "leetcode"
# Output: 0


def firstUniqChar(self, s):
    """
    :type s: str
    :rtype: int
    """

    d = Counter(s)
    res = -1

    for i in range(len(s)):
        if d[s[i]] == 1 :
            return i

    return res