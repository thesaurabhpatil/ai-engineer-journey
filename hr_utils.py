def calculate_tenure(join_year:int, current_year:int=2026) -> int:
    """
    Calculate the tenure of an employee based on their joining year and the current year.

    Args:
        join_year (int): The year the employee joined the company.
        current_year (int): The current year.

    Returns:
        int: The tenure of the employee in years.
    """
    if join_year > current_year:
        raise ValueError("Joining year cannot be in the future.")
    return current_year - join_year

join_year = [2015, 2018, 2020, 2022]
tenures = [calculate_tenure(year) for year in join_year]
print(tenures)

employees = {
    "E01": 2018,
    "E02": 2020,
    "E03": 2016
}
employee_tenures = {emp_id: calculate_tenure(year) for emp_id, year in employees.items()}
print(employee_tenures)

try:
    print(calculate_tenure(2030))
except ValueError as e:
    print("Error:",e)
