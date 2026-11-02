fin = open("mailbox.txt", 'r')
fout = open("output.txt", 'w')

domains = []
lines = fin.readlines()

for line in lines:
    if line.startswith("To:"):
        email = line.split()[1]
        domain = email.split("@")[1]
        if domain not in domains:
            domains.append(domain)
domains.sort()
fout.write(domain + "\n")

fin.close()
fout.close()