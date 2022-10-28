import pandas as pd


def showOptions():
    '''Display options'''
    choosing = True
    while choosing:
        print("1 - By Country/Area")
        print("2 - By Users")
        print("3 - By Population")
        print("4 - By Population Rank")
        print("5 - By Percentage of Users")
        print("6 - By Internet Users Rank")
        print("7 - Display Dataset Info")
        print("Q - Exit")
        option = input("How would you like to filter this data? ")
        if option.isalpha() and option.capitalize() == 'Q':
            return option.capitalize()
        elif option.isnumeric() and int(option) > 0 and int(option) < 8:
            return int(option)
        else:
            print("\nPlease enter a valid option.\n")


def getAmount():
    '''Get amount of rows to display'''
    filtering = True
    while filtering:
        rows = input("How many rows of data would you like to see? (1 - 215) ")
        if rows.isnumeric() and int(rows) > 0 and int(rows) < 216:
            filtering = False
        else:
            print("\nPlease enter a valid number.\n")
    return int(rows)


def getDirection():
    '''Get ascending/descending order'''
    ordering = True
    while ordering:
        order = input(
            "Would you like to see Ascending or Descending order? (A/D) ")
        if order.isalpha() and order.capitalize() == "A":
            direction = True
            ordering = False
        elif order.isalpha() and order.capitalize() == "D":
            direction = False
            ordering = False
        else:
            print("\nPlease enter a valid option.\n")
    return direction


# Read the data csv file
data = pd.read_csv("data.csv", usecols=['Country or Area', 'Internet Users',
                   'Population', 'Population Rank', 'User Percentage', 'Internet Users Rank'])

# Create a pandas dataframe
df = pd.DataFrame(data=data)
# Add one to the dataframe index to start with one instead of zero
df.index = df.index + 1

# Prompt user for dataset usage option
researching = True
while researching:
    option = showOptions()
    # Use the Dataset
    if option != 'Q':
        if option != 7:
            amount = getAmount()
            direction = getDirection()
        # Filter by Country/Area
        if option == 1:
            print("\n", df.sort_values("Country or Area",
                                       ascending=direction).head(amount), "\n")
        # Filter by Internet Users
        elif option == 2:
            print("\n", df.sort_values("Internet Users",
                                       ascending=direction).head(amount), "\n")
        # Filter by Population
        elif option == 3:
            print("\n", df.sort_values("Population",
                                       ascending=direction).head(amount), "\n")
        # Filter by Population Rank
        elif option == 4:
            print("\n", df.sort_values("Population Rank",
                                       ascending=direction).head(amount), "\n")
        # Filter by Percentage
        elif option == 5:
            print("\n", df.sort_values("User Percentage",
                                       ascending=direction).head(amount), "\n")
        # Filter by Internet Users Rank
        elif option == 6:
            print("\n", df.sort_values("Internet Users Rank",
                                       ascending=direction).head(amount), "\n")
        elif option == 7:
            # Display Dataframe Information
            print("\n")
            df.info()
            print("\n")
    # Quit the program
    else:
        print("\nSee you later!")
        researching = False
