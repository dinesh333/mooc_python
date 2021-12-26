# Programming exercise:
# List of years
# Please write a function named list_years(dates: list) which takes 
# a list of date type objects as its argument. The function should 
# return a new list, which contains the years in the original list 
# in chronological order, from earliest to latest.

def list_years(dates: list) -> list:
    asc_dates = sorted(dates)
    for i, d in enumerate(asc_dates):
        asc_dates[i] = d.year
    return asc_dates