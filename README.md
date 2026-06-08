# dirty_csv_checker

Data pipeline workflows must actively defend internal schemas against external structural anomalies. This
micro-project configures a filter engine to detect, parse, and isolate records violating defined data invariants
cleanly using `pandas` and `pytest` .