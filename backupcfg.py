jobs = {'job1' : ['/home/ec2-user/environment/ictprg302/file1.dat'],
    'job2' : ['/home/ec2-user/environment/ictprg302/dir1'],
    'job3' : ['/home/ec2-user/environment/ictprg302/file2.txt'],
    'job4' : ["/home/ec2-user/environment/ictprg302/file3.txt", "/home/ec2-user/environment/ictprg302/file4.txt"]}
    
dstPath = '/home/ec2-user/environment/ictprg302/backups/'

logPath = "/home/ec2-user/environment/ictprg302/backup.log"

#Elastic email setup

smtp = {"sender" : "shaunmd107@gmail.com", # elasticemail.com verified sender
        "recipient" : "30025441@students.sunitafe.edu.au",  # elasticemail.com verified recipient
        "server" : "smtp.elasticemail.com", # elasticemail.com SMTP server
        "port" : 2525, # elasticemail.com SMTP port
        "user" : "shaunmd107@gmail.com", # elasticemail.com user
        "password" : "" } # elasticemail.com password
    
    #MAKE SURE TO REMOVE PASSWORD BEFORE UPLOADING TO GITHUB