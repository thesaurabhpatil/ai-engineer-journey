from datetime import datetime, timedelta

# Create a date object
today = datetime.now()
print(f"Today's date: {today}")

# Create a specific date
specific_date = datetime(2024, 3, 15)
print(f"Specific date: {specific_date}")

# Parse a date from string
date_string = "2024-12-25"
parsed_date = datetime.strptime(date_string, "%Y-%m-%d")
print(f"Parsed date: {parsed_date}")

# Extract month and year
month = today.month
year = today.year
print(f"Month: {month}, Year: {year}")

# Format date as string
formatted_date = today.strftime("%Y-%m-%d")
print(f"Formatted date: {formatted_date}")

# Convert between date formats
iso_format = today.isoformat()
print(f"ISO format: {iso_format}")

# Add/subtract days
tomorrow = today + timedelta(days=1)
next_week = today + timedelta(weeks=1)
print(f"Tomorrow: {tomorrow}")
print(f"Next week: {next_week}")

# Get month and year as tuple
month_year = (today.month, today.year)
print(f"Month-Year tuple: {month_year}")