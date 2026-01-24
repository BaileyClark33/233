"""
Part 1: Array Creation
(a) convert the startList given below to a one dimensional array. Print this array, and it's shape. Nicely.

(b) convert the startList given below into a two dimensional array, of 4 rows of 3 columns. Print this array, and it's shape. Nicely. (NOTE: When printing structures like arrays,
lists and so on, printing nicely DOESN'T mean you have to iterate over them. It just means 'add text so I know what I'm looking at, e.g. Here is listA....')

(c) Use arange to produce a one dimensional array of values starting at 4, and ending at 14. Both 4 and 14 should appear in the array. Print this array, and it's shape. Nicely.

(d) Create an array of random integers in the range 2 to 11 (inclusive) that is of dimension 5 rows by 4 columns. Print this array, and it's shape. Nicely.

(e) Create an array of random floats in the range 0 to 1, with 7 rows of 4 columns. Print this array, and it's shape. Nicely.
HINT: To do this, look up the numpy random.random function. It'll help.
"""

import numpy as np

startList = [8, 5, 3, 3, 2, 8, 9, 1, 2, 4, 6, 0]

array_1a = np.array(startList)
print("Array part a:", array_1a, "Shape:", array_1a.shape)

array_1b = np.array(startList).reshape(4, 3)
print("Array part b:")
print(array_1b)
print("Shape:", array_1b.shape)

array_1c = np.arange(4, 15)
print("Array part c:", array_1c, "Shape:", array_1c.shape)

array_1d = np.random.randint(2, 12, size=(5, 4))
print("Array part d:")
print(array_1d)
print("Shape:", array_1d.shape)

array_1e = np.random.random(size=(7, 4))
print("Array part e:")
print(array_1e)
print("Shape:", array_1e.shape)


"""
Part 2: Array Math
(a) Generate an array of random values, in the range 0 to 1, with 10 rows of 6 columns. Print the array.

(b) Find the MAXIMUM value in EACH COLUMN. Print the results

(c) Find the mean of each column. Print the results

(d) Take the mean from (c) away from the max for each column, and print the results.

(e) Tell me which column (using it's index value) has the largest value for (d). Do NOT do this by hand - have code figure it out.

(f) Print the sum of the means of all the rows.

HINT: For (e), there's a function in numpy called argmax that's helpful.

HINT: Make sure you check your answers by hand to confirm you got the correct value.
"""

array_2a = np.random.random(size=(10, 6))
print("Array part 2a:")
print(array_2a)
print()

max_per_column = np.max(array_2a, axis=0)
print("Max per column:")
print(max_per_column)
print()

mean_per_column = np.mean(array_2a, axis=0)
print("Mean per column:")
print(mean_per_column)
print()

difference = max_per_column - mean_per_column
print("Difference between max and mean per column:")
print(difference)
print()

largest_diff_index = np.argmax(difference)
print("Column (start at index 0) with largest difference:", largest_diff_index)
print()

mean_sum = np.sum(np.mean(array_2a, axis=1))
print("Sum of the means of all the rows:", mean_sum)
print()

"""
    Part 3: Slicing and Selection
(a) Starting with the list given below, reshape it into an array of 7 rows and 3 colums

(b) If you've done it correctly, you should see a square inside your array comprised of the value 99. Slice this square of values from your array in (a)

(c) Change the values in the slice from b, making the top left and bottom right 101 instead of 99, WITHOUT changing the original array from (a). 
Print both array from (a) and array from (c) when you've done.

(d) Slice out the first column from (a) and print it

(e) Slice out the second row from (a) and print it

(f) Slice out the last two elements of the bottom row of (a), and print them

(g) Create a logical mask for all the items in your array from (a) that are odd

(h) Use this mask from (g) as an index, and create a new array of all the values that are odd

(i) Use slicing on your array from (a) to produce two variables. One variable containing 7 rows of 2 columns (all the data EXCEPT the last column from each row),
and one variable that is a 7 by 1 array, containing the values from the last column. You will need to reshape this last variable (so a (7,) shape is not acceptable, but a (7,1) is).

(j) Create a one dimensional vector of 100 random values in the range 0 to 1. Generate a second one dimensional vector of integers, 
starting at 5 and ending at 12 (both 5 and 12 should be in the vector). Use this vector of integers as a mask to select elements from the 100 element vector of floats,
at those index positions. Print out the resulting selection.

# Copilot, the 99's show up at (3, 1), (3, 2), (4, 1), (4, 2)
"""

startList_2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 99, 99, 12, 99, 99, 15, 16, 17, 18, 19, 20]

array_3a = np.array(startList_2).reshape(7, 3)
print("Array part a:")
print(array_3a)
print()

array_3b = array_3a[3:5, 1:3]
print("Array part b (sliced square):")
print(array_3b)
print()

array_3c = array_3a.copy()
array_3c[3, 1] = 101
array_3c[4, 2] = 101
print("Array part c:")
print(array_3c)
print()
print("Original array from part a:")
print(array_3a)
print()

first_column = array_3a[:, 0]
print("First column from part d:", first_column)
print()

second_row = array_3a[1, :]
print("Second row from part e:", second_row)
print()

last_two_elements = array_3a[6, 1:3]
print("Last two elements of bottom row from part f:", last_two_elements)
print()

odd_mask = array_3a % 2 == 1
odd_values = array_3a[odd_mask]
print("All odd values in array")
print(odd_values)
print()

array_3i_2col = array_3a[:, :2]
array_3i_1col = array_3a[:, 2].reshape(7, 1)
print("Array part i - two column:")
print(array_3i_2col)
print()

print("Array part i - one column:")
print(array_3i_1col)
print()

array_3j_floats = np.random.random(size=100)
array_3j_indices = np.arange(5, 13)
print("Selected values from part j:")
print(array_3j_floats[array_3j_indices])
