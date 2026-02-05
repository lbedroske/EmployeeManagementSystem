#imports
import pickle
import Employee  #employee.py must define the employee class

#main program loop
def main():
    employee_dict=load_pickle("employees.dat")  #load saved data if available

    while True:
        display_menu()  #show menu options
        choice=input("Enter your choice (1-5): ").strip()

        if choice=='1':
            lookup(employee_dict)
        elif choice=='2':
            add_employee(employee_dict)
        elif choice=='3':
            change_employee(employee_dict)
        elif choice=='4':
            delete_employee(employee_dict)
        elif choice=='5':
            save_pickle(employee_dict,"employees.dat")  #save before exit
            print("Program saved. Goodbye!")
            break
        else:
            print("Invalid choice. Enter a number from 1 to 5.")

#display menu options
def display_menu():
    print("\n=== Employee Management Menu ===")
    print("1. Look up an employee")
    print("2. Add a new employee")
    print("3. Change an existing employee's details")
    print("4. Delete an employee")
    print("5. Save and Quit")

#load pickled dictionary or return empty one
def load_pickle(filename):
    try:
        with open(filename,"rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        print("No saved data found. Starting with empty dictionary.")
        return {}

#save dictionary to file using pickle
def save_pickle(data_dict,filename="employees.dat"):
    try:
        with open(filename,"wb") as file:
            pickle.dump(data_dict,file)
        print(f"Data successfully saved to {filename}.")
    except Exception as e:
        print(f"Error saving data: {e}")

#look up employee by id
def lookup(employee_dict):
    emp_id=input("\nEnter the employee ID to look up: ").strip()

    if emp_id in employee_dict:
        print("\nEmployee found:")
        print(employee_dict[emp_id])  #uses __str__()
    else:
        print(f"No employee found with ID {emp_id}.")

#add a new employee
def add_employee(employee_dict):
    print("\nFor the new employee, enter the following...")
    name=input("Name: ").strip()
    emp_id=input("ID number: ").strip()
    dept=input("Department: ").strip()
    title=input("Title: ").strip()

    if emp_id in employee_dict:
        print("Employee ID already exists. Use a unique ID.")
    else:
        employee_dict[emp_id]=Employee.Employee(name,emp_id,dept,title)
        print("Employee added.")

#change employee details
def change_employee(employee_dict):
    emp_id=input("\nEnter the employee ID to change: ").strip()

    if emp_id in employee_dict:
        employee=employee_dict[emp_id]

        print("\nEmployee found:")
        print(employee)

        print(f"\nEnter the new values for employee {emp_id}...")
        name=input("Name: ").strip()
        dept=input("Department: ").strip()
        title=input("Title: ").strip()

        employee.set_name(name)
        employee.set_department(dept)
        employee.set_job_title(title)

        print("Employee details updated.")
    else:
        print(f"No employee found with ID {emp_id}.")

#delete an employee
def delete_employee(employee_dict):
    emp_id=input("\nEnter the employee ID to delete: ").strip()

    if emp_id in employee_dict:
        print("\nEmployee found:")
        print(employee_dict[emp_id])

        answer=input("Are you sure you want to delete this employee? (y/n): ").strip().lower()
        if answer=="y":
            employee_dict.pop(emp_id)
            print("Employee deleted.")
        else:
            print("Deletion cancelled.")
    else:
        print(f"No employee found with ID {emp_id}.")

#program entry point
if __name__=="__main__":
    main()
