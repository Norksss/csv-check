# CSV Check

A small, dependency-free Python command-line tool for checking CSV files before importing them into a spreadsheet or contact tracker.

Requires Python 3.9 or later. Run:

```sh
python3 csv_check.py contacts.csv
```

Reports empty files, unnamed or duplicate headers (ignoring case and surrounding spaces), inconsistent record widths, malformed CSV, and unreadable files. Reads UTF-8 files, including those with a byte order mark. Quoted multiline fields are supported. The source file is never modified.

Exit status: 0 for a clean file, 1 for validation problems, 2 for a read or parsing error.

This is an initial release. It does not check email validity, deduplicate contacts, or establish that data is accurate.

Licensed under the MIT license. See LICENSE.
