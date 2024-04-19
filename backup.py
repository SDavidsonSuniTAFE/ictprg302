#!/usr/bin/python3
"""
Author: Shaun Davidson
shaunmd107@gmail.com
Version 1.0
MIT Copyright Licence
"""
import sys
import os
import pathlib
import shutil
import smtplib
from datetime import datetime
from backupcfg import jobs, dstPath, smtp, logPath

def sendEmail(errorType, message, dateTimeStamp):
 #Send an email message to the specified recipient. 
#Parameters: 
    #message (string): message to send. 
    #dateTimeStamp (string): Date and time when program was run. 
# create email message 
    email = 'To: ' + smtp["recipient"] + '\n' + 'From: ' + smtp["sender"] + '\n' + f'Subject: Backup Error - {errorType}\n\n' + message + '\n' 
    # connect to email server and send email
    try:
        smtp_server = smtplib.SMTP(smtp["server"], smtp["port"])
        smtp_server.ehlo()
        smtp_server.starttls()
        smtp_server.ehlo()
        smtp_server.login(smtp["user"], smtp["password"])
        smtp_server.sendmail(smtp["sender"], smtp["recipient"], email)
        smtp_server.close()
        pass
    except Exception as e:
        print("ERROR: Send email failed: " + str(e), file=sys.stderr)
        pass
    
def logging(message):
    file = open(logPath, "a") #Opens the backup log file. if the file doesn't exist the program will make it
    file.write(f"{message} \n") #prints to log file. \n works as ENTER and makes it so the next message starts on a new line
    file.close()

def Error(errorType, errorMessage, dateTimeStamp):#What the program does when it inconters an error
    print(f"ERROR: {errorMessage}") #Print error to screen
    failureMessage = f"FAILURE - {dateTimeStamp} - ERROR: {errorMessage}" #failure message to be sent to the log file
    logging(failureMessage)
    sendEmail(errorType, failureMessage, dateTimeStamp)

def main():
    dateTimeStamp = datetime.now().strftime("%Y%m%d-%H%M%S") #D&T stamp #Timestamp not working properly, hour value always starts with 0 i.e 11:55:30 is displayed 015530
    argCount = len(sys.argv)
    if argCount != 2: #if no job is giving or multiple jobs are given
        if argCount < 2:
            Error("jobname", "jobname is missing from the command line", dateTimeStamp)
        else:
            Error("jobname", "too many jobs are entered in the command line", dateTimeStamp)
    else:
        jobName = sys.argv[1]
        if jobName not in jobs: #if job doesn't exist
            Error("job  doesn't exist", f"jobname {jobName} is not defined", dateTimeStamp)
        else:
            for srcPath in jobs[jobName]:
                if not os.path.exists(srcPath): #if the FILE DESTINATION doesn't exist i.e the job name exists but leads to a file that doesn't exist
                 Error("source path not found", f"source path {srcPath} does not exist", dateTimeStamp)
                else:
                    if not os.path.exists(dstPath): #if the backup destination doesn't exist
                        Error("job  path", f"path {dstPath} does not exist", dateTimeStamp)
                    else:
                    
                        srcDetails = pathlib.PurePath(srcPath) #Variable that is the last part of the source path i.e "file1"
                        dstLoc = dstPath + "/" + srcDetails.name + "-" + dateTimeStamp #destination of the backup created with time stamp i.e "/home/ec2-user/environment/ictprg302/backups/file1-YYYYMMDD-hhmmss"
                    
                        if pathlib.Path(srcPath).is_dir():
                            shutil.copytree(srcPath, dstLoc)
                            sccMessage = f"SUCCESS - {dateTimeStamp} - your directory has been backed up =)"
                            print(sccMessage)
                            logging(sccMessage)
                        
                        else:
                            shutil.copy2(srcPath, dstLoc)
                            sccMessage = f"SUCCESS - {dateTimeStamp} - your file has been backed up =)"
                            print(sccMessage)
                            logging(sccMessage)
                        
if __name__ == "__main__":
    main()