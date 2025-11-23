
class  facebook:

    def __init__(self):
        self.username=" "
        self.password=" "
        self.loggedin=" "
        self.menu()


    def menu(self):
        user_input=input(""" welcome to facebook how would like to  proceed ?
                         1.press one for signup
                         2.Press two for singin 
                         3.press three for write a post
                         4.press four for message a friend
                         5.press any key to exit""")
        if user_input =="1":
            self.signup()

        if user_input =="2":
            self.signin()
        if user_input =="3":
            self.post()
        if user_input=="4":
            self.sendfriend()
        if user_input=="5":
            exit()


    def signup(self):
        email=input("enter your email")
        pwd=input("enter your password")
        self.username=email
        self.password =pwd
        print("you are signed up successfully")
        print("\n")
        self.menu()


    def signin(self):
        if self.username==" " and self.password== " ":
            print("signup first by pressing 1 in the menu")

        else:
            uname=input("enter username")
            passw=input("enter password")

            if self.username==uname and self.password==passw:
                print("your are logged in succesfully")
                self.loggedin=True
            else:
                print("enter a correct info")
            print("\n")
            self.menu()

    def post(self):
        if self.loggedin==True:
            txt=input("enter a message here")
            print(f" following content is posted {txt}")
        else:
            print("your need to signin first then post")
        print("\n")
        self.menu()


    def sendfriend(self):
        if self.loggedin==True:
            txt=input("enter a message here")
            friend=input("whom you want to send a message")
            print(f" message is send to {friend}")
        else:
            print("you need to singup first")

        print("\n")
        self.menu()



d=facebook()
