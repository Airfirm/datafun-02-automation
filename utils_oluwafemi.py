"""
File: utils_oluwafemi.py

Purpose: Reusable Module for My Analytics Projects

Description: This module provides a byline for my analytics projects. 
When we work hard to write useful code, we want it to be reusable.
A good byline could be used in every Python analytics project we do.

Author: Oluwafemi Salawu

Date: 2025-05-09
Copyright (c) 2023 Oluwafemi Salawu
"""

#####################################
# Import Modules
#####################################

# Import helpful modules from the Python Standard library
# See more at: https://docs.python.org/3/library/

import statistics


#####################################
# Declare Global Variables
#####################################

# declare a boolean variable (has a value True or False)
# TODO: Add another or replace this with your own boolean variable
had_international_clients: bool = False

# declare an integer variable 
# TODO: Add or replace this with your own integer variable
years_in_operation: int = 7

# declare a floating point variable
# TODO: Add or replace this with your own floating point variable
average_client_satisfaction: float = 5.6

# declare a list of strings
# TODO: Add or replace this with your own list  
skills_required: list = ["Data Analytics Engineer", "BI Developer", "Business Technology Product Manager"]

# declare a list of numbers so we can illustrate statistics skills
# TODO: Add or replace this with your own numeric list  
client_satisfaction_scores: list = [45.5, 54.2, 25.1, 16.9, 70.3]

# Calculate basic statistics using built-in Python functions and the statistics module
# TODO: Replace these variable names with the variable name of your own numeric list
minimum_score: float = min(client_satisfaction_scores)  
maximum_score: float = max(client_satisfaction_scores)  
the_mean_score: float = statistics.mean(client_satisfaction_scores)  
standard_deviation_score: float = statistics.stdev(client_satisfaction_scores)

# Use a Python formatted string (f-string) to show information
# TODO: Modify the text in the byline to fit your information
# TODO: Modify the variables in the byline to use your variable names
byline: str = f"""
---------------------------------------------------------
Data Analytics: Delivering Professional Insights To Foster Decison-Making
---------------------------------------------------------
Ever Had An International Clients:  {had_international_clients}
Number Of Years in Operation:         {years_in_operation}
Skills Required:             {skills_required}
Satisfaction Scores: {client_satisfaction_scores}
Lowest Satisfaction Score: {minimum_score}
Highest Satisfaction Score: {maximum_score}
Mean Score: {the_mean_score:.2f}
Standard Deviation Scores: {standard_deviation_score:.2f}
"""

#####################################
# Define global functions
#####################################

def get_byline() -> str:
    '''
    Get a byline for my analytics projects.
       
    Returns a string byline that illustrates my specific skills.

    A function is a block of code that performs a task.
    This function just returns our byline.
    We can call this (or other functions) in later modules 
    so we can write it once and reuse it. 
    We use a type hint to indicate this function returns a string
    (that is, it has a Python type of str).
    It doesn't need any additional information passed in, 
    so there's nothing needed inside the parentheses.
    Everything after the colon must be indented consistently (usually 4 spaces)
    '''
    return byline

#####################################
# Define main function for this module.
#####################################

def main() -> None:
    '''
    Print results of get_byline() when main() is called.

    This function just prints the byline to the console when we run this as a script.
    The type hint indicates this function doesn't return anything when called 
    (that is, it has a Python type of None).
    It doesn't need any additional information passed in, 
    so there's nothing inside the parentheses.
    Everything after the colon must be indented consistently (usually 4 spaces)
    '''

    print("START main() in utils_oluwafemi.py")
    print(get_byline())
    print("END main() in utils_oluwafemi.py")

#####################################
# Conditional Execution
#####################################

# If we are running this file as a script then call main()
# and verify our code works as expected.

if __name__ == '__main__':
    main()