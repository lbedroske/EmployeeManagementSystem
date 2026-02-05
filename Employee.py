#Employee class

class Employee:
    """Represents a single employee with basic identifying information."""

    #initialize employee attributes
    def __init__(self, name, id_number, department, job_title):
        self.__name = name
        self.__id_number = id_number
        self.__department = department
        self.__job_title = job_title

    #set employee name
    def set_name(self, name):
        self.__name = name

    #set employee ID number
    def set_id_number(self, id_number):
        self.__id_number = id_number

    #set employee department
    def set_department(self, department):
        self.__department = department

    #set employee job title
    def set_job_title(self, job_title):
        self.__job_title = job_title

    #get employee name
    def get_name(self):
        return self.__name

    #get employee ID number
    def get_id_number(self):
        return self.__id_number

    #get employee department
    def get_department(self):
        return self.__department

    #get employee job title
    def get_job_title(self):
        return self.__job_title

    def __str__(self):
        """Return a formatted string representation of the employee."""
        return (
            f"Name: {self.__name}\n"
            f"ID: {self.__id_number}\n"
            f"Department: {self.__department}\n"
            f"Job Title: {self.__job_title}"
        )