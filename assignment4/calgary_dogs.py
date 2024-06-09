import pandas as pd

# calgary_dogs.py
# AUTHOR NAME
#
# A terminal-based application for computing and printing statistics based on given input.
# Detailed specifications are provided via the Assignment 4 README file.
# You must include the main listed below. You may add your own additional classes, functions, variables, etc. 
# You may import any modules from the standard Python library.
# Remember to include docstrings and comments.


def main():

    # Import data here

    df = pd.read_excel(r"assignment4\CalgaryDogBreeds.xlsx")
    breedsArray = df['Breed'].unique()
    df_ind = df.set_index(['Breed', 'Year', 'Month']) 
    df_ind.sort_index()

    def get_dog_data(df, dogName):
        return df.loc[[dogName]]
    
    def get_sum_of_licenses_by_breed(df, dogName):
        df = df.loc[[dogName]].reset_index()
        return df['Total'].sum()
    
    def get_percent_of_breed_year(df, dogName, year):
        df = df.groupby(level = ['Breed','Year'])['Total'].sum().reset_index(name = 'Total Licenses')
        df = df[df['Year'] == year]
        totalLicenses = df['Total Licenses'].sum()
        df['Percent of Total'] = df.apply(lambda x: x['Total Licenses']/totalLicenses * 100, axis = 1)
        df = df.reset_index(drop = True)
        df = df[df['Breed'] == dogName]
        
        return df['Percent of Total'].loc[df.index[0]]
    
    def print_total_licenses_of_breed(df, dogName):
        print("There have been", get_sum_of_licenses_by_breed(df_ind, dogName), dogName, "dogs registered in total.")
    
    def print_percent_of_breed_year(df, dogName, year):
        print("The", dogName, "was", "%.6f%%" % get_percent_of_breed_year(df_ind, dogName, year),"of top breeds in", year)

    print("ENSF 692 Dogs of Calgary")
    print_total_licenses_of_breed(df, 'LABRADOR RETR')
    print_percent_of_breed_year(df_ind, 'LABRADOR RETR', 2021)
    print_percent_of_breed_year(df_ind, 'LABRADOR RETR', 2022)
    print_percent_of_breed_year(df_ind, 'LABRADOR RETR', 2023)
    # print(df['Breed'].unique())


    

    # User input stage

    # Data anaylsis stage

if __name__ == '__main__':
    main()
