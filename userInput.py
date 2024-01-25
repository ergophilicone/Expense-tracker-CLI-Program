from saveUserInput import save_to_csv


def user_input():
    """
    Collects user input for expense tracking.

    Returns:
    dict: A dictionary containing validated expense details.

    Details:
    - Expense Amount: The cost of the expense (numerical value).
    - Expense Category: Categorizes the expense from a predefined list.
    - Date of Expense: Date when the expense occurred.
    - Additional Notes (Optional): Optional comments about the expense.

    Usage:
    - The user is prompted to enter expense details interactively.
    - Validates input for Expense Amount and Expense Category.
    - Returns a dictionary with keys: ["Expense Amount", "Expense Category", "Date Of Expense", "Additional Notes"].

    Example:
    Enter Expense Amount: 50.00
    ---------------------------------------
    Select Expense Category From Below List
    ---------------------------------------
    Groceries
    Utilities
    Transportation
    Entertainment
    Dining Out
    Healthcare
    Housing
    Clothing
    Personal Care
    Education
    Gifts and Donations
    Miscellaneous
    Enter Expense Category: Groceries
    Enter Date Of Expense: 2024-01-25
    Enter Additional Notes (Optional): Monthly grocery shopping
    {'Expense Amount': '50.00', 'Expense Category': 'Groceries', 'Date Of Expense': '2024-01-25',
    'Additional Notes': 'Monthly grocery shopping'}
    """
    predefined_expense_list = ["Groceries", "Utilities", "Transportation", "Entertainment", "Dining Out",
                               "Healthcare", "Housing", "Clothing", "Personal Care", "Education",
                               "Gifts and Donations", "Miscellaneous"]

    key_list = ["Expense Category", "Expense Amount", "Date Of Expense(dd-mm-yyyy)", "Additional Notes"]
    value_list = []

    # Input validation functions
    def validate_amount(value_check):
        """
        Validates that the input can be converted to a numerical value.

        Args:
        value (str): The input value.

        Returns:
        bool: True if the input is a valid numerical value, False otherwise.
        """
        try:
            str(value_check)
            return True
        except ValueError:
            print("Invalid input. Please enter a numerical value for Expense Amount.")
            return False

    def validate_category(value_check):
        """
        Validates that the input is a valid expense category.

        Args:
        value (str): The input value.

        Returns:
        bool: True if the input is a valid expense category, False otherwise.
        """
        if value_check in predefined_expense_list:
            return True
        else:
            print("Invalid input. Please choose a category from the predefined list.")
            return False

    def validate_date(value_check):
        """
        Placeholder function for date validation. Add custom date validation logic if needed.

        Args:
        value (str): The input value.

        Returns:
        bool: Always returns True for now.
        """
        # Add your own date validation logic if needed
        return True

    counter = 0
    for key in key_list:
        if counter != 0:
            value = input("Enter " + key + " : ")
            while not validate_amount(value):
                value = input("Enter " + key + " : ")
            counter += 1
            value_list.append(value)
        else:
            print("---------------------------------------\n"
                  "Select Expense Category From Below List\n"
                  "---------------------------------------\n")
            for expense in predefined_expense_list:
                print(expense)
            print("------------------------------------------------\n")
            value = input("Enter " + key + " : ")
            while not validate_category(value):
                value = input("Enter " + key + " : ")
            counter += 1
            value_list.append(value)

    user_inputs_zipped = zip(key_list, value_list)

    save_to_csv(dict(user_inputs_zipped))

    return "New Data Saved !"
