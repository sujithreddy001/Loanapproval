# TestLoanApproval.py

import unittest
from LoanApprovalModule import LoanApprovalModule

class TestLoanApproval(unittest.TestCase):
    def test_approve_loan_approved(self):
        # Test loan approval logic with mock loan application data for approval
        application_data = {
            'credit_score': 750,
            'loan_amount': 10000,
            'purpose': 'Home improvement',
            'employment_status': 'Employed'
        }
        result = LoanApprovalModule.approve_loan(application_data)
        self.assertEqual(result, 'Approved')

    def test_approve_loan_rejected(self):
        # Test loan approval logic with mock loan application data for rejection
        application_data = {
            'credit_score': 600,
            'loan_amount': 5000,
            'purpose': 'Education',
            'employment_status': 'Unemployed'
        }
        result = LoanApprovalModule.approve_loan(application_data)
        self.assertEqual(result, 'Rejected')

    def test_approve_loan_invalid_data(self):
        # Test loan approval logic with invalid loan application data
        application_data = {}  # Missing required fields
        result = LoanApprovalModule.approve_loan(application_data)
        self.assertEqual(result, 'Invalid Data')

if __name__ == '__main__':
    unittest.main()
