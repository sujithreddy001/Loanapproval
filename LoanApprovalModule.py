class LoanApprovalModule:
    @staticmethod
    def approve_loan(application_data):
        # Implementation of loan approval logic based on application_data
        if 'credit_score' not in application_data or 'loan_amount' not in application_data:
            return 'Invalid Data'
        
        credit_score = application_data['credit_score']
        loan_amount = application_data['loan_amount']
        
        # Additional logic based on application_data
        
        if credit_score > 700 and loan_amount< 100000: 
            return 'Approved'
        else:
            return 'Rejected'
