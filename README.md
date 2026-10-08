Application Activity Analytics Dashboard



Project Overview



The Application Activity Analytics Dashboard is a Streamlit-based cybersecurity and data analytics mini-project. It analyzes synthetic application activity logs using Python and Pandas and displays activity, performance, and unusual activity metrics through an interactive dashboard.



This project uses synthetic data only. No real user data, passwords, personal information, or real application logs are used.



Problem Statement



Application activity logs contain useful information about application performance, errors, failures, and unusual activity. Manually analyzing these logs can be time-consuming.



This project provides a simple dashboard to analyze activity logs and identify potentially suspicious activity using basic rules.



Objectives



\- Analyze application activity logs using Pandas.

\- Calculate activity and performance metrics.

\- Analyze successful, error, and failed events.

\- Calculate error rate.

\- Analyze events and errors by module.

\- Calculate average duration by module.

\- Detect potentially suspicious activity using simple thresholds.

\- Display results through a Streamlit dashboard.



Key Features



\- Total event count

\- Successful event count

\- Error event count

\- Failed event count

\- Error rate

\- Events by module

\- Errors by module

\- Average duration by module

\- Rule-based suspicious activity detection

\- Interactive Streamlit dashboard

\- Synthetic dataset



Technologies Used



\- Python

\- Pandas

\- Streamlit

\- Matplotlib

\- CSV



Project Workflow



Synthetic Activity Logs → Pandas Analysis → Activity \& Performance Metrics → Error \& Duration Analysis → Rule-Based Suspicious Activity Detection → Streamlit Dashboard → Testing \& Documentation



Dataset Description



The project uses a synthetic CSV dataset:



"data/activity\_logs.csv"



The dataset contains the following columns:



\- "timestamp" – Date and time of the activity

\- "module" – Application module

\- "event\_type" – Type of application event

\- "status" – Result of the activity

\- "duration" – Duration of the activity



Possible status values are:



\- "success"

\- "error"

\- "failed"



Suspicious Activity Detection



The project uses a simple rule-based approach.



If a module has 5 or more errors, it crosses the alert threshold and should be reviewed.



This alert does not automatically mean that an attack has occurred. It only indicates activity that may require further investigation.



Project Structure



Application-Activity-Analytics/

│

├── analysis.py

├── app.py

├── data/

│   └── activity\_logs.csv

├── screenshots/

├── requirements.txt

├── test\_report.md

├── threat\_model.md

├── README.md

└── .gitignore



How to Run the Project



Install the required libraries:



pip install -r requirements.txt



Run the Streamlit dashboard:



streamlit run app.py



Open the local URL provided by Streamlit in a web browser.



Security and Ethical Considerations



\- The project uses synthetic data only.

\- No real user information or passwords are collected.

\- No real application logs are used.

\- Suspicious activity detection is rule-based and intended for educational purposes.

\- Alerts are indicators for review, not proof of malicious activity.

\- The project does not demonstrate offensive hacking techniques.



Team Contributions



Aditi – Data Analysis



\- Created the synthetic activity dataset.

\- Developed "analysis.py".

\- Performed Pandas-based analysis.

\- Implemented rule-based suspicious activity detection.



Pratibha – Streamlit Dashboard



\- Developed "app.py".

\- Created the Streamlit dashboard.

\- Displayed activity metrics, charts, logs, and alerts.



Archna – Documentation and Testing



\- Created "README.md".

\- Created "threat\_model.md".

\- Created "test\_report.md".

\- Prepared project documentation.

\- Supported basic testing and reporting.

