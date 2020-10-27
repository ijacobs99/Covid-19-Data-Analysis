"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
========================================================================================================================
Name: Isabel Jacobs
========================================================================================================================
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

#pandas is a library included with Anaconda. It's great for manipulating csv files as "dataframes".
import pandas as pd

#Here we are reading the csv file "covidtesting_cs2120-snippet.csv" into a dataframe called "covid19_data"
covid19_data = pd.read_csv('/Users/isabeljacobs/Documents/Personal Projects/Covid-19-Data-Analysis/covid data initial.csv')

#Uncomment the line below to print the csv contents
#print(covid19_data)

"""
This function finds the daily increase of cases in a dataframe and returns a list with all of these increases.
i.e. for "Confirmed_Negative-Cumulative" as an input column, it should return a list where each subsequent
entry is equal to the number of "new" confirmed negative cases for that corresponding day.
"""
def get_daily_increase(dataframe, col_name):
    #In the lines below we are creating a list called "daily_increase" and adding an initial value to the list
    daily_increase = []
    daily_increase.append(dataframe.iloc[0][col_name])

    #This loops through the column, finding all of the daily increases
    for i in range(len(dataframe[col_name])-1):
        # Uncomment the line below to see how many iterations are in the loop
        #print(i)

        daily_increase.append(dataframe.iloc[i+1][col_name] - dataframe.iloc[i][col_name])

    # Uncomment the line below to see what daily_increase looks like
    print(daily_increase)

    return daily_increase


"""
This function finds the cumulative increase of cases in a dataframe and returns a list with all of those increases.
i.e. for "Confirmed_Positive-Daily" as an input column, it should return a list where the entry for a particular day
is equal to the sum of all previous daily entries (# of cases) + the current daily entry (# of cases).
"""
def get_cumulative_increase(dataframe, col_name):
    cumulative_increase = []
    cumulative_increase.append(0)

    # This loops through the column, adding all of the increases (cumulative) to the list
    for i in range(0,len(dataframe[col_name])):
        
        cumulative_increase.append(cumulative_increase[i]+dataframe.iloc[i][col_name])

    cumulative_increase.pop(0)
    #Uncomment the line below to see what cumulative_increase looks like
    print(cumulative_increase)

    return cumulative_increase

"""
This function returns the overall number of cases for 2 cumulative case lists (i.e. Confirmed_Positive-Cumulative and
Confirmed_Negative-Cumulative).
"""
def total_cumulative_count(cumulative_list1, cumulative_list2):
    total_cumulative_count = cumulative_list1[len(cumulative_list1)-1] + cumulative_list2[len(cumulative_list2)-1]
    return total_cumulative_count

"""
This function adds a list (i.e. the output of cumulative_increase) to a dataframe. You can use this
function to call cumulative_increase and add the returned list to your covid19_data dataframe.
"""
def add_column_to_dataframe(dataframe, column_name, column_list):
    dataframe[column_name] = column_list

"""
This function returns the maximum value of a list.
"""
def get_max_of_list(list):
    return max(list)

"""
This function returns a dataframe column as a list.
"""
def convert_df_column_to_list(dataframe, column_name):
    return dataframe[column_name].tolist()

"""
This function exports a dataframe to a specific csv file named "a1_submission.csv". Include this csv file in your submission.
"""
def export_dataframe_to_csv(dataframe):
    dataframe.to_csv("a1_submission.csv",index=False)

#----------------------------------------------------------------------------------------------------------

print("get_daily_increase function output:")
dailyIncreaseList = get_daily_increase(covid19_data, "Confirmed_Negative-Cumulative")
print("get_cumulative_increase function output:")
cumulativeIncreaselist = get_cumulative_increase(covid19_data, "Confirmed_Positive-Daily")

print("Confirmed Negative Daily and Confirmed Positive Cumulative lists added to dataframe:")
add_column_to_dataframe(covid19_data, "Confirmed_Negative-Daily", dailyIncreaseList)
add_column_to_dataframe(covid19_data, "Confirmed_Positive-Cumulative", cumulativeIncreaselist)
print(covid19_data)

max_val = get_max_of_list(covid19_data["Confirmed_Positive-Daily"])
print("Maximum increase of the Positive Daily column is: ", max_val )
export_dataframe_to_csv(covid19_data)
