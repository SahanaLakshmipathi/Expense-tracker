from Employee import EmployeeDetails
from ExpenseTracker import main, add_expense, save_expense
import unittest
from unittest.mock import patch, mock_open

import os

#valid test case results
class TestEmployeeExpenseTracker(unittest.TestCase):
    @patch('builtins.input', side_effect=['ABC', '321', '100', '1'])
    def test_add_expense_valid(self, mock_input):
        expense = add_expense()
        self.assertEqual(expense.name, 'ABC')
        self.assertEqual(expense.employee_ID, '321')
        self.assertEqual(expense.amount, 100)
        self.assertEqual(expense.category, 'Travel')

#invalid test case results
    @patch('builtins.input', side_effect=['ABC', '321', '100','9', '1'])
    def test_add_expense_invalid_category(self, mock_input):
        expense = add_expense()
        self.assertEqual(expense.name, 'ABC')
        self.assertEqual(expense.employee_ID, '321')
        self.assertEqual(expense.amount, 100)
        self.assertEqual(expense.category, 'Travel')


    def test_save_expense(self):
        expense = EmployeeDetails(name='ABC', id='321', category='Travel', amount=100)
        save_expense(expense, 'test_expenses.csv')

        # Check if the file exists after saving
        file_exists = os.path.exists('test_expenses.csv')
        self.assertTrue(file_exists)

        # Optionally, you can delete the temporary file after the test
        # os.remove('test_expenses.csv')

if __name__ == "__main__":
    unittest.main()


