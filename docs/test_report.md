

\# Test Report



\## 1. Introduction



This test report documents the basic testing performed for the Application Activity Analytics Dashboard.



The purpose of testing is to verify that the synthetic dataset, Pandas analysis, suspicious activity detection, and Streamlit dashboard work correctly.



\## 2. How to Mark Test Results



After performing each test:



\- Write \*\*PASS\*\* if the expected result is achieved.

\- Write \*\*FAIL\*\* if the expected result is not achieved.

\- Add a short explanation in the Actual Result column.



The tests should be performed using the synthetic dataset only.



\## 3. Test Cases



| Test Case | Expected Result | Actual Result | Status |

|---|---|---|---|

| CSV file loads correctly | The activity log CSV loads without errors. | To be tested | Pending |

| Dashboard starts successfully | Streamlit dashboard opens without errors. | To be tested | Pending |

| Total event count is displayed correctly | Total number of events is displayed correctly. | To be tested | Pending |

| Success/error/failed counts are displayed correctly | The counts for each status are displayed correctly. | To be tested | Pending |

| Error rate is calculated correctly | Error rate is calculated and displayed correctly. | To be tested | Pending |

| Events by module are displayed | Activity counts for each module are displayed. | To be tested | Pending |

| Errors by module are displayed | Error counts for each module are displayed. | To be tested | Pending |

| Average duration by module is displayed | Average duration for each module is displayed. | To be tested | Pending |

| Suspicious activity threshold works correctly | A module with 5 or more errors generates an alert. | To be tested | Pending |

| Dashboard handles the synthetic dataset without crashing | Dashboard loads and displays the dataset without crashing. | To be tested | Pending |



\## 4. Testing Summary



Testing will be completed using the synthetic activity dataset.



The final test status will be updated after running the dashboard and checking the displayed results.



\## 5. Conclusion



The test report provides a basic verification of the project's main functionality, including data loading, metric calculation, visualization, and rule-based suspicious activity detection.

