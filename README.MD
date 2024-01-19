A project to modify subtitle files to delay / hasten by given number of seconds
- Currently, it only supports SRT files.
- Following command shows the expected arguments


`python -m srt.main --help`
```
usage: main.py [-h] -i INPUT -o OUTPUT -s SYNC

options:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        The input file path
  -o OUTPUT, --output OUTPUT
                        The output file path
  -s SYNC, --sync SYNC  +/- seconds to delay / hasten by
```