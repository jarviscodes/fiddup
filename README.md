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
Usage: main.py [OPTIONS]

Options:
  -i, --inpath TEXT      [required]
  -a, --analyze BOOLEAN
  -t, --threshold FLOAT
  -e, --extensions TEXT  [required]
  -v, --verbose
  --help                 Show this message and exit.
```

## Example output

```
(env) E:\Users\Jarvis\PycharmProjects\fiddup>python -m fiddup -i C:\Temp -e txt -d True
[Results]
Original                                Compared to                             Match          
New folder                              New folder - Copy                       74.07
New folder - Copy                       New folder - Copy (2)                   89.47
New folder - Copy                       New folder - Copy (3)                   89.47
New folder - Copy                       New folder - Copy (4)                   89.47
New folder - Copy                       New folder - Copy (5)                   89.47
New folder - Copy                       New folder - Copy (6)                   89.47
New folder - Copy (2)                   New folder - Copy (3)                   95.24
New folder - Copy (2)                   New folder - Copy (4)                   95.24
New folder - Copy (2)                   New folder - Copy (5)                   95.24
New folder - Copy (2)                   New folder - Copy (6)                   95.24
New folder - Copy (3)                   New folder - Copy (4)                   95.24
New folder - Copy (3)                   New folder - Copy (5)                   95.24
New folder - Copy (3)                   New folder - Copy (6)                   95.24
New folder - Copy (4)                   New folder - Copy (5)                   95.24
New folder - Copy (4)                   New folder - Copy (6)                   95.24
New folder - Copy (5)                   New folder - Copy (6)                   95.24
New Text Document - Copy (2).txt        New Text Document - Copy (3).txt        96.88
New Text Document - Copy (2).txt        New Text Document - Copy (4).txt        96.88
New Text Document - Copy (2).txt        New Text Document - Copy (5).txt        96.88
New Text Document - Copy (2).txt        New Text Document - Copy (6).txt        96.88
New Text Document - Copy (2).txt        New Text Document - Copy.txt            93.33
New Text Document - Copy (2).txt        New Text Document.txt                   79.25
New Text Document - Copy (3).txt        New Text Document - Copy (4).txt        96.88
New Text Document - Copy (3).txt        New Text Document - Copy (5).txt        96.88
New Text Document - Copy (3).txt        New Text Document - Copy (6).txt        96.88
New Text Document - Copy (3).txt        New Text Document - Copy.txt            93.33
New Text Document - Copy (3).txt        New Text Document.txt                   79.25
New Text Document - Copy (4).txt        New Text Document - Copy (5).txt        96.88
New Text Document - Copy (4).txt        New Text Document - Copy (6).txt        96.88
New Text Document - Copy (4).txt        New Text Document - Copy.txt            93.33
New Text Document - Copy (4).txt        New Text Document.txt                   79.25
New Text Document - Copy (5).txt        New Text Document - Copy (6).txt        96.88
New Text Document - Copy (5).txt        New Text Document - Copy.txt            93.33
New Text Document - Copy (5).txt        New Text Document.txt                   79.25
New Text Document - Copy (6).txt        New Text Document - Copy.txt            93.33
New Text Document - Copy (6).txt        New Text Document.txt                   79.25
New Text Document - Copy.txt            New Text Document.txt                   85.71
```