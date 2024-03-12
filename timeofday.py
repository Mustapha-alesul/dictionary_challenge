hours = {}
with open('mbox.txt','r') as filee:
    for file in filee:
        if file.startswith("From"):
            try:
                line = file.split()[5]

            except IndexError:
                continue
            # hours = line.split(':')[0]
            