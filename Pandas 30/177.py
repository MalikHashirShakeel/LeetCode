import pandas as pd

#Find nth heighest salary.
def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    distinct_salaries = employee["salary"].drop_duplicates().sort_values(ascending = False)

    if N > 0 and N <= len(distinct_salaries):
        result = distinct_salaries.iloc[N - 1]

    else:
        result =  None

    return pd.DataFrame({f"getNthHighestSalary({N})": [result]})