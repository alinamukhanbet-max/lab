fin = open("mailbox.txt", "r")
fout = open("output.txt", "w")
dates = []
for line in fin:
    if line.startswith("Date: "):
        words = line.split()
        if len(words) >= 5:
            date = words[2] + " " + words[3]
            if date not in dates:
                dates.append(date)
dates.sort()
for date in dates:
    fout.write(date + "\n")
fin.close()
fout.close()