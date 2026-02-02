"""
Part 1: DataFrame Creation
(a) Create a dictionary of student populations for the cities which house the top 10 state schools by population, taken from Wikipedia. Use the 2024-25 enrollment table.
Create this by hand, by writing out the dictionary.

(b) Create a dictionary of total city population for the cities named in the dictionary above, using the information from Wikipedia. Use the estimated 2024 column for your dictionary.
If any of the cities or towns in part (a) don't appear in this table, Google, and find an estimate. Use that number instead. Make sure you document where you get your numbers from.

(c) Create two series, one for each of the dictionaries in (a) and (b). Make the city name the index, and the population the value for each.

(d) Create a dataframe from the two series. Print the dataframe

(e) Generate a new column, percentage, that is the percentage of the total city population that is students. Divide the student population by the total population,
and multiply by 100.

(f) Extract the values of the percentage from the data frame. Print the min, the max and the mean density from the resulting values.
Print all values to 2 decimal places (e.g. 20.23%). This is a useful string format guide

(g) The argmax method you explored last week works for Pandas series. So use it to find the index, and use that index to find the value it returns to
print the name of the town with highest percentage student population in this data.
"""

import pandas as pd

# Dictionary of student populations
student_population = {
    "College Station": 79114,  # Texas A&M University
    "Orlando": 69818,  # University of Central Florida
    "Columbus": 66901,  # Ohio State University
    "Gainesville": 60795,  # University of Florida
    "Urbana-Champaign": 59238,  # University of Illinois
    "Minneapolis": 56666,  # University of Minnesota
    "Tempe": 56643,  # Arizona State University
    "Miami": 55687,  # Florida International University
    "Austin": 52384,  # University of Texas
    "East Lansing": 52089,  # Michigan State University
}

# Dictionary of total city populations
city_population = {
    "College Station": 120511,  # Source: Wikipedia
    "Orlando": 316121,  # Source: Wikipedia
    "Columbus": 913175,  # Source: Wikipedia
    "Gainesville": 145214,  # Source: Wikipedia
    "Urbana-Champaign": 126638,  # Source: Wikipedia (combined Urbana + Champaign)
    "Minneapolis": 425336,  # Source: Wikipedia
    "Tempe": 189988,  # Source: Wikipedia
    "Miami": 449514,  # Source: Wikipedia
    "Austin": 984567,  # Source: Wikipedia
    "East Lansing": 47741,  # Source: Wikipedia
}

student_series = pd.Series(student_population)
city_series = pd.Series(city_population)

df = pd.DataFrame(
    {"Student Population": student_series, "City Population": city_series}
)
print("DataFrame:")
print(df)
print()

df["Percentage"] = (df["Student Population"] / df["City Population"]) * 100

percentages = df["Percentage"]
print(f"Min percentage: {percentages.min():.2f}%")
print(f"Max percentage: {percentages.max():.2f}%")
print(f"Mean percentage: {percentages.mean():.2f}%")
print()

highest_city_index = percentages.idxmax()
print(f"City with highest percentage student population: {highest_city_index}")


"""
Part 2: Sink or Swim
On our course website a CSV file of the Titanic dataset. This set is conventionally split into two - one part for training models, and one part for testing the resulting model. 
We'll see what that means later.

For now, know that I've given you access to the training data set. The name and path of the file are given in the cell below.

You know some basic pandas commands for manipulating data. Remember that you can think of the underlying representation of that data as a numpy array. 
Try to use 'array-like' operations when completing the following. I don't mean you need to extract the values as arrays, but that you can use array-like behavior over 
Series and DataFrames as we have seen in class.

(a) Load the data into a dataframe, and print me some basic numbers - how many rows and how many columns?

(b) There's a column in the data called 'Survived'. The score is 1 if they survived, and, well, 0 if they didn't.

You can use the sum method, to tell me how many people survived in this data set. Print both the total number of survivors, AND the percentage survival rate, to 2 decimal places. 
This is a good standard for printing stats from now on.

(c) We know something about the passengers. We're going to focus on two elements, their gender (represented in the 'Sex' column) and their class of travel
(represented in the 'Pclass' column). For Pclass, 1 means first class, 2 means second class and 3 means third class.

We're going to see if we can figure out the likely futures of Rose (female, first class) and Jack (male, third class) from the Titanic movie.

(If you've not seen the movie Titanic, then a bunch of references in this assignment will go over your head. You'll lose nothing, except some eye rolling)

To do this we're going to want to extract subsets of our overall data.

This is very similar to the masking you did in a previous assignment.

For instance, taking the states data we created in class, you can create a mask to pull out places with a population greater than say 70000, by writing:

popMask = states_df['population'] > 70000

and then using that mask to index the data frame:

highPop_df = states_df[popMask]

Often in pandas documentation, you'll see them combine these two steps into one:

highPop_df = states_df[states_df['population'] > 70000]

I don't mind which method you use, so long as it makes sense to you. For columns where the content is a string, such as the 'Sex' column, then we most usually test to 
see if a string is equal to something, or not equal to something.

Here's want I want you to do:

Extract data for only the female passengers
Tell me how many female passengers there were in this data
both as a total number, and as a percentage of all the passengers in the data
Find out how many women survived
print both as a total number and the percentage of women passengers that survived (as a percent of the women passengers as a whole). 
Check your math and make sure everything makes sense.
(d) Repeat the above, but for the male passengers.

(e) Ok, but what about the class? There are three passenger classes. Repeat the exercise above, but print me stats (total numbers, survivors, percentages) 
for each of the classes, regardless of gender.

(f) Finally, tell me what the survival percentage was for female passengers in first class, and for male passengers in third class. 
This requires you to use logical combinations. So, for example, extract all the female, first class passengers and find what percentage of those survived. Repeat for males.

These are all combinations of things we have done together in class. You can make this as complicated as you want, but I only want you to use methods we have covered in class.

This BTW is NOT how we might address this for real - or rather in time I'm going to show you other ways to achieve this. 
But for now I want you to work on the basic level we've looked at in class. That also means that if you do find a solution to this online, it's probably wrong for this assignment...

(g) In the text box below, give me a parargraph or so write up on the survivability chances of the genders, passenger classes, and how those correspond to two 
hypothetical characters: Jack, a third class man, and Rose, a first class female. THIS is the critical part of data analytics. Using data to tell a story. 
Write your response in markdown cell below, not as a short answer question to this prompt in this cell. Use full sentences and paragraph breaks as you would for an 
essay writing assignment. While spelling and grammar are not critical for a good grade, thoughfullness and authenticity are important.
"""

# Do part 2 here

path = "https://georgiadoing.github.io/CSC233-W26/Data/"
csv_file = "titanic_train.csv"

filename = path + csv_file

titanicData = pd.read_csv(filename)

print("Part a")
num_rows = len(titanicData)
num_columns = len(titanicData.columns)
print(f"Number of rows: {num_rows}")
print(f"Number of columns: {num_columns}")
print()

print("Part b")
total_survivors = titanicData["Survived"].sum()
survival_rate = (total_survivors / num_rows) * 100
print(f"Total survivors: {total_survivors}")
print(f"Survival rate: {survival_rate:.2f}%")
print()

print("Part c")
female_df = titanicData[titanicData["Sex"] == "female"]
num_females = len(female_df)
female_percentage = (num_females / num_rows) * 100
female_survivors = female_df["Survived"].sum()
female_survival_rate = (female_survivors / num_females) * 100
print(
    f"Total female passengers: {num_females} ({female_percentage:.2f}% of all passengers)"
)
print(f"Female survivors: {female_survivors}")
print(f"Female survival rate: {female_survival_rate:.2f}%")
print()

print("Part d")
male_df = titanicData[titanicData["Sex"] == "male"]
num_males = len(male_df)
male_percentage = (num_males / num_rows) * 100
male_survivors = male_df["Survived"].sum()
male_survival_rate = (male_survivors / num_males) * 100
print(f"Total male passengers: {num_males} ({male_percentage:.2f}% of all passengers)")
print(f"Male survivors: {male_survivors}")
print(f"Male survival rate: {male_survival_rate:.2f}%")
print()

print("Part e")
for pclass in [1, 2, 3]:
    class_df = titanicData[titanicData["Pclass"] == pclass]
    num_passengers = len(class_df)
    class_percentage = (num_passengers / num_rows) * 100
    class_survivors = class_df["Survived"].sum()
    class_survival_rate = (class_survivors / num_passengers) * 100
    print(f"Class {pclass}:")
    print(
        f"Total passengers: {num_passengers} ({class_percentage:.2f}% of all passengers)"
    )
    print(f"Survivors: {class_survivors}")
    print(f"Survival rate: {class_survival_rate:.2f}%")
print()

print("Part f")
female_first_class = titanicData[
    (titanicData["Sex"] == "female") & (titanicData["Pclass"] == 1)
]
rose_survival_rate = (
    female_first_class["Survived"].sum() / len(female_first_class)
) * 100

male_third_class = titanicData[
    (titanicData["Sex"] == "male") & (titanicData["Pclass"] == 3)
]
jack_survival_rate = (male_third_class["Survived"].sum() / len(male_third_class)) * 100

print(f"Rose (female, first class) survival rate: {rose_survival_rate:.2f}%")
print(f"Jack (male, third class) survival rate: {jack_survival_rate:.2f}%")

"""
Part 3: Rock of Ages
You should see in the data that there is a column called Age. It holds the age of the passenger. There are missing values in this column.

(a) Show HOW MANY missing values there are. To do that, you can create a mask using the isnull() method, 
which will create a True value where each age is in fact NaN. You can then SUM those True values to get a count. 
Print the total number, and the percentage of missing values in the Age column.

(b) If we try any aggregate statistics like median or mean on a numpy array from this column, the result will be NaN, 
because of those missing values. Instead, using a notnull() mask on the 'Age' column, extract only the non-NaN values, 
and compute and print the median, the mean, the min and the max values for age.

(c) Call the .hist() method on a Series containing the age values, after the NaN values have been removed.
Write something about the distribution of ages on that fateful journey of the Titanic.

We'll talk about labeling this histogram nicely later.
"""

# Do part 3 here

print("Part a")
age_missing_mask = titanicData["Age"].isnull()
num_missing_age = age_missing_mask.sum()
total_age_entries = len(titanicData)
percentage_missing = (num_missing_age / total_age_entries) * 100
print(f"Total missing: {num_missing_age}")
print(f"Percentage missing: {percentage_missing:.2f}%")
print()

print("Part b")
age_notnull_mask = titanicData["Age"].notnull()
age_values = titanicData["Age"][age_notnull_mask]
age_median = age_values.median()
age_mean = age_values.mean()
age_min = age_values.min()
age_max = age_values.max()
print(f"Median age: {age_median:.2f}")
print(f"Mean age: {age_mean:.2f}")
print(f"Minimum age: {age_min:.2f}")
print(f"Maximum age: {age_max:.2f}")
print()

print("Part c")
_ = age_values.hist()
print("""
The age distribution of Titanic passengers shows a concentration of adults
in their 20s and 30s, with the most common age group being young adults.
The distribution is slightly right-skewed, with a long tail extending to
older passengers up to 80 years old. There is also a notable presence of
children and infants, particularly in the younger age ranges below 10 years.
Overall, the passenger demographic skewed younger, reflecting the typical
age distribution of travelers in the early 20th century.
""")
