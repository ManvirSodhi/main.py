import unittest
import logging


class Student(unittest.TestCase):
    logging.basicConfig(filename="data.log", format='%(asctime)s %(message)s', filemode='w')
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    def compare_marks(self, maths, science, history, geo):
        try:
            assert maths > 0
            assert science > 0
            self.assertGreater(maths+science, history+geo, "Maths and Science have more marks.")
            self.assertEqual(maths, science, "Maths and Science have equal marks.")
            self.assertLess(geo, history, "Geography has less marks than History.")
            self.assertNotEqual(science, history, "Science and history marks are not equal.")
            if maths+science+history+geo > 200:
                session_passed = True
            else:
                session_passed = False
            self.assertTrue(session_passed, "You have passed the examination.")
            if maths + science + history + geo > 350:
                distinction = True
            else:
                distinction = False
            self.assertFalse(distinction, "You didn't pass with distinction marks. Good luck for next term.")
        except:
            self.logger.exception("Marks entered are not correct, kindly put greater than zero value.")

    def average_marks(self, marks, students):
        try:
            avg = marks/students
            self.logger.info("The average marks for the student calculated successfully.")
            return avg
        except:
            self.logger.error("Number of students must be greater than zero.")

    def attendance_average(self, days_present, students):
        try:
            assert students > 0
            attendance_avg = days_present/students
            return attendance_avg
        except:
            self.logger.error("Number of students must be greater than 0.")

    def student_absent(self, total_students, present_students):
        try:
            absent_count = total_students - present_students
            assert absent_count >= 0
            return absent_count
        except:
            self.logger.exception("The number of total students should always be higher than present count.")


