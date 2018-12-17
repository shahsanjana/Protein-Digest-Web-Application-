
def digest(sequence,enzyme,cleave,minlen,maxlen,minmw,maxmw):
    s = sequence.upper()
    
    cuts=[0]
    zero_cleave =[]


    mw = {'A': 71.04, 'C': 103.01, 'D': 115.03, 'E': 129.04, 'F': 147.07,
        'G': 57.02, 'H': 137.06, 'I': 113.08, 'K': 128.09, 'L': 113.08,
        'M': 131.04, 'N': 114.04, 'P': 97.05, 'Q': 128.06, 'R': 156.10,
        'S': 87.03, 'T': 101.05, 'V': 99.07, 'W': 186.08, 'Y': 163.06 }

    if enzyme == "Trypsin":
        for i in range(len(s)-1):
                if ( (s[i]=='K' or s[i]=='R')and(s[i+1]!='P')):
                        cuts.append(i+1)
        cuts.append(len(s))
        #adds entire length of seq

    if enzyme == "Lys N":
        for i in range(len(s)-1):
            if ( (s[i]=='K')):
                        cuts.append(i)
        cuts.append(len(s))

    if enzyme == "Lys C":
        for i in range(len(s)-1):
            if ( (s[i]=='K')):
                        cuts.append(i+1)
        cuts.append(len(s))

    if enzyme == "Proteinase K":
        for i in range(len(s)-1):
            if ( (s[i]=='A'or s[i]=='F' or s[i]=='Y' or s[i]=='W' or s[i]=="L" or s[i]=="I" or s[i]=="V")):
                        cuts.append(i+1)
        cuts.append(len(s))

    if enzyme == "Thermolysin":
        for i in range(len(s)-1):
            if ( (s[i]=='A'or s[i]=='F' or s[i]=='I' or s[i]=='L' or s[i]=="M" or s[i]=="V" and s[i-1]!="D" and s[i-1]!="E")):
                        cuts.append(i)
        cuts.append(len(s))

    n=int(cleave)+1
    z = zip(cuts,cuts[n:])
    for a, b in zip(cuts, cuts[n:]):
        zero_cleave.append(s[a:b])

    mwvalues0=[]
    lenvalues0=[]

    try:
        for i in zero_cleave:
            mwvalues0.append(sum(map(mw.get,i)))
            lenvalues0.append(len(i))
    except TypeError:
        pass
    
    
    mil = int(minlen)
    mal = int(maxlen)

    mimw =float(minmw)
    mamw= float(maxmw)

    cleaves=[]

    try:
        for i in zero_cleave:
            if len(i) >=mil and len(i)<= mal and sum(map(mw.get,i)) >=mimw and sum(map(mw.get,i))<=mamw:
                cleaves.append(i)
    except TypeError:
        pass


    d0={}
    d1= {}
    l0=[]
    l1=[]
    lenvalues=[]
    molweight=[]

    try:
        for i in cleaves:
            d0["molecular weight"] = sum(map(mw.get,i))
            d0['sequence']=i
            d0["peptide length"] = len(i)
            d0["missed cleaveages"] = cleave
            l0.append(d0.copy())
    except TypeError:
        pass


    for r in l0:
        lengths=r["peptide length"]
        mws=r["molecular weight"]
        lenvalues.append(lengths)
        molweight.append(mws)


    try:
        d1["inputted sequence"] = s
        d1["length of inputted seq"]= len(sequence)
        d1["smallest peptide length"] = min(lenvalues)
        d1["largest peptide length"] = max(lenvalues)
        d1["lowest molecular weight"] = min(molweight)
        d1["largest molecular weight"] = max(molweight)
        l1.append(d1)
    except ValueError:
        pass


    return(l0,l1)



