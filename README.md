# Usage of vali.py
A script that automatically creates `n` folds of the provided `.db` file and
validated several types of **GOR**.

```py
vali.py --id run_cb513_TESTTTTT --gor 1 3 4 --folds 4 --ali --db validation/cb513.db
```

- `--id`: name of validation run
- `--gor`: gor types
- `--folds`: number of folds
- `--ali`: gor V switch
- `--db`: path to db file


