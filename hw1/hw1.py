import random
import csv

nums = []
n = int(input("How many numbers will you enter? "))
for i in range(n):
    num = int(input("Enter number " + str(i + 1) + ": "))
    nums.append(num)


largest = float("-inf")
smallest = float("inf")
mean = 0

for i in range(len(nums)):
    if nums[i] > largest:
        largest = nums[i]
    if nums[i] < smallest:
        smallest = nums[i]
    mean += nums[i]

mean = mean / len(nums)
print("Largest number: ", largest)
print("Smallest number: ", smallest)
print("Mean: ", mean)


part2_a1 = [2.3, "nick", "cat", 5, 6, "squirrel"]

part2_b1 = [44, 55, 66, 77, 88, 99]
part2_b2 = ["chicken", "zebra", "koala", "budgie", "elephant"]

print(part2_a1[: len(part2_a1) // 2])
print(part2_a1[(len(part2_a1) + 1) // 2 :])


def split_list(input_list):
    mid = len(input_list) // 2
    first_half = input_list[:mid]
    second_half = input_list[mid:]
    return first_half, second_half


print(split_list(part2_b1))
print(split_list(part2_b2))

copied_list = part2_b2[:]
print("Original list: ", part2_b2)
copied_list[0] = "Bailey"
print("Copied list: ", copied_list)


part3_a1 = [2, 6, 7.3, 9, 1, 10, 3, 4.9]

part3_b1 = [-2, 6, -7.3, 0, 1, 10, -3, 4.9]

part3_c1 = ["A", "B", "C"]
part3_c2 = [1, 2, 3]

part3_d1 = ["2.3", "nick", "cat", "5", "6", "squirrel"]

q1_list = [x for x in part3_a1 if x < 5]
print(q1_list)

q2_list = [True if x <= 0 else False for x in part3_b1]
print(q2_list)

q3_list = [[x, y] for x in part3_c1 for y in part3_c2]
print(q3_list)

q4_list = [int(x) for x in part3_d1 if x.isdigit()]
print(q4_list)

part4_c3 = [True, False, True]


def count_elements(list):
    count = {}
    for item in list:
        if item in count:
            count[item] += 1
        else:
            count[item] = 1
    return count


rand_list = [random.randint(1, 6) for _ in range(100)]

rand_list_count = count_elements(rand_list)
print(rand_list_count)

highest = -1
mode = ""
for key, value in rand_list_count.items():
    if value > highest:
        highest = value
        mode = key

print("Unique Elements:", len(rand_list_count), "Mode:", mode)

q3_dict = {}
for i in range(len(part4_c3)):
    q3_dict["col" + str(i + 1)] = part4_c3[i]

user = input("What column do you want to access?")
column_name = "col" + user
if column_name in q3_dict:
    print("Value:", q3_dict[column_name])
else:
    print("Column does not exist.")

file = open("/content/drive/MyDrive/Colab Notebooks/Data/assignment1.csv")


data = []
for row in csv.reader(file):
    data.append(row)

dict = {}
keys = data[0]
for i in range(1, len(data)):
    for j in range(len(keys)):
        if keys[j] not in dict:
            dict[keys[j]] = []
        dict[keys[j]].append(data[i][j])

print(dict)
