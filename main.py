import numpy as np
import lecture3


if __name__ == '__main__':
    dir_path = r'C:/Users/Anwender/PycharmProjects/AppliedDataScienceWithPython/venv/lecture3resources'

    #lecture3.write_stats_to_file_from_file( dir_path + '/bill_of_rights.txt', dir_path + "/stats.txt")
    #lecture3.get_coordinates_from_csv(dir_path + "/gps.csv")
    #lecture3.activity3_1()
    #lecture3.activity3_2()
    #lecture3.activity3_3()

    array = np.array([
        [1, 2, 3, 4, 5],
        [5, 7, 8, 9, 10],
        [11, 12, 13, 14, 15]],
        dtype=float)

    #array = lecture3.subtract_from_matrix(array, 5)
    #print(array)

    #arr = [6, 6, 3, 4, 5, 5, 8, 6, 9, 10, 6, 3, 3, 4]

    #lecture3.find_most_frequent(arr)
    #lecture3.create_nxn_array(10)

    #lecture3.find_top_and_bottom_5(dir_path+"/titanic_data_sample.csv")
    #lecture3.find_age_and_fare(dir_path+"/titanic_data_sample.csv")
    #lecture3.find_survived_with_age(dir_path + "/titanic_data_sample.csv", 25)
    lecture3.find_activity5_4(dir_path + "/titanic_data_sample.csv", 25)
