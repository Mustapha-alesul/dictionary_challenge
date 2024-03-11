"A python challenge to sort out emails sent messages from  A given list"

filee = open("mbox.txt","r")
line = set()
for file in filee:
    if file.startswith("From"):
        line = file.split()[1]
    print(line)