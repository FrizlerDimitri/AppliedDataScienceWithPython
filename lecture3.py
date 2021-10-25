import csv
import numpy as np
import pandas as pd


# Activity 1 - Write a function that takes a filename as input.
# You will be using the bill_of_rights.txt located in the data folder for
# this activity. Write a function that takes the filename as input and finds
# the total number of lines, words and most frequent word in the file and writes
# these statistics into a file named ‘stats.txt’.

def write_stats_to_file_from_file(source_path, target_path):
    source = open(source_path, 'r')
    lines = source.readlines()

    count_lines = 0
    count_word = 0
    word_box = {}

    for line in lines:
        count_lines = count_lines + 1
        words = line.split()
        count_word = count_word + len(words)
        for word in words:
            if word in word_box.keys():
                word_box[word] = word_box[word] + 1
            else:
                word_box[word] = 1

    sorted_word_box_by_value = sorted(word_box.items(), key=lambda dic: dic[1], reverse=True)
    most_used_word = sorted_word_box_by_value[0][0]
    most_used_word_count = sorted_word_box_by_value[0][1]

    print("lines: " + str(count_lines))
    print("words: " + str(count_word))

    target = open(target_path, "w")

    target.write("lines: " + str(count_lines) + "\n")
    target.write("words: " + str(count_word) + "\n")
    target.write("most used word is : " + "\"" + most_used_word + "\"" + " with "
                 + str(most_used_word_count) + " occurries" + "\n")


# -----------------------------------------------------------------------------------------------------------------------
# Activity 2 - Parse a file to produce a list¶
# You will be using the file gps.csv located in the data folder for this activity.
# Parse the file and produce a list of coordinates (lat and lon) along with the unix timestamp of their visit.

class Cordination:

    def __init__(self, lat, long, time):
        self.lat = lat
        self.long = long
        self.time = time

    def __str__(self):
        return f"lat : {self.lat}, long : {self.long}, time : {self.time} "

    def __repr__(self):
        return str(self)


def get_coordinates_from_csv(source_path):
    list = []
    with open(source_path, "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader, None)  # skip header

        for line in csv_reader:
            lat = line[2]
            long = line[3]
            time = line[15]
            c = Cordination(lat, long, time)
            list.append(c)

        print(list)


# -----------------------------------------------------------------------------------------------------------------------
# Activity 3¶
# 1) Create an array of 5 values between 5 to 10 and remove 1,2,4 index value from the array.
# 2) Create an empty array having 10 values and assign half values as 10 and half of them as 20.
# 3) Write a function that takes as input a 2-D ndarray and scale the last row and column by 2.5.

def activity3_1():
    array1 = np.array([5, 6, 7, 8, 9])
    updated_array1 = np.delete(array1, [1, 2, 4])
    print(array1)
    print(updated_array1)


def activity3_2():
    array = np.zeros(10)

    array[0: (int(len(array) / 2))] = 10
    array[int((len(array) / 2)): len(array)] = 20
    print(array)


def activity3_3():
    array = np.array([[1, 2, 3, 4, 5], [5, 7, 8, 9, 10], [11, 12, 13, 14, 15]], dtype=float)

    n = array.shape[0]
    m = array.shape[1]

    array[0][4] *= 2.5
    array[1][4] *= 2.5
    array[2] *= 2.5

    print(array)


# -----------------------------------------------------------------------------------------------------------------------
# Activity 4¶
# Write a function that takes a matrix as input and subtract the mean of each row of a matrix.
# Write a function to find the most frequent value in an array.
# Write a function which creates an n×n array with (i,j) entry equal to i+j

def subtract_from_matrix(matrix, sub):
    arr = np.array(matrix)
    return arr - sub


def find_most_frequent(array):
    box = {}
    for x in array:
        if x in box.keys():
            box[x] = box[x] + 1
        else:
            box[x] = 1
    sorted_box = sorted(box.items(), key=lambda dic: dic[1], reverse=True)
    print("most frequent number : " + str(sorted_box[0][0]))


def create_nxn_array(n):
    arr = np.zeros(shape=[n, n], dtype=float)
    for i in range(0, n):
        for j in range(0, n):
            arr[i][j] = i * j
            # print(arr[i][j])

    print(arr)


# -----------------------------------------------------------------------------------------------------------------------
# Activity 5
# Using the ‘titanic_data_sample' using pandas.
# 1. Find and print top 5 and bottom 5 rows from the data.
# 2. Find the descriptive statistics of age and fare of all passengers.
# 3. Extract passengers who age is below 25 and have survived.
# 4. Extract the number of Female Passengers over 25 and in 1st class.

def find_top_and_bottom_5(source_path):
    df = pd.read_csv(source_path)
    print(df.head(5))
    print(df.tail(5))

def find_age_and_fare(source_path):
    df = pd.read_csv(source_path)
    print(df.columns)
    print(df[["Age","Fare"]])

def find_survived_with_age(source_path,age):
    df = pd.read_csv(source_path)
    result = df.loc[ (df["Age"]<=age) & (df["Survived"]==1) ]
    print(result)

def find_activity5_4(source_path,age):
    df = pd.read_csv(source_path)
    #print(df[["Sex","Age","Pclass"]])
    result = df.loc[(df["Age"] >= age) & (df["Sex"] == "female") & (df["Pclass"]==1)]
    print(result)



