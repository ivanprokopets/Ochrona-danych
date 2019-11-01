import htpasswd
def changepassword(user,newpassword):
    with htpasswd.Basic("/home/ligerd/test/haszowanie/user.db") as userdb:
        try:
            userdb.change_password(user, newpassword)
        except htpasswd.basic.UserExists as e:
            print(e)