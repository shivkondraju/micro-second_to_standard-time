# micro-second_to_standard-time
Conversion of Micro Second Time String to Standard Time in a Data Frame

Working in financial industry means data analysts and scientists have to deal with Ticker data. 

In a project I worked, I was provided with ticker data (csv file) which has a time format like 90000073936 and date is in format of 20200302 . 

The number you see is time with hours, minutes, seconds, milli seconds, micro seconds all in one string as a number. The date is in format of yyyymmdd all in one string as a number.
My task is to convert a number looking time and date to a readable standard date time format in a single column of Data Frame.

This project is about the same.

The attached csv file has limited source data.

Example:
Original Data:
Time: 90000073936
Date: 20200302

Expected Output:
2020-03-02 09:00:26


Happy Coding!
