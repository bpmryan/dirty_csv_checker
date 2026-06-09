# dirty_csv_checker

This is way for me to learn how to do tests in python.

Data pipeline workflows must actively defend internal schemas against external structural anomalies. This
micro-project configures a filter engine to detect, parse, and isolate records violating defined data invariants
cleanly using `pandas` and `pytest` .


**Terminal Commands**

`
pytest -v
`

`
pytest --cov=clean_engine --cov-report=term-missing
`