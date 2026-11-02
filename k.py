fin=open("mailbox.txt","r")
fout=open("output.txt","w")
for line in fin:
    if line.startswith("From: "):
        words=line.split()
        if len(words) >=2:
            email=words[1]
            fout.write(email+ "\n")
fin.close()
fout.close()