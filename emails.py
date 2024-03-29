"A python challenge to sort out emails sent messages from  A given list"

filee = open("mbox.txt","r")
emails = {}
days = {}
for file in filee:
    if file.startswith("From"):
        try:
            day = file.split()[2]
            days[day] = days.get(day, 0) + 1

        except IndexError:
            continue

        line = file.split()[1]
        emails[line] = emails.get(line, 0) + 1

        most_email_sent = max(emails)
        domain_name = most_email_sent[most_email_sent.index('@')+1 : most_email_sent.index(".")]
        most_traffic_day = max(days)

print(emails)
print("maximum:", most_email_sent)
print('domain name of most sending email:', domain_name)
print(days)
print("Most Traffic Day:",most_traffic_day)
filee.close()