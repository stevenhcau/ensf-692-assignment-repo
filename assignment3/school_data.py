# school_data.py
# AUTHOR NAME
#
# A terminal-based application for computing and printing statistics based on given input.
# You must include the main listed below. You may add your own additional classes, functions, variables, etc. 
# You may import any modules from the standard Python library.
# Remember to include docstrings and comments.

import numpy as np
import csv
from given_data import year_2013, year_2014, year_2015, year_2016, year_2017, year_2018, year_2019, year_2020, year_2021, year_2022

# Declare any global variables needed to store the data here

# builder function
def get_school_codes():
    
    school_codes_dict = dict()
    school_names = []

    with open('assignment3/Assignment3Data.csv', newline='') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        school_num = 0
        
        school_codes_dict[school_num] = {}
        for row in csv_reader:
            school = row[1]
            if school not in school_names:
                school_codes_dict[school_num] = {row[2]:row[1]}
                school_names.append(row[1])
                school_num += 1

    return school_codes_dict

school_codes = get_school_codes()



# You may add your own additional classes, functions, variables, etc.


def generate_school_data():

    school_data = np.empty((20, 10, 3), 'int')

    for i in range(20):

        school = np.array([year_2013.reshape(20,3)[i],
                          year_2014.reshape(20,3)[i],
                          year_2015.reshape(20,3)[i],
                          year_2016.reshape(20,3)[i],
                          year_2017.reshape(20,3)[i],
                          year_2018.reshape(20,3)[i],
                          year_2019.reshape(20,3)[i],
                          year_2020.reshape(20,3)[i],
                          year_2021.reshape(20,3)[i],
                          year_2022.reshape(20,3)[i]])
        
        school_data[i] = school

    print(school_data)
        


    

    # data = np.array[year_2013.reshape(20,3), 
    #                 year_2014.reshape(20,3), 
    #                 year_2015.reshape(20,3), 
    #                 year_2016.reshape(20,3), 
    #                 year_2017.reshape(20,3), 
    #                 year_2018.reshape(20,3), 
    #                 year_2019.reshape(20,3), 
    #                 year_2020.reshape(20,3), 
    #                 year_2021.reshape(20,3), 
    #                 year_2022.reshape(20,3)]

    # return data

# create a function to create the numpy array
# by school, by year, and then fill grades



def main():

    school_codes = get_school_codes()
    generate_school_data()


    # print("ENSF 692 School Enrollment Statistics")

    # # Print Stage 1 requirements here

    # # Prompt for user input

    # # Print Stage 2 requirements here
    # print("\n***Requested School Statistics***\n")

    # # Print Stage 3 requirements here
    # print("\n***General Statistics for All Schools***\n")


if __name__ == '__main__':
    main()

