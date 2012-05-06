def readdata():
    """Reads date from the master.csv and returns a list of tuples containing data
         from each line of the csv"""

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

def undone(master_data):
    """ Separates data from the master list that's yet to be taken care of"""
    i=1
    undone=[]
    for data in master_data:
        if data[3]!="done":
            undone.append(data)
        else:
            a="do nothing"
    undone.pop(0)
    return undone

