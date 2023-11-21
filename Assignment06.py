# ------------------------------------------------------------------------------------------ #
# Title: Assignment06
# Desc: This assignment demonstrates using functions, classes, and parameters
# with structured error handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   Kyle Hayward, 11/21/2023, Completed Script
# ------------------------------------------------------------------------------------------ #

################################################
# -- Import modules -- #
import json

################################################
# -- Defining the program's Data -- #

# Data Constants
MENU: str = """
--------Course Registration Menu--------
 Select from the following menu:
   1. Register a Student for a Course
   2. Show current data
   3. Save data to a file
   4. Exit the program
----------------------------------------
"""

FILE_NAME: str = "Enrollments.json"

# Data variables
menu_choice: str = ""
students: list = []

################################################
# -- Processing the Data -- #


# Defining the file processing class
class FileProcessor:
    """
    A set of processing functions that reads from and writes to JSON files.

    ChaneLog: (Who, When, What)
    Kyle Hayward, 11/21/2023, Created Class
    """

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """ This function opens the JSON file and loads the data into the students list

        ChangeLog: (Who, When, What)
        Kyle Hayward, 11/21/2023, Created Function
        """
        try:
            # Open file in read mode and load data into student list
            file = open(file_name, 'r')
            student_data = json.load(file)
            file.close()
        # Error handling to create a file if it does not exist
        except FileNotFoundError as e:
            print()
            print('*' * 50)
            IO.output_error_messages(message="The file doesn't exist!"
                                             "\nCreating the file."
                                             "\nFile has been created.")
            print('*' * 50)
            # Creates the "Enrollments" JSON file
            file = open(FILE_NAME, 'w')
        # Catch all exception error handling
        except Exception as e:
            IO.output_error_messages(message="There was a non-specific error!",
                                     error=e)
        finally:
            if not file.closed:  # Why this variable reference error?
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """ This function writes student list data to the JSON file and presents data to the user.
            While this function also contains presentation data, it is still largely a File Processing function.

        ChangeLog: (Who, When, What)
        Kyle Hayward, 11/21/2023, Created Function
        """

        try:
            # Open "Enrollments.json" and writes the student list data to it
            file = open(file_name, "w")
            json.dump(student_data, file)
            file.close()

            print()
            print('*' * 50)
            print("The following data is saved: \n")
            # Loops through the students list and prints each row
            for student in student_data:
                print(f'{student["FirstName"]}, '
                      f'{student["LastName"]}, '
                      f'{student["CourseName"]}!')
            print('*' * 50)

        except TypeError as e:
            IO.output_error_messages(message="Please validate the data is in valid JSON format.",
                                     error=e)
        except Exception as e:
            IO.output_error_messages(message="There was a non-specific error",
                                     error=e)
        finally:
            if not file.closed:
                file.close()


################################################
# -- Present the Data (Input/Output) --#


# Defining the presentation input/output class
class IO:
    """
    A set of presentation functions that manages user input and output

    ChangeLog: (Who, When, What)
    Kyle Hayward, 11/21/2023, Created CLass
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ This function displays the custom error message to the user

        ChangeLog: (Who, When, What)
        Kyle Hayward, 11/21/2023, Created Function
        :return: None
        """

        print(message, end="\n\n")
        if error is not None:
            print("Technical Error Message")
            print(error,
                  error.__doc__,
                  type(error),
                  sep="\n")

    @staticmethod
    def output_menu(menu: str):
        """ This function displays a menu of options to the user

        ChangeLog: (Who, When, What)
        Kyle Hayward, 11/21/2023, Created Function

        :return: None
        """

        print()
        print(menu)
        print()

    @staticmethod
    def input_menu_choice():
        """ This function receives the menu selection from the user

        ChangeLog: (Who, When, What)
        Kyle Hayward, 11/21/2023, Created Function

        :return: A string with the users menu selection
        """

        choice = "0"
        try:
            print('*' * 50)
            choice = input("Enter your menu selection: ")
            print('*' * 50)
            if choice not in ("1", "2", "3", "4"):
                raise Exception("Please choose menu option 1, 2, 3, or 4.")
        except Exception as e:
            IO.output_error_messages(e.__str__())

        return choice

    @staticmethod
    def output_student_data(student_data: list):
        """ This function displays all data contained in the students list

        ChangeLog: (Who, When, What)
        Kyle Hayward, 11/21/2016, Created Function

        :return: None
        """

        if not student_data:
            print()
            print('*' * 50)
            print("There is currently no data to display.")
            print("Please choose menu option 1 to enter data.")
            print('*' * 50)
        else:
            print()
            print('*' * 50)
            print("The current data is: \n")
            for student in student_data:
                print(f'{student["FirstName"]}, '
                      f'{student["LastName"]}, '
                      f'{student["CourseName"]}')
            print('*' * 50)

    @staticmethod
    def input_student_data(student_data: list):
        """ This function prompts for and stores student's first name, last name and course data

        ChangeLog: (Who, When, What)
        Kyle Hayward, 11/21/2023, Created function

        :return: None
        """

        try:
            # Prompt the user for input
            print()
            print('*' * 50)
            student_first_name = input("Please enter the student's first name: ")
            # Validate first name contains letters only
            if not student_first_name.isalpha():
                raise ValueError("\nThe first name should only contain letters!")

            student_last_name = input("Please enter the student's last name: ")
            # Validate last name contains letters only
            if not student_last_name.isalpha():
                raise ValueError("\nThe last name should only contain letters!")

            course_name = input("Please enter the course name: ")
            print('*' * 50)
            # Validate user does not leave course name blank
            if not course_name:
                raise ValueError("\nYou did not enter any course information!")

            # Adding data to the dictionary
            student = {"FirstName": student_first_name,
                       "LastName": student_last_name,
                       "CourseName": course_name}
            # Appending dictionary data to the student list
            student_data.append(student)

            print()
            print('*' * 50)
            print()
            print(f'You have registered '
                  f'{student["FirstName"]} '
                  f'{student["LastName"]} for '
                  f'{student["CourseName"]}!\n')
            print('*' * 50)

        except ValueError as e:
            IO.output_error_messages(message="That is not the correct type of data!",
                                     error=e)
        except Exception as e:
            IO.output_error_messages(message="There was a non-specific error!",
                                     error=e)
        return student_data

# End of function definitions

################################################
# -- Main body of the script --#


students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

while True:
    IO.output_menu(menu=MENU)

    menu_choice = IO.input_menu_choice()

    if menu_choice == "1":
        IO.input_student_data(student_data=students)
        continue

    elif menu_choice == "2":
        IO.output_student_data(student_data=students)
        continue

    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue

    elif menu_choice == "4":
        break

print()
print('*' * 50)
print("The program has exited!")
print('*' * 50)
