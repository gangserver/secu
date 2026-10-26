import hashlib

fname = "dummy.txt"
fp = open(fname, "rb")
fbuf = fp.read()
fp.close()

m = hashlib.md5()
m.update(fbuf)
fmd5 = m.hexdigest()
print(f"fmd5 : {fmd5}")



