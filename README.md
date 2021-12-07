# AntiRansom
Fighting against ransomware using honeypots

See the project's page http://www.security-projects.com/?Anti_Ransom

**CHANGES IN V5**

1- Use handle from Sysinternals to track access/modify the honeyfolder (better accuracy) 

2- When new process access the honeyfolder, AntiRansom checks the authenticode signature of the process, if its OK, then alert, if not, stop the process and alert 

3- Added a new parameter "enforced" to enforce blocking without user intervention, useful for large deploy (AntiRansom blocks the threat and log into Eventlog)
