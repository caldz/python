set a=%date:~0,4%%date:~5,2%%date:~8,2%%time:~0,2%%time:~3,2%%time:~6,2%
::mdbparserkv -rx master.csv -tx slave.csv -output "reply_time-%a%.csv"
mdbparserkv -rx master.csv -tx slave.csv -output "reply_time.csv"