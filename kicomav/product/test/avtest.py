import os
import shutil
import hashlib
from pickle import FALSE

encoding = "utf-8"
os_sep = os.sep

VirusDB = [
    "44d88612fea8a8f36de82e1278abb02f:EICAR Test",
    "77bff0b143e4840ae73d4582a8914a43:Dummy Test"
]

def read_file(
        fname: str,
        mtd: str = "rb",
        ret_type: bytes | str = bytes,
    ) -> bytes | None:
    with open(fname, mtd) as fp:
        fbuf = fp.read()
        if ret_type is str:
            print("return type str")
            fbuf = fbuf.decode(encoding)
        return fbuf

def convertType(
        data: str | bytes,
        target_type: str | bytes
    ) -> str | bytes | None:
    if isinstance(data, str) and not isinstance(data, target_type):
        # print("str -> bytes")
        return data.encode(encoding)
    elif isinstance(data, bytes) and not isinstance(data, target_type):
        # print("bytes -> str")
        return data.decode(encoding)
    else:
        return data

def file_action(
        fname: str, 
        action: str = "move",
    ) -> None:
    if action == "delete":
        print("File deleted")
        os.remove(fname)
    elif action == "move":
        dst = f"temp{os.sep}{get_file_name(fname)}"
        print(f"File moved : {dst}")
        # os.rename(fname, dst)       # 대상 파일이 이미 있으면 FileExistsError 오류
        # os.replace(fname, dst)      # 대상 파일이 이미 있으면 덮어쓰기(Overwrite)
        shutil.move(fname, dst)
    else:
        print("No action")

def get_file_name(
        file_path: str,
    ) -> str | None:
    file_name = os.path.basename(file_path)
    
    # path/file.ext 일 때 filename : path/file, file_extension : .ext
    # filename, file_extension = os.path.splitext(file_path)          
    
    # r_idx = file_path.rfind(os_sep)             # 찾는 문자열이 없을 때 -1 리턴
    # r_idx = file_path.rindex(os_sep)            # 찾는 문자열이 없을 때 ValueError
    # file_name = file_path[r_idx+1:]
    print(f"file_name : {file_name}")
    return file_name

vdb = []
def MakeVirusDB() -> None:
    for pattern in VirusDB:
        t =  []
        v = pattern.split(":")
        t.append(v[0])
        t.append(v[1])
        vdb.append(t)

if __name__ == "__main__":
    # file_name = "dummy.txt"
    file_name = "eicar.txt"
    # file_name = "normal.txt"
    fname = f"file{os.sep}{file_name}"
    # action = ""
    # action = "delete"
    action = "move"
    
    fbuf = read_file(fname, "rb", bytes)
    print(f"fbuf : {fbuf}")
    
    m = hashlib.md5()
    m.update(fbuf)
    fmd5 = m.hexdigest()
    print(f"fmd5 : {fmd5}")
    
    MakeVirusDB()
    # print(f"vdb : {vdb}")
    
    for v in vdb:
        if fmd5 == v[0]:
            print(v[1])
            is_virus = True
            break
    else:
        print("No Virus")
        is_virus = False
    
    if is_virus:
        file_action(fname, action)

    """
    if fbuf[0:3] == b"X5O":
        print("Virus")
        if action == "delete":
            print("File deleted")
            os.remove(fname)
        elif action == "move":
            dst = "temp" + os.sep + fname
            print(f"File moved : {dst}")
            # os.rename(fname, dst)       # 대상 파일이 이미 있으면 FileExistsError 오류
            # os.replace(fname, dst)      # 대상 파일이 이미 있으면 덮어쓰기(Overwrite)
            shutil.move(fname, dst)
        else:
            print("No action")
    else:
        print("No Virus")
    """




