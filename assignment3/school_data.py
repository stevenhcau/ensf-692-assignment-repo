# school_data.py
# AUTHOR NAME
#
# A terminal-based application for computing and printing statistics based on given input.
# You must include the main listed below. You may add your own additional classes, functions, variables, etc. 
# You may import any modules from the standard Python library.
# Remember to include docstrings and comments.

import numpy as np
import statistics as stats
import math
import csv
from given_data import year_2013, year_2014, year_2015, year_2016, year_2017, year_2018, year_2019, year_2020, year_2021, year_2022


'''
generateSchoolInfo()

Builder function which returns an array of {school name : school code} key value pairs
'''
def generateSchoolInfo():
    
    school_codes_dict = dict()
    school_names = []

    # Open CSV to grab school names and school codes
    with open('assignment3/Assignment3Data.csv', newline='') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        school_num = 0
        
        school_codes_dict[school_num] = {}
        for row in csv_reader:
            school = row[1]
            # check to see if current item exists in dictionary
            if school not in school_names:
                school_codes_dict[school_num] = {row[2]:row[1]}
                school_names.append(row[1])
                school_num += 1

    return school_codes_dict

'''
cleanSchoolData()

Takes an array containing non-numeric numbers and returns an array containing only numbers
'''
def cleanSchoolData(array):
    return [i if i >= 0 else 0 for i in array]


'''
generateSchoolData()
returns an array with 3 dimensions and shape (20, 10, 3)
'''
def generateSchoolData():
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
                          cleanSchoolData(year_2021.reshape(20,3)[i]),
                          cleanSchoolData(year_2022.reshape(20,3)[i])])
        
        school_data[i] = school
    return school_data

'''
getEnrollment()
takes school, year, and grade as inputs and returns the enrollment
'''
def getEnrollment(school, year, grade = 0):
    return school_data[school][year][grade]

'''
generateSchoolNames()
returns an array containing the school names
'''
def generateSchoolNames():

    school_names = []

    with open('assignment3/Assignment3Data.csv', newline='') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        
        for row in csv_reader:
            if row[1] not in school_names:
                school_names.append(row[1])

    return school_names

'''
generateSchoolCodes()
returns an array containing the school codes
'''
def generateSchoolCodes():

    school_codes = []

    with open('assignment3/Assignment3Data.csv', newline='') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        
        for row in csv_reader:
            if row[2] not in school_codes:
                school_codes.append(row[2])                

    return school_codes

'''
getSchoolInfo(user_input)

takes user input and calls getSchoolStatistics to print out school information
raises ValueError if user_input is invalid
'''
def getSchoolInfo(user_input):
    if user_input in school_codes:
        getSchoolStatistics(school_codes.index(user_input))
    elif user_input in school_names:
        getSchoolStatistics(school_names.index(user_input))
    else:
        raise ValueError

'''
getMeanEnrollment(input_school, grade)

takes input_school, and grade and returns the average enrollment for a particular grade
'''
def getMeanEnrollment(input_school, grade):
    if grade == 10:
        grade = 0
    elif grade == 11:
        grade = 1
    elif grade == 12:
        grade = 2 
    else:
        raise ValueError   
    
    return stats.mean([i[grade] for i in school_data[input_school]])

'''
getHighestBySchoolEnrollment(input_school)

takes 'input_school' and returns the maximum enrollment from the 'input_school' school
'''
def getHighestBySchoolEnrollment(input_school):
    return max(school_data[input_school].flatten())

'''
getLowestBySchoolEnrollment(input_school)

takes 'input_school' and returns the minimum enrollment from the 'input_school' school
'''
def getLowestBySchoolEnrollment(input_school):
    return min(school_data[input_school].flatten())

'''
getTotalTenYearEnrollment(input_school)

takes 'input_school' and returns the total enrollment from 2013-2022
'''
def getTotalTenYearEnrollment(input_school):
    return sum(school_data[input_school].flatten())

'''
getMedianTotalEnrollment(input_school)

takes 'input_school' and returns the median enrollment form 2013-2022
'''
def getMedianTotalEnrollment(input_school):
    school_data[input_school].flatten()
    if all(i >= 0 for i in school_data[input_school].flatten()):
        print('For all enrollments over 500, the median value was:', math.floor(stats.median(school_data[input_school].flatten())))
    else:
        print('No enrollments over 500')
    
'''
getTotalEnrollmentByYear(input_school)

takes 'input_school' and prints out the total enrollment for each year at given 'input_school'
'''
def getTotalEnrollmentByYear(input_school):
    print("Total enrollment for 2013:", sum(school_data[input_school][0]))
    print("Total enrollment for 2014:", sum(school_data[input_school][1]))
    print("Total enrollment for 2015:", sum(school_data[input_school][2]))
    print("Total enrollment for 2016:", sum(school_data[input_school][3]))
    print("Total enrollment for 2017:", sum(school_data[input_school][4]))
    print("Total enrollment for 2018:", sum(school_data[input_school][5]))
    print("Total enrollment for 2019:", sum(school_data[input_school][6]))
    print("Total enrollment for 2020:", sum(school_data[input_school][7]))
    print("Total enrollment for 2021:", sum(school_data[input_school][8]))
    print("Total enrollment for 2022:", sum(school_data[input_school][9]))


'''
getSchoolStatistics(input)

takes 'input' as a valid user input and prints out the required school statistics
'''
def getSchoolStatistics(input):
    print("")
    print("***Requested School Statistics***")
    print("")
    print('School name:', school_names[input])
    print('School code:', school_codes[input])
    print('Mean enrollment for Grade 10:', getMeanEnrollment(input, 10))
    print('Mean enrollment for Grade 11:', getMeanEnrollment(input, 11))
    print('Mean enrollment for Grade 12:', getMeanEnrollment(input, 12))
    getTotalEnrollmentByYear(input)
    print('Max enrollment:', getHighestBySchoolEnrollment(input))
    print('Max enrollment:', getLowestBySchoolEnrollment(input))
    print('Total ten year enrollment:', getTotalTenYearEnrollment(input))
    print('Mean total enrollment over 10 years:', int(math.floor(getTotalTenYearEnrollment(input)/10)))
    getMedianTotalEnrollment(input)

'''
getMeanYearEnrollment(source)

takes 'source' as a 1D numpy.array object of enrollment over a year and returns the average enrollment
'''
def getMeanYearEnrollment(source):
    return int(math.floor(stats.mean(cleanSchoolData(source))))

'''
getMeanYearEnrollment(source)

takes 'source' as a 1D numpy.array object of enrollment over a year and returns the total enrollment
'''
def getTotalAllEnrollment(source):
    return int(np.sum(cleanSchoolData(source)))

'''
getHighestEnrollment()

returns highest enrollment recorded
'''
def getHighestEnrollment():
    all_enrollments = np.concatenate((cleanSchoolData(year_2013),
                                     cleanSchoolData(year_2014),
                                     cleanSchoolData(year_2015),
                                     cleanSchoolData(year_2016),
                                     cleanSchoolData(year_2017),
                                     cleanSchoolData(year_2018),
                                     cleanSchoolData(year_2019),
                                     cleanSchoolData(year_2020),
                                     cleanSchoolData(year_2021),
                                     cleanSchoolData(year_2022)))
    return int(max(all_enrollments))

'''
getLowestEnrollment()

returns lowest enrollment recorded
'''
def getLowestEnrollment():
    all_enrollments = np.concatenate((cleanSchoolData(year_2013),
                                     cleanSchoolData(year_2014),
                                     cleanSchoolData(year_2015),
                                     cleanSchoolData(year_2016),
                                     cleanSchoolData(year_2017),
                                     cleanSchoolData(year_2018),
                                     cleanSchoolData(year_2019),
                                     cleanSchoolData(year_2020),
                                     cleanSchoolData(year_2021),
                                     cleanSchoolData(year_2022)))
    return int(min(all_enrollments))

def getGraduatingClass(input_school):
    return ([i[2] for i in school_data[input_school]])

                                     
# generate variables
school_info = generateSchoolInfo()
school_names = generateSchoolNames()
school_data = generateSchoolData()
school_codes = generateSchoolCodes()

        
# create a function to create the numpy array
# by school, by year, and then fill grades

def main():

    # Print Stage 1 requirements here
    print("Shape of full data array:", np.shape(school_data))
    print("Dimensions of full data array:", np.ndim(school_data))

    # Prompt for user input
    user_input = input("Please enter high school name or school code: ")

    # Print Stage 2 requirements here
    getSchoolInfo(user_input)

    # Print Stage 3 requirements here
    print("\n***General Statistics for All Schools***\n")
    print('Mean enrollment in 2013:', getMeanYearEnrollment(year_2013))
    print('Mean enrollment in 2022:', getMeanYearEnrollment(year_2022))
    print('Total graduating class of 2022 across all schools:', getTotalAllEnrollment(year_2022))
    print('Highest enrollment:', getHighestEnrollment())
    print('Lowest enrollment:', getLowestEnrollment())


if __name__ == '__main__':
    main()

