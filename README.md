# Python File Integrity Monitor

## Overview

A beginner cybersecurity project that uses SHA-256 hashing to detect changes to monitored files.

## How It Works

1. The program creates a SHA-256 hash for each monitored file.
2. The original hashes are saved as a baseline in `hashes.json`.
3. When the program runs again, it calculates the files' current hashes.
4. The current hashes are compared with the saved baseline.
5. If the hashes match, the file is reported as unchanged.
6. If the hashes are different, the file is reported as modified.

## Technologies Used

* Python
* SHA-256
* JSON
* hashlib

## How to Run

Make sure Python is installed, then run:

```bash
python3 file_monitor.py
```

## Example Output

```text
[ALERT] test.txt has been modified!
[OK] test2.txt has not been modified.
```

## What I Learned

* How cryptographic hashing works
* How SHA-256 can be used to identify file changes
* How to store data using JSON
* How to compare a current file state against a saved baseline
* How to use Python functions, lists, loops, and conditional statements
