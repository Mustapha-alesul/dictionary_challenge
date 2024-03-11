"A python challenge to sort out emails sent messages from  A given list"

filee = open("mbox.txt","r")
emails = {}
for file in filee:
    if file.startswith("From"):
        line = file.split()[1]
        emails.get(line,0) + 1
print(emails)