# SaS Assignment

Implement a program that reads a list of date-time values from a file and writes to a separate file the list of unique, valid date-time values. "Valid" date-time values should adhere to the following format (https://en.wikipedia.org/wiki/ISO_8601): YYYY-MM-DDThh:mm:ssTZD

Where:
• YYYY = four-digit year
• MM = two-digit month (01 through 12)
• DD = two-digit day of month (01 through 31)
• hh = two digits of hour (00 through 23)
• mm = two digits of minute (00 through 59)
• ss = two digits of second (00 through 59)
• TZD = time zone designator (“Z” for GMT or +hh:mm or -hh:mm)

It is not necessary to perform semantic validation of the data-time value. In other words, the date-time value "9999-02-31T12:34:56+12:34" should be considered valid by your program even though February 31, 9999 is not a legitimate dat
