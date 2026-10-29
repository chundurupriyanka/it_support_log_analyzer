# IT Support Log Analyzer

## Overview

IT Support Log Analyzer is a Python project that reads application log
files and summarizes their entries. It counts `ERROR`, `WARNING`, and
`INFO` entries, identifies repeated error and warning messages, and
reports malformed entries.

This is an independent learning project using sample log data to
practice Python fundamentals in an IT support troubleshooting scenario.

## Features

- Reads application log entries from `application.log`.
- Counts `ERROR`, `WARNING`, and `INFO` entries.
- Uses dictionaries to count repeated error, warning, and INFO messages.
- Sorts error, warning, and INFO messages by occurrence frequency.
- Identifies the most frequent error and warning messages.
- Identifies the most frequent INFO message or reports ties when multiple messages share the highest frequency.
- Skips blank lines.
- Detects and counts malformed log entries.
- Generates an `analysis_report.txt` report containing error, warning, and INFO summaries, along with total counts.
- Handles missing files and invalid input using exception handling.
- Handles empty error, warning, and INFO results without accessing the first item of an empty list.



## Technologies and Python Concepts

-   Python 3
-   File handling (`open()` and `with`)
-   Strings, lists, and dictionaries
-   Loops and conditional statements
-   Exception handling (`try`, `except`, `finally`)
-   `continue`
-   `sorted()` and `lambda`

## Project Structure

``` text
it_support_log_analyzer/
├── application.log
├── log_analyzer.py
└── README.md
```

## Sample Log Data

These entries match the sample log file used to test the project:

``` text
2026-10-11 09:00:10 INFO Application started
2026-10-11 09:01:15 WARNING High response time
2026-10-11 09:02:20 ERROR Database connection failed
2026-10-11 09:03:25 INFO Request processed successfully
2026-10-11 09:04:30 ERROR Database connection failed
2026-10-11 09:05:35 WARNING High response time
2026-10-11 09:06:40 ERROR Authentication failed
2026-10-11 09:07:45 INFO Application running normally
ERROR Database connection failed
2026-10-11 ERROR
WARNING Disk space running low
2026-10-11 09:03:25 INFO WARNING messages are important
```

### Malformed Entries

The program's current validation treats these three entries as
malformed:

-   `ERROR Database connection failed` --- missing date and time.
-   `2026-10-11 ERROR` --- missing required fields.
-   `WARNING Disk space running low` --- missing date and time.

The final entry,
`2026-10-11 09:03:25 INFO WARNING messages are important`, is valid.
`INFO` is the log level; `WARNING` is part of the message text. The
program should count it as INFO, not WARNING.

## How It Works

1.  Opens and reads `application.log`.
2.  Skips blank lines.
3.  Validates each entry's structure and log level.
4.  Counts ERROR, WARNING, and INFO entries.
5.  Groups repeated error and warning messages in dictionaries.
6.  Sorts messages by occurrence frequency.
7.  Displays the most frequent error and warning when available.
8.  Handles missing files and empty error or warning results.

## How to Run

**Prerequisite:** Python 3 installed on your system.

Run this command from the project directory:

``` bash
python3 log_analyzer.py
```

Keep `application.log` in the same directory as `log_analyzer.py`.

## Example Output

``` text
Error summary:
 Database connection failed: 2 occurrences
 Authentication failed: 1 occurrences
 Most frequent error: Database connection failed
occurrences: 2
warnings summary
 High response time: 2 occurrences
Most frequent warnings: High response time
Occurrences: 2
Total errors: 3
Total warnings: 2
Total malformed entries: 3
Total info entries: 4
Log analysis attempt is finished
```

## What I Learned

-   Reading and processing text files in Python.
-   Using dictionaries to count repeated messages.
-   Sorting dictionary items by occurrence frequency.
-   Validating log entries before processing them.
-   Handling exceptions and missing files.
-   Skipping blank lines and counting malformed entries.
-   Handling empty results without an `IndexError`.
-   Applying Python fundamentals to an IT support troubleshooting
    scenario.

## Possible Future Improvements

-   Filter log entries by date or log level.
-   Save analysis results to a separate report file.
-   Add automated tests for valid, malformed, and empty log files.
-   Improve handling of large log files.

## Disclaimer

This is an independent learning project using sample log data. Do not
upload confidential company logs, credentials, or other sensitive
information to a public repository.
