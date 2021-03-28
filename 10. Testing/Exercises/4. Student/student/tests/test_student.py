import unittest
from project.student import Student


class StudentTests(unittest.TestCase):
    def setUp(self):
        self.student = Student(name='Bogdan', courses={'English': [], 'Deutsch': []})

    def test_student_enroll_if_all_attributes_are_set(self):
        self.assertEqual('Bogdan', self.student.name)
        if not self.student.courses:
            self.assertEqual({}, self.student.courses)
        else:
            self.assertEqual({'English': [], 'Deutsch': []}, self.student.courses)

    def test_student_enroll_if_course_is_already_added(self):
        result = self.student.enroll(course_name='English', notes=['Alphabet'], add_course_notes='')
        self.assertEqual(['Alphabet'], self.student.courses['English'])
        self.assertEqual("Course already added. Notes have been updated.", result)

    def test_student_enroll_if_add_course_notes_equals_Y_or_empty_string(self):
        result = self.student.enroll(course_name='Swedish', notes=['Alphabet'], add_course_notes="")
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual(['Alphabet'], self.student.courses['Swedish'])
        result = self.student.enroll(course_name='Spanish', notes=['Alphabet'], add_course_notes="Y")
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual(['Alphabet'], self.student.courses['Spanish'])

    def test_student_enroll_if_course_is_NOT_added(self):
        result = self.student.enroll(course_name='Spanish', notes=None, add_course_notes="A")
        self.assertEqual("Course has been added.", result)
        self.assertEqual([], self.student.courses['Spanish'])

    def test_student_add_notes_if_course_name_is_in_courses(self):
        result = self.student.add_notes(course_name='Deutsch', notes='Tough language')
        self.assertEqual(['Tough language'], self.student.courses['Deutsch'])
        self.assertEqual("Notes have been updated", result)

    def test_student_add_notes_if_course_name_is_NOT_in_courses(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes(course_name='Spanish', notes='Tough language')
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_student_leave_course_if_course_name_is_in_courses(self):
        result = self.student.leave_course(course_name='Deutsch')
        self.assertTrue('Deutsch' not in self.student.courses)
        self.assertEqual("Course has been removed", result)

    def test_student_leave_course_if_course_name_is_NOT_in_courses(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course(course_name='Spanish')
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))


if __name__ == '__main__':
    if __name__ == '__main__':
        unittest.main()
