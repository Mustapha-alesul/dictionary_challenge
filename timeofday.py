hours = {}
hrs = ()
with open('mbox.txt','r') as filee:
    for file in filee:
        if file.startswith("From"):
            try:
                line = file.split()[5]

            except IndexError:
                continue

            hour = line.split(':')[0]
            hours[hour] = hours.get(hour, 0) + 1
            hrs = hours

    print(hours.keys(),hours.values())