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

    df = pd.read_excel('assignment4\CalgaryDogBreeds.xlsx')
    breedsArray = df['Breed'].unique()
    df_ind = df.set_index(['Breed', 'Year', 'Month']) 
    df_ind.sort_index()

    def getDogData(df, dogName):
        return df.loc[[dogName]]
    
    def getTotalByBreed(df, dogName):
        df = df.loc[[dogName]].reset_index()
        return df['Total'].sum()
    
    def getTopBreedStat(df, year):
        df = df.groupby(level = ['Breed','Year'])['Total'].sum().reset_index(name = 'Total Licenses')
        df = df[df['Year'] == year]
        totalLicenses = df['Total Licenses'].sum()
        df['Percent of Total'] = df.apply(lambda x: x['Total Licenses']/totalLicenses * 100, axis = 1)
        
        print(totalLicenses)


        return df
    

    print(getTopBreedStat(df_ind, 2021))
    # print(df['Breed'].unique())


    print("ENSF 692 Dogs of Calgary")

    # User input stage

    # Data anaylsis stage

if __name__ == '__main__':
    main()
