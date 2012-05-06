def readdata():
    fname="master.csv"
    master=[]
    fin=open(fname)
    for record in fin:
        record = record.strip() #strips non-printing characters
        data = record.split(",")
        entry=(data[0],data[1],data[2],data[3],data[4])
        master.append(entry)
    fin.close()
    return master
               
