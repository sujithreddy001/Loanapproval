from flask import Flask, request, jsonify
from riskassessment import RiskAssessment

app = Flask(__name__)

@app.route('/submit_loan_application', methods=['POST'])
def submit_loan_application():
    # Extract data from request
    data = request.json
    credit_score = data.get('credit_score')
    dti_ratio = data.get('dti_ratio')
    employment_status = data.get('employment_status')
    purpose = data.get('purpose')

    # Ensure all required fields are provided
    if credit_score is None or dti_ratio is None or employment_status is None or purpose is None:
        return jsonify({'error': 'Missing required fields'}), 400

    # Create a RiskAssessment object
    risk_assessment = RiskAssessment(credit_score, dti_ratio, employment_status, purpose)
    
    # Calculate the risk score
    total_score = risk_assessment.score_calculator()

    # Determine loan approval based on total score
    # Assuming a simple threshold for demonstration
    if total_score >= 75:
        result = "Approved"
    else:
        result = "Rejected"

    # Return the decision
    return jsonify({'result': result, 'total_score': total_score})

@app.route('/')
def index():
    return 'Welcome to my Flask application!'

if __name__ == '__main__':
    app.run(debug=True)
