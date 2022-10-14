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
