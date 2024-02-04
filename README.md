### Loan Approval Prediction Project
This project aims to analyze and predict the likelihood of loan approval based on various financial and personal information using machine learning techniques.

### Data:

The project utilizes a loan application dataset containing features such as applicant demographics, income, asset values, and cibil score. The target variable is the loan approval status (Approved/Rejected).

### Analysis:

A comprehensive exploratory data analysis (EDA) was conducted to understand the data's characteristics, relationships between features, and potential patterns related to loan approval. Univariate, bivariate, and multivariate analyses were performed, including statistical tests and visualizations.

### Modeling:

Several machine learning models were trained and evaluated to predict loan approval, including logistic regression, and gradient boosting. Cross-validation techniques were used to ensure model generalizability and avoid overfitting. The best-performing model was selected based on metrics: F1-score.

### Deployment:

To demonstrate the model's usage, a simple deployment on a local machine was developed. Users can input new loan application details, and the model predicts the likelihood of approval along with the confidence score.

Screenshots:

Screenshot 1: Shows the interface where users can enter loan application information.
![image](https://github.com/Chitwan54/Loan_Status_Prediction/assets/69714874/c3d7441f-400b-4f87-ad94-a12830b56ea4)

Screenshot 2: Displays the predicted loan approval status.
![image](https://github.com/Chitwan54/Loan_Status_Prediction/assets/69714874/9a45b199-3148-4fb0-873a-5df7c86f7f07)

### Future Work:

**Multivariate Analysis:**
Investigating the relationship between 'employment_type,' 'income_annum,' and 'loan_status' to discern patterns among different employment categories. This could provide insights into the financial stability and reliability of various employment types in loan approval.
Exploring interactions between 'education,' 'employment_type,' and 'cibil_score' to understand how educational qualifications may influence employment types and credit scores, which, in turn, impact loan approval.

**Feature Engineering:**
Creating new features or transforming existing ones to capture complex relationships. For instance, deriving a debt-to-income ratio by combining 'loan_amount' and 'income_annum' might offer a more nuanced understanding of an applicant's financial health.

**Advanced Statistical Testing:**
Conducting more advanced statistical tests such as two-way ANOVA or chi-squared tests for independence to unveil hidden relationships among multiple categorical variables.

**Feature Importance and Impact:**
Analyzing feature importance and impact on model predictions to understand which variables significantly influence the loan approval decision. This insight aids in better interpretability and trustworthiness of the model.

**Predictive Analytics on Customer Segmentation:**
Leveraging clustering techniques to segment customers based on their financial profiles and analyzing how these segments correlate with loan approval. This could provide valuable insights for targeted marketing strategies or personalized financial products.Implement the model in a scalable production environment for real-world loan assessment.

**Web Application:**
Develop a user-friendly web application for loan approval prediction.
