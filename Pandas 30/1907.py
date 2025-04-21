import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    low_salary = accounts[accounts["income"] < 20000]
    average_salary = accounts[(accounts["income"] >= 20000) & (accounts["income"] <= 50000)]
    high_salary = accounts[accounts["income"] > 50000]

    low_salary_count = low_salary.drop_duplicates(subset = "account_id").shape[0]
    average_salary_count = average_salary.drop_duplicates(subset = "account_id").shape[0]
    high_salary_count = high_salary.drop_duplicates(subset = "account_id").shape[0]

    return pd.DataFrame({
        "category" : ["Low Salary", "Average Salary", "High Salary"],
        "accounts_count" : [low_salary_count, average_salary_count, high_salary_count]
    })