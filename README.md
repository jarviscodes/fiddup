# Fiddup

**Fi**le **D**e**Dup**licator

Small tool to quickly scan a directory for files of similar names.
Useful to scan through archives of books, documents, downloads, movies, music, ...

Outputs the original filename, the compared filename, and similarity.
Only outputs above a specified similarity are stored.

## Depends

Install through
`pip3 install -r requirements.txt`

Or install individually:
* `pip3 install click`
* `pip3 install colorama`

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
(venv) C:\Users\Cedric\PycharmProjects\fiddup>python main.py --inpath C:\Temp\ -e txt -e pdf -v
[Info] Starting with analyze: True
[Info] Starting with match threshold: 0.7
[Info] Scanning for extensions: txt, pdf
[Results]
Original                                Compared to                             Match          
C:\Temp\Movie-1-About-Fish.txt          C:\Temp\Movie-2-Fish.txt                          85.19
C:\Temp\Movie-1-About-Fish.txt          C:\Temp\Ebook-1-About-Fish.pdf                    76.67
C:\Temp\Movie-1-About-Fish.txt          C:\Temp\Ebook-2-About-Fish.pdf                    73.33
C:\Temp\Movie-1-About-Fish.txt          C:\Temp\Ebook-3-About-Fish.pdf                    73.33
C:\Temp\Movie-2-Fish.txt                C:\Temp\Movie-1-About-Fish.txt                    85.19
C:\Temp\Ebook about fish.pdf            C:\Temp\Ebook-1-About-Fish.pdf                    82.76
C:\Temp\Ebook about fish.pdf            C:\Temp\Ebook-2-About-Fish.pdf                    82.76
C:\Temp\Ebook about fish.pdf            C:\Temp\Ebook-3-About-Fish.pdf                    82.76
C:\Temp\Ebook-1-About-Fish.pdf          C:\Temp\Movie-1-About-Fish.txt                    76.67
C:\Temp\Ebook-1-About-Fish.pdf          C:\Temp\Ebook about fish.pdf                      82.76
C:\Temp\Ebook-1-About-Fish.pdf          C:\Temp\Ebook-2-About-Fish.pdf                    96.67
C:\Temp\Ebook-1-About-Fish.pdf          C:\Temp\Ebook-3-About-Fish.pdf                    96.67
C:\Temp\Ebook-2-About-Fish.pdf          C:\Temp\Movie-1-About-Fish.txt                    73.33
C:\Temp\Ebook-2-About-Fish.pdf          C:\Temp\Ebook about fish.pdf                      82.76
C:\Temp\Ebook-2-About-Fish.pdf          C:\Temp\Ebook-1-About-Fish.pdf                    96.67
C:\Temp\Ebook-2-About-Fish.pdf          C:\Temp\Ebook-3-About-Fish.pdf                    96.67
C:\Temp\Ebook-3-About-Fish.pdf          C:\Temp\Movie-1-About-Fish.txt                    73.33
C:\Temp\Ebook-3-About-Fish.pdf          C:\Temp\Ebook about fish.pdf                      82.76
C:\Temp\Ebook-3-About-Fish.pdf          C:\Temp\Ebook-1-About-Fish.pdf                    96.67
C:\Temp\Ebook-3-About-Fish.pdf          C:\Temp\Ebook-2-About-Fish.pdf                    96.67
```