# Fiddup

**Fi**le **D**e**Dup**licator

Small tool to quickly scan a directory for files of similar names.
Useful to scan through archives of books, documents, downloads, movies, music, ...

Outputs the original filename, the compared filename, and similarity.
Only outputs above a specified similarity are stored.

## Installation

### From PyPi

`pip3 install fiddup`

### From Sauce
* `git pull https://github.com/jarviscodes/fiddup`

* `setup.py install`

## Usage
```
Usage: python -m fiddup [OPTIONS]

Options:
  -i, --inpath TEXT      [required]
  -a, --analyze BOOLEAN
  -t, --threshold FLOAT
  -e, --extensions TEXT  [required]
  -d, --directory
  -v, --verbose
  --help                 Show this message and exit.

```

## Example output

```
(env) E:\Users\Jarvis\PycharmProjects\fiddup>python -m fiddup -i C:\Temp -e mp4 -d -v
[Info] Starting with analyze: True
[Info] Starting with match threshold: 0.7
[Info] Scanning for extensions: mp4
[Info] Found 7 directories.
[Info] Found 0 files.
|###################################| 7/7 [100%] in 0.0s (248.30/s)
 Results────────────────┬───────────────────────┬────────────
│ Name                  │ Compared to           │ Similarity │
│ New folder            │ New folder - Copy     │       0.74 │
│ New folder - Copy     │ New folder - Copy (2) │       0.89 │
│ New folder - Copy     │ New folder - Copy (3) │       0.89 │
│ New folder - Copy     │ New folder - Copy (4) │       0.89 │
│ New folder - Copy     │ New folder - Copy (5) │       0.89 │
│ New folder - Copy     │ New folder - Copy (6) │       0.89 │
│ New folder - Copy (2) │ New folder - Copy (3) │       0.95 │
│ New folder - Copy (2) │ New folder - Copy (4) │       0.95 │
│ New folder - Copy (2) │ New folder - Copy (5) │       0.95 │
│ New folder - Copy (2) │ New folder - Copy (6) │       0.95 │
│ New folder - Copy (3) │ New folder - Copy (4) │       0.95 │
│ New folder - Copy (3) │ New folder - Copy (5) │       0.95 │
│ New folder - Copy (3) │ New folder - Copy (6) │       0.95 │
│ New folder - Copy (4) │ New folder - Copy (5) │       0.95 │
│ New folder - Copy (4) │ New folder - Copy (6) │       0.95 │
│ New folder - Copy (5) │ New folder - Copy (6) │       0.95 │
 ───────────────────────┴───────────────────────┴──────────── 
```