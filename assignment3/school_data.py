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
school_codes = dict()




# You may add your own additional classes, functions, variables, etc.

def get_school_codes():
    
    school_codes_dict = dict()

    with open('assignment3/Assignment3Data.csv', newline='') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
                continue
            elif row[2] not in school_codes:
                school_codes_dict[row[2]] = row[1]
                line_count += 1
        
    return school_codes_dict


def main():
    
    school_codes = get_school_codes()
    print(school_codes)
    print(year_2013)

    # print("ENSF 692 School Enrollment Statistics")

    # # Print Stage 1 requirements here

    # # Prompt for user input

    # # Print Stage 2 requirements here
    # print("\n***Requested School Statistics***\n")

    # # Print Stage 3 requirements here
    # print("\n***General Statistics for All Schools***\n")


if __name__ == '__main__':
    main()

