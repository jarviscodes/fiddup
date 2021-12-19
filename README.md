# Fiddup

![Version 2.3.1](https://img.shields.io/badge/Version-2.3.1-blue)
![MIT License](https://img.shields.io/badge/License-MIT-success)
![Flake8](https://github.com/jarviscodes/fiddup/actions/workflows/flake8_linter.yml/badge.svg)
![Tests](https://github.com/jarviscodes/fiddup/actions/workflows/testing_and_coverage.yml/badge.svg)

**Fi**le **D**e**Dup**licator

Small tool to quickly scan a directory for files of similar names.
Useful to scan through archives of books, documents, downloads, movies, music, ...

Two modes are available: Assistant (name based comparison), and Hash mode (hash comparison).

Fiddup is non-destructive. It will report similarities and duplicates, but it will not remove them.

In order to keep things performant and memory-limited, hashmode only hashes parts of both files.
In case of false positives, first try to increase the `--chunk_count` flag. (default=5)

## Installation

### From PyPi

`pip3 install fiddup`

### From Sauce
* `git pull https://github.com/jarviscodes/fiddup`

* `setup.py install`

## Usage
```
Usage: python -m fiddup [OPTIONS]

  Fiddup is a Non-destructive file deduplicator that can assist you to find
  similar or duplicate files.

Options:
  -i, --inpath TEXT      Path to scan for duplicates.  [required]
  -a, --assistant        Toggles Assistant mode (name similarity search).
  -t, --threshold FLOAT  Similarity threshold. Assistant will only show
                         similarities > this.
  -e, --extensions TEXT  List of extensions to scan for, specify multiple with
                         e.g.: -e zip -e txt -e pdf.  [required]
  -d, --directory        Include directories in comparison. Only available in
                         assistant mode.
  -v, --verbose          Show verbose output.
  -h, --hashmode         Toggles hash mode (file hash comparison).
  --chunk_count INTEGER  Number of chunks to read from files while hashing.
                         Higher = more accuracy = Slower.
  --help                 Show this message and exit.

```

### Assistant

Outputs a filename1, filename2, name similarity table. Useful when sorting out things manually on name base.

### Hashmode

Get the hashes from the files and compare the files content-wise by doing so.

## Testing

`python -m unittest discover -s tests`