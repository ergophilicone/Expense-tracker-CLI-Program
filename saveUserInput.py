import csv


def save_to_csv(expense_data, filename='expenses.csv'):
    """
    Saves expense data to a CSV file.

    Args:
    expense_data (dict): Dictionary containing expense details.
    filename (str): Name of the CSV file. Default is 'expenses.csv'.
    """
    with open(filename, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=expense_data.keys())

        # Check if the file is empty, write header if necessary
        if file.tell() == 0:
            writer.writeheader()

        writer.writerow(expense_data)
