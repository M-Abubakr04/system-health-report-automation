# System Health Report Automation

A Python automation script that monitors system health and sends email reports automatically.

# Features
- Collects CPU, memory, and disk usage
- Works on both Windows and Linux
- Sends system report via email
- Uses environment variables for security
- Can be scheduled using Task Scheduler or Crontab

# Technologies Used
- Python
- SMTP
- Windows (WMIC)
- Linux (free, df)

# Setup
1. Clone the repository   
2. Set environment variables for email credentials
3. Run the script manually or via scheduler

# Setup for Windows 
1.  Press Windows+R
2.  Type taskschd.msc
3.  Create Task
4.  Click Create Basic Task
5.  Name: Daily System Health Report
6.  Trigger
7.  Choose Daily
8.  Time of your choice
9.  Action
10. Choose Start a Program
11. Program/script:
12. C:\Users\M.Abubakr\Desktop\system_report.bat  #Giving path of the .bat file

# Setup or Linux
1. Go to crontab -e
2. Choose the time and give path to the script


# Best Practice
Credentials are not hard-coded and must be provided via environment variables.