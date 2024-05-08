class RiskAssessment:
    def __init__(self, credit_score, dti_ratio, employment_status, purpose):
        self.credit_score = credit_score
        self.dti_ratio = dti_ratio
        self.employment_status = employment_status
        self.purpose = purpose

    def score_calculator(self):
        if self.credit_score >= 800:
            credit_score_points = 100
        elif self.credit_score >= 750:
            credit_score_points = 85
        elif self.credit_score >= 700:
            credit_score_points = 70
        else:
            credit_score_points = 50

        if self.employment_status == 'Employed':
            employment_points = 100
        elif self.employment_status == 'Self-employed':
            employment_points = 80
        else:
            employment_points = 50

        if self.purpose == 'Home improvement':
            purpose_points = 100
        elif self.purpose == 'Education':
            purpose_points = 90
        elif self.purpose == 'Investment':
            purpose_points = 70
        else:
            purpose_points = 60
    # Credit Score: 50%
    # Employment Status: 30%
    # Purpose of the Loan: 20%
        total_score=(credit_score_points * 0.50)+(employment_points * 0.30)+(purpose_points * 0.20)
        return total_score
