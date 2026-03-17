import logging

# Configure logging
logging.basicConfig(
    filename='app.log',
    level=logging.ERROR,
    format='%(asctime)s %(levelname)s:%(message)s'
)

def divide_numbers(a, b):
    try:
        with open('input.txt', 'r') as f:
            f.read()
    except FileNotFoundError as e:
        logging.error("File not found: %s", e)
        print("Error: The file was not found.")
    try:
        result = a / b
        return result
    except ZeroDivisionError as e:
        logging.error("Attempted to divide by zero: %s", e)
        print("Error: Cannot divide by zero.")
    except Exception as e:
        logging.error("Unexpected error: %s", e)
        print("An unexpected error occurred.")

if __name__ == "__main__":
    print(divide_numbers(10, 2))   # Should print 5.0
    print(divide_numbers(10, 0))   # Should print error message and log it