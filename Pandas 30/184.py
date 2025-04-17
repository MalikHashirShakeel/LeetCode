import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    df = employee.merge(department, left_on='departmentId', right_on='id', suffixes=('_emp', '_dept'))
    
    max_salary = df.groupby('name_dept')['salary'].transform('max')
    
    highest_paid = df[df['salary'] == max_salary][['name_dept', 'name_emp', 'salary']]
    
    highest_paid.columns = ['Department', 'Employee', 'Salary']
    
    return highest_paid