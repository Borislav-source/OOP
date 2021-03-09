from project.employee import Employee
from project.person import Person


class Teacher(Employee, Person):

    @staticmethod
    def teach():
        return 'teaching...'
