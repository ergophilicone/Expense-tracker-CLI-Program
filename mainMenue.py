from userInput import user_input


def main_menu():
    """
      Displays the main menu for the Expense Tracker.

    Usage:
    - Prints the welcome message and menu options.
    - Calls the option_selector function to process the user's choice.
      """
    print("------------------------------------------------\n"
          "------------------------------------------------\n"
          "Welcome To Expense Tracker - Track Efficiently \n"
          "Author : Md Faisal\n"
          "Version Details: Version 1.0 | Saves Data as CSV\n"
          "------------------------------------------------\n"
          "------------------------------------------------\n"
          "1) Make New Entry\n2) View Previous Expenses\n")
    option_selector()


def option_selector():
    """
      Processes the user's choice from the main menu.

    Usage:
    - Takes user input for menu selection.
    - If the user chooses to make a new entry (1), it calls the user_input function.
    - If the user chooses to view previous expenses (2), it calls the view_expenses function.
    - If the user enters an invalid option, prompts for a valid choice.
    """
    option_selector_var = input("Enter your choice: ")
    if option_selector_var == "1":
        user_input()
    elif option_selector_var == "2":
        pass
    else:
        print("Please select from the any two options : ")
        option_selector()
