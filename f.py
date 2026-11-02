file=open ("mailbox.txt","r")
fout=open("output.txt","w")

ls_ids=[]
lines=file.readlines()

for line in lines:
  if "with ESMTP id" in line:
      a=line.split("with ESMTP id")[1]
      b=a.split()[0].strip(";,\n ")
      if b not in ls_ids:
          ls_ids.append(b)
ls_ids.sort()
for eid in ls_ids:
      fout.write(str(eid)+"\n")

file.close()
fout.close()