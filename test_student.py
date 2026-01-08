import unittest
from unittest.mock import patch
import io
import sys
from student import calculate_grade, main


class TestStudentGrade(unittest.TestCase):

    # 🔹 Grade S (90–100) → 3 tests
    def test_grade_S_lower(self):
        self.assertEqual(calculate_grade(90), "S")

    def test_grade_S_middle(self):
        self.assertEqual(calculate_grade(95), "S")

    def test_grade_S_upper(self):
        self.assertEqual(calculate_grade(100), "S")

    # 🔹 Grade A (80–89) → 3 tests
    def test_grade_A_lower(self):
        self.assertEqual(calculate_grade(80), "A")

    def test_grade_A_middle(self):
        self.assertEqual(calculate_grade(85), "A")

    def test_grade_A_upper(self):
        self.assertEqual(calculate_grade(89), "A")

    # 🔹 Grade B (65–79) → 3 tests
    def test_grade_B_lower(self):
        self.assertEqual(calculate_grade(65), "B")

    def test_grade_B_middle(self):
        self.assertEqual(calculate_grade(72), "B")

    def test_grade_B_upper(self):
        self.assertEqual(calculate_grade(79), "B")

    # 🔹 Grade C (50–64) → 3 tests
    def test_grade_C_lower(self):
        self.assertEqual(calculate_grade(50), "C")

    def test_grade_C_middle(self):
        self.assertEqual(calculate_grade(57), "C")

    def test_grade_C_upper(self):
        self.assertEqual(calculate_grade(64), "C")

    # 🔹 Grade D (40–49) → 3 tests
    def test_grade_D_lower(self):
        self.assertEqual(calculate_grade(40), "D")

    def test_grade_D_middle(self):
        self.assertEqual(calculate_grade(45), "D")

    def test_grade_D_upper(self):
        self.assertEqual(calculate_grade(49), "D")

    # 🔹 Grade F (Below 40) → 3 tests
    def test_grade_F_zero(self):
        self.assertEqual(calculate_grade(0), "F")

    def test_grade_F_middle(self):
        self.assertEqual(calculate_grade(25), "F")

    def test_grade_F_upper(self):
        self.assertEqual(calculate_grade(39), "F")

    # 🔹 Test main program using sys.argv
    def test_main_output(self):
        test_args = [
            "Student.py",
            "neha dodamani",
            "ICA",
            "3",
            "85",
            "78",
            "90"
        ]

        with patch.object(sys, 'argv', test_args):
            captured_output = io.StringIO()
            sys.stdout = captured_output

            main()

            sys.stdout = sys.__stdout__
            output = captured_output.getvalue()

            self.assertIn("GRADING CRITERIA", output)
            self.assertIn("STUDENT DETAILS", output)
            self.assertIn("Name       : neha dodamani", output)
            self.assertIn("Department : ICA", output)
            self.assertIn("Semester   : 3", output)
            self.assertIn("Average    : 84.33", output)
            self.assertIn("Grade      : A", output)


if __name__ == "__main__":
    unittest.main()