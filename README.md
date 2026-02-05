# Employee Management System

This program is a simple employee management system written in Python. It uses an `Employee` class to store information about each employee and a dictionary to keep track of all employee records. Employee data is saved using Python's `pickle` module so the information is preserved between program runs.

The system allows the user to:
- Look up an employee by ID
- Add a new employee
- Change an existing employee's details
- Delete an employee
- Save all changes before exiting

---

## How It Works

### Employee Class
The `Employee` class stores four pieces of information:
- name
- id number
- department
- job title

It includes getter and setter methods for each attribute, along with a `__str__()` method so employee objects print in a readable format.

### Data Storage
Employee objects are stored in a dictionary where:
- the key is the employee ID
- the value is the `Employee` object

The dictionary is saved to a file named `employees.dat` using `pickle`.

### Program Flow
The program runs in a loop and displays a menu with five options. Each option calls a function that performs the requested action.

---

## File Structure
```
EmployeeManagementSystem/
│
├── employee_management.py     # main program
├── Employee.py                # employee class definition
└── employees.dat              # saved employee data (created automatically)
```

---

## Running the Program

1. Make sure `Employee.py` and the main program file are in the same folder.
2. Run the main program:
```bash
   python employee_management.py
```
3. Use the menu to add, look up, change, or delete employees.
4. Choose **Save and Quit** to write all changes to `employees.dat`.

---

## Example Output
```
=== Employee Management Menu ===
1. Look up an employee
2. Add a new employee
3. Change an existing employee's details
4. Delete an employee
5. Save and Quit

Enter your choice (1-5): 2

For the new employee, enter the following...
Name: John Smith
ID number: 123
Department: Sales
Title: Manager

Employee added.
```

---

## Skills Demonstrated

- Object-oriented programming
- Class design and encapsulation
- Persistent data storage with pickle
- Dictionary-based data management
- Menu-driven program structure
- Clean, readable code organization

---

## Notes

- The program automatically creates `employees.dat` if it does not exist.
- Employee IDs must be unique.
- All user-facing messages begin with capital letters for readability.
