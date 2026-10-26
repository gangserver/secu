import sys
import os
import hashlib

VirusDB = []
vdb = []
vsize = []

def LoadVirusDB() -> None:
    with open("db" + os.sep + "virus.db", "rb") as fp:
        while True:
            line = fp.readline()
            if not line:
                break
            
            str_line = str(line, "utf-8")
            # str_line = line.decode()
            
            str_line = str_line.strip()
            VirusDB.append(str_line)

def MakeVirusDB() -> None:
    for pattern in VirusDB:
        t = []
        v = pattern.split(":")
        t.append(v[1])
        t.append(v[2])
        vdb.append(t)
        
        size = int(v[0])
        if vsize.count(size) == 0:
            vsize.append(size)

def SearchVDB(fmd5: str) -> tuple(bool, str):
    for t in vdb:
        if t[0] == fmd5:
            return True, t[1]
    
    return False, ""

if __name__ == "__main__":
    LoadVirusDB()
    MakeVirusDB()
    
    if len(sys.argv) != 2:
        print("Usage : antivirus.py [file]")
        exit(0)
    
    fname = sys.argv[1]
    
    size = os.path.getsize(fname)
    if vsize.count(size):
        with open(fname, "rb") as fp:
            buf = fp.read()
            
            m = hashlib.md5()
            m.update(buf)
            fmd5 = m.hexdigest()
            
            ret, vname = SearchVDB(fmd5)
            if ret:
                print(f"{fname} : {vname}")
                os.remove(fname)
            else:
                print(f"{fname} : ok1")
            
    else:
        print(f"{fname} : ok2")




