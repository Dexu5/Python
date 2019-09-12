import smtplib
import time

sent=0
multi=raw_input("Would you like to send to multiple targets? y/n: ")

if multi=="y":
    gmail_username=raw_input("Please enter your gmail username: ")
    gmail_password=raw_input("Please enter password: ")
    print ("Connecting to server please wait...")
    smtpserver=smtplib.SMTP("smtp.gmail.com",587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(gmail_username,gmail_password)
    print("Connection attained")

    print("Please enter targets. Press enter  on a blank line to end input")
    emaillist=[]
    while True:
      tgts=raw_input("Please enter target: ")
      if len(tgts)==0: break
      emaillist.append(tgts)
      num_sent=input('Number of emails to send: ')
      msg=raw_input("Please enter a message to send to targets: ")
      while sent <=num_sent:
        for tgts in emaillist:
          smtpserver.sendmail(gmail_username,tgts,msg)
          print ("Sending emails")
          sent+=1
          print ("Done")

elif multi=="n":

    gmail_username=raw_input("Please enter your gmail username: ")
    gmail_password=raw_input("Please enter password: ")
    smtpserver=smtplib.SMTP("smtp.gmail.com",587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(gmail_username,gmail_password)
    targetEmail=raw_input("Please enter target E-mail: ")
    print("Connecting please wait...")
    msg=raw_input("Please enter a message: ")
    numSent=input("How many messages would you like to send?: ")
    for i in xrange(numSent + 1):
      smtpserver.sendmail(gmail_username,targetEmail,msg)
      print "Sent %s %d emails." % (targetEmail,sent)
      sent= sent + 1
      print "Done"
      time.sleep(1)
else:
    print "Please choose y or n"