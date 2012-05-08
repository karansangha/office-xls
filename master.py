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
    undone=[]
    for data in master_data:
        if data[3]!="done":
            undone.append(data)
        else:
            a="do nothing"
    undone.pop(0)
    return undone

def getdates(undone_data):
    """ Gets the date from undone_data"""
    dates=[]
    for data in undone_data:
        dates.append(data[4])
    return dates
    
def createfile(dates_data,undone_data):
    """ Creates file based on the data from dates_data and matching it with
        data from undone_data"""
    for date in dates_data:
        filename=date+".csv"
        top="Serial Number"+","+"Name"+","+"Phone number"+","+"comments"+","+"Next call"+"\n"
        fout=open(filename, "w")
        fout.write(top)
        for data in undone_data:
            if (date==data[4]):
                record = data[0]+","+data[1]+","+data[2]+","+data[3]+","+data[4]+"\n"
                fout.write(record)
        fout.close()

m=readdata()
n=undone(m)
u=getdates(n)
createfile(u,n)        
