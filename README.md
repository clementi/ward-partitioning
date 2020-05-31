# ward-partitioning

usage: `python main.py HOUSEHOLDS_FILE [LIMIT] [SEED]`, where

* `HOUSEHOLDS_FILE` is the path to a CSV file of households
* `LIMIT` is the partition size limit (optional)
* `SEED` is a random seed for shuffling households before assigning to partitions (optional). A seed of zero (`0`) disables shuffling