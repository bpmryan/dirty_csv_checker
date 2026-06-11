# dirty_csv_checker

This is way for me to learn how to do tests in python.

A robust, enterprise-inspired data engineering utility designed to ingest raw, unpredictable data files, isolate records violating strict schema constraints, and output predictable, clean artifacts. Fully verified with an automated `pytest` suite.

Data pipeline workflows must actively defend internal schemas against external structural anomalies. This
micro-project configures a filter engine to detect, parse, and isolate records violating defined data invariants
cleanly using `pandas` and `pytest` .


### Prerequisites
Make sure you have Python 3.10+ installed on your system.

### Installation
1. Navigate to the project root directory.
2. Install the required data manipulation dependencies:
   ```bash
   pip install -r requirements.txt

**Terminal Commands**

`
pytest -v
`

`
pytest --cov=code --cov-report=term-missing
`