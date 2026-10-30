# 1.Array Sum


# def read_array():
#     n = int(input("Enter N: "))
#     arr = []
#     for i in range(n):
#         value = int(input("Enter element " + str(i + 1) + ": "))
#         arr.append(value)
#     return arr


# arr = read_array()
# total = 0
# for x in arr:
#     total = total + x
# print("Sum =", total)


#  2.Largest, Second Largest, Smallest, Second Smallest

# arr = read_array()

# largest = arr[0]
# smallest = arr[0]
# for x in arr:
#     if x > largest:
#         largest = x
#     if x < smallest:
#         smallest = x

# second_largest = None
# for x in arr:
#     if x < largest:
#         if second_largest is None or x > second_largest:
#             second_largest = x

# second_smallest = None
# for x in arr:
#     if x > smallest:
#         if second_smallest is None or x < second_smallest:
#             second_smallest = x

# print("Largest         =", largest)
# print("Second largest  =", second_largest)
# print("Smallest        =", smallest)
# print("Second smallest =", second_smallest)


# 3.Count Even and Odd

# arr = read_array()
# even = 0
# odd = 0
# for x in arr:
#     if x % 2 == 0:
#         even = even + 1
#     else:
#         odd = odd + 1
# print("Even numbers =", even)
# print("Odd numbers  =", odd)


# 4.Search element

# arr = read_array()
# key = int(input("Enter number to search: "))

# found = False
# for i in range(len(arr)):
#     if arr[i] == key:
#         print(key, " at ", i + 1)
#         found = True

# if not found:
#     print(key, "not  in array")


# 5.Reverse array

# arr = read_array()

# print("Reverse order:", end=" ")

# for i in range(len(arr) - 1, -1, -1):
#     print(arr[i], end=" ")
# print()

# print("Original array:", arr)


# 6.Remove duplicates

# arr = read_array()
# unique = []
# for x in arr:
#     if x not in unique:
#         unique.append(x)
# print("Array without duplicates:", unique)


# 7.Move zeros
# arr = read_array()

# result = []
# zero_count = 0

# for x in arr:
#     if x == 0:
#         zero_count = zero_count + 1
#     else:
#         result.append(x)

# for i in range(zero_count):
#     result.append(0)

# print("After moving zeros:", result)


# 8.Patterns

# Pattern 1
size = 7
mid = size // 2
for row in range(size):
    for col in range(size):
        if row == mid or col == mid:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print("\b")

#  Pattern 2:
n = 5
for row in range(n):
    for col in range(n):
        if row == 0 or row == 4 or col == 0 or col == 4:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


# Pattern 3
n = 5
size = 2 * n - 1
mid = n - 1
for row in range(size):
    for col in range(size):
        distance = abs(row - mid) + abs(col - mid)
        if distance == mid:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


# Pattern 4
n = 5
for i in range(n + 1):
    for s in range(n - i):
        print(" ", end=" ")
    for num in range(i + 1):
        print(num+1, end=" ")
    for num in range(i, 0, -1):
        print(num, end=" ")
    print()


# Pattern 5
n = 5
for row in range(n):
    for col in range(n):
        if (row + col) % 2 == 0:
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()


# 9. Count vowels, consonants, digits, special characters
# text = input("Enter a string: ")
# vowels = 0
# consonants = 0
# digits = 0
# special = 0

# for ch in text:
#     if ch.isalpha():
#         if ch.lower() in "aeiou":
#             vowels = vowels + 1
#         else:
#             consonants = consonants + 1
#     elif ch.isdigit():
#         digits = digits + 1
#     else:
#         special = special + 1

# print("Vowels             =", vowels)
# print("Consonants         =", consonants)
# print("Digits             =", digits)
# print("Special characters =", special)


# 10. Find all occurrences of a substring

# text = input("Enter the main string: ")
# sub = input("Enter the substring: ")

# count = 0
# for i in range(len(text) - len(sub) + 1):
#     if text[i:i + len(sub)] == sub:
#         count = count + 1
#         print("Found at index", i)

# print("Total occurrences =", count)


# 11. Reverse word
# sentence = input("Enter a sentence: ")
# words = sentence.split()

# result = ""
# for word in words:
#     reversed_word = ""
#     for ch in word:
#         reversed_word = ch + reversed_word
#     result = result + reversed_word + " "

# print(result.strip())


# 12. Longest , shortest word
# sentence = input("Enter a sentence: ")
# words = sentence.split()

# longest = words[0]
# shortest = words[0]

# for word in words:
#     if len(word) > len(longest):
#         longest = word
#     if len(word) < len(shortest):
#         shortest = word

# print("Longest word  =", longest)
# print("Shortest word =", shortest)

