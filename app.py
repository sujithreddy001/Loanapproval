
from flask import Flask, request, jsonify
from pymongo import MongoClient
from riskassessment import RiskAssessment

app = Flask(__name__)

# Connecting to MongoDB
client = MongoClient('localhost', 27017)
db = client['loanapplication']
collection = db['loan_applications']

# for Log messages
print("Connected to MongoDB")
print("Database 'loanapplication' and collection 'loan_applications' created")

@app.route('/submit_loan_application', methods=['POST'])
def submit_loan_application():
    data = request.json
    credit_score = data.get('credit_score')
    # dti_ratio = data.get('dti_ratio')
    employment_status = data.get('employment_status')
    purpose = data.get('purpose')

    if None in (credit_score, employment_status,purpose):
        return jsonify({'error': 'Missing required fields'}), 400

    risk_assessment = RiskAssessment(credit_score, employment_status,purpose)
    total_score = risk_assessment.score_calculator()

    result = "Approved" if total_score >= 75 else "Rejected"

    # Insert application data into the MongoDB collection
    application_data = {
        'credit_score': credit_score,
        # 'dti_ratio': dti_ratio,
        'employment_status': employment_status,
        'purpose': purpose,
        'total_score': total_score,
        'result': result
    }
    collection.insert_one(application_data)

    return jsonify({'result': result, 'total_score': total_score})

if __name__ == '__main__':
    app.run(debug=True)
