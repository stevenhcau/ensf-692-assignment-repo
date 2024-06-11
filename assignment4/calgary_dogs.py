import pandas as pd

# calgary_dogs.py
# Steven (Han) Au
#
# A terminal-based application for computing and printing statistics based on given input.
# Detailed specifications are provided via the Assignment 4 README file.
# You must include the main listed below. You may add your own additional classes, functions, variables, etc. 
# You may import any modules from the standard Python library.
# Remember to include docstrings and comments.


def main():

    # Import Data from CalgaryDogBreeds.xlsx
    df = pd.read_excel(r'assignment4\CalgaryDogBreeds.xlsx')
    breedsArray = df['Breed'].unique() # build array of breed names to validate user input later
    df_ind = df.set_index(['Breed', 'Year', 'Month']) 
    df_ind.sort_index()

    def get_dog_data(df, dogName):
        """
        Returns a dataframe filtered by a breed

        Parameters
        ----------
        dogName : String
            String of dog breed
        df: pd.DataFrame
            DataFrame of dog breeds and licenses    

        Returns
        -------
        df: pd.DataFrame
            Dataframe filtered by breed
        """
        return df.loc[[dogName]]
    
    def get_sum_of_licenses_by_breed(df, dogName):
        """
        Returns the total number of licenses across all years for a particular breed

        Parameters
        ----------
        dogName : String
            String of dog breed
        df: pd.DataFrame
            DataFrame of dog breeds and licenses

        Returns
        -------
        int
            Total number of licenses across all years for a particular breed
        """       
        df = df.loc[[dogName]].reset_index()
        return df['Total'].sum()
    
    def print_top_years_of_breeds(df, dogName):
        """
        Print the years that a dog breed was found in top breeds

        Parameters
        ----------
        dogName : String
            String of dog breed
        df: pd.DataFrame
            DataFrame of dog breeds and licenses

        Returns
        -------
        None
            Print the years that a dog breed was found in top breeds for years
        """
        df = get_dog_data(df, dogName).reset_index()
        years = df['Year'].unique()
        print('The', dogName, 'was found in top breeds for years: ', end ='')
        print(*years, sep =' ')
    
    def print_top_months_of_breeds(df, dogName):
        """
        Print the most popular months over all years for a particular dog breed given a dog breed input

        Parameters
        ----------
        dogName : String
            String of dog breed
        df: pd.DataFrame
            DataFrame of dog breeds and licenses

        Returns
        -------
        None
            Displays the most popular months over all years for a particular dog breed given a dog breed input in terminal
        """
        df = df.groupby(level = ['Breed','Month'])['Total'].sum().reset_index(name = 'Total Licenses')
        df = df[df['Breed'] == dogName]
        df = df.sort_values(by = 'Total Licenses', ascending = False)
        months = df['Month'].unique()[:9]
        months = sorted(months)
        print('Most popular month(s) for', dogName, 'dogs: ', end ='')
        print(*months, sep = ' ')
    
    def get_percent_of_breed_year(df, dogName, year):
        """
        Displays the percentage of total licenses for a particular dog breed and year

        Parameters
        ----------
        dogName : String
            String of dog breed
        Year: int
            integer of dog breed
        df: pd.DataFrame
            DataFrame of dog breeds and licenses

        Returns
        -------
        float :
            Percentage of total licenses for a particular dog breed and year
        """
        df = df.groupby(level = ['Breed','Year'])['Total'].sum().reset_index(name = 'Total Licenses')
        df = df[df['Year'] == year]
        totalLicenses = df['Total Licenses'].sum()
        df['Percent of Year'] = df.apply(lambda x: x['Total Licenses']/totalLicenses * 100, axis = 1)
        df = df.reset_index(drop = True)
        df = df[df['Breed'] == dogName]

        return df['Percent of Year'].loc[df.index[0]]
    
    def get_total_percent_of_breed_licenses(df, dogName):
        """
        Returns the percentage of breed licenses across all years

        Parameters
        ----------
        dogName : String
            String of dog breed
        df: pd.DataFrame
            DataFrame of dog breeds and licenses

        Returns
        -------
        float :
            Percentage of breed licenses across all years
        """
        df = df.groupby(level = ['Breed'])['Total'].sum().reset_index(name = 'Total Licenses')
        totalLicenses = df['Total Licenses'].sum()
        df['Percent of Licenses'] = df.apply(lambda x: x['Total Licenses']/totalLicenses * 100, axis = 1)
        df = df[df['Breed'] == dogName]

        return df['Percent of Licenses'].loc[df.index[0]]
    
    def print_total_licenses_of_breed(df, dogName):
        """
        Print total of licenses of a particular breed across all years

        Parameters
        ----------
        dogName : String
            String of dog breed
        df: pd.DataFrame
            DataFrame of dog breeds and licenses

        Returns
        -------
        None
            Display total of licenses of a particular breed across all years
        """
        print("There have been", get_sum_of_licenses_by_breed(df_ind, dogName), dogName, "dogs registered in total.")
    
    def print_percent_of_breed_year(df, dogName, year):
        """
        Print total of licenses of a particular breed across all years

        Parameters
        ----------
        dogName : String
            String of dog breed
        df: pd.DataFrame
            DataFrame of dog breeds and licenses

        Returns
        -------
        None
            Display total of licenses of a particular breed across all years
        """
        print("The", dogName, "was", "%.6f%%" % get_percent_of_breed_year(df, dogName, year),"of top breeds in", year, ".")

    def print_total_percent_of_breed_licenses(df, dogName):
        """
        Print percentage of licenses of a particular breed across all years

        Parameters
        ----------
        dogName : String
            String of dog breed
        df: pd.DataFrame
            DataFrame of dog breeds and licenses

        Returns
        -------
        None
            Display percentage of licenses of a particular breed across all years
        """
        print("The", dogName, "was", "%.6f%%" % get_total_percent_of_breed_licenses(df, dogName),"of top breeds across all years.")


    def print_breed_stats(df, dogName):
        """
        Print statistics for a particular breed

        Parameters
        ----------
        dogName : String
            String of dog breed
        df: pd.DataFrame
            DataFrame of dog breeds and licenses

        Returns
        -------
        None
            Displays statistics for a particular breed
        """
        print_top_years_of_breeds(df, dogName)
        print_total_licenses_of_breed(df, dogName)
        print_total_licenses_of_breed(df, dogName)
        print_percent_of_breed_year(df, dogName, 2021)
        print_percent_of_breed_year(df, dogName, 2022)
        print_percent_of_breed_year(df, dogName, 2023)
        print_total_percent_of_breed_licenses(df_ind, dogName)
        print_top_months_of_breeds(df, dogName)
        print("")

    def update_status():
        """
        Gets user input for breed and output stats. Implements input for user input. Requires main variable boolean: check_input.

        Parameters
        ----------
        None

        Returns
        -------
        None
            Displays statistics for a particular breed
        """
        inp = input("Please enter a dog breed: ")
        inp = str.upper(inp)
        if inp in breedsArray:
            print_breed_stats(df_ind, inp)
            check_input = False
        else:
            print('Dog breed was not found in the data. Please try again.\n')


    print("ENSF 692 Dogs of Calgary")

    # User input stage
    check_input = True

    while check_input:
        update_status()

if __name__ == '__main__':
    main()
