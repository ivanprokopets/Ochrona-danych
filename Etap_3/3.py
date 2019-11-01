import htpasswd
def addnew(user,password):
    with htpasswd.Basic("/home/ligerd/test/haszowanie/user.db") as userdb:
        try:
            userdb.add(user,password)
        except htpasswd.basic.UserExists as e:
            print(e)