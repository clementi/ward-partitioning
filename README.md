# ward-partitioning

usage: `python main.py HOUSEHOLDS_FILE [LIMIT] [SEED]`, where:

* `HOUSEHOLDS_FILE` is the path to a CSV file of households.
* `LIMIT` is the partition size limit (optional); default is `99`.
* `SEED` is a random seed for shuffling households before assigning to partitions (optional). Default is whatever the system uses to seed the random number generator. A seed of zero (`0`) disables shuffling, and households are added to groups in the order they appear in the CSV file.
