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
  -a, --assistant
  -t, --threshold FLOAT
  -e, --extensions TEXT  [required]
  -d, --directory
  -v, --verbose
  -h, --hashmode
  --help                 Show this message and exit.


```

### Assistant

Outputs a filename1, filename2, name similarity table. Useful when sorting out things manually on name base.

### Hashmode

Get the hashes from the files and compare the files content-wise by doing so.

## Testing

`python -m unittest discover -s tests`