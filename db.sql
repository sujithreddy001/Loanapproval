CREATE TABLE loan_applications (
    id SERIAL PRIMARY KEY,
    applicant_name VARCHAR(100),
    credit_score INTEGER,
    loan_amount DECIMAL,
    loan_purpose VARCHAR(255),
    income DECIMAL,
    employment_status VARCHAR(50),
    status VARCHAR(20) DEFAULT 'Pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
