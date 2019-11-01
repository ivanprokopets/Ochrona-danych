from passlib.apache import HtpasswdFile
def check(user,password):
    path = "/home/ligerd/test/haszowanie/user.db"
    ht = HtpasswdFile(path)
    print(ht.verify(user, password))