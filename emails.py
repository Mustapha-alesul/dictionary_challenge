"A python challenge to sort out emails sent messages from  A given list"

filee = open("mbox.txt","r")
emails = {}
days = {}
for file in filee:
    if file.startswith("From"):
        line = file.split()[1]
        emails[line] = emails.get(line, 0) + 1
        try:
            day = file.split()[2]

        days[day] = days.get(day, 0) + 1
        maxx = max(emails)
        domain_name = maxx[maxx.index('@')+1 : maxx.index(".")]
print(emails)
print("maximum:", maxx)
print('domain:', domainn)
print(day)
filee.close()