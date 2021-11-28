from tkinter import Tk, Label, Entry, \
    StringVar, Button, messagebox, ttk
from home_view import check_login


def switch_screens(obj):
    print(type(obj).__name__)
    if not obj or type(obj).__name__ == 'LoginUi':
        obj.destroy()
        SignupUi()
    else:
        obj.destroy()
        LoginUi()


class LoginUi(Tk):
    def __init__(self):
        super().__init__()
        # input var type declares
        self.name_type = StringVar()
        self.pass_type = StringVar()
        self.screen_framework()
        self.login_page()

    def _login(self):
        if '' in [self.name_type.get(), self.pass_type.get()]:
            messagebox.showerror("Error", "please enter the username and password.",
                                 parent=self)
        else:
            var = check_login(self.name_type.get(), self.pass_type.get())
            messagebox.showinfo("info", var, parent=self)

    def screen_framework(self):
        # app title
        self.title("Book Management")
        # win size
        self.maxsize(width=500, height=500)
        self.minsize(width=500, height=500)

    def login_page(self):
        Label(self, text='Login',
              font='Verdana 25 bold').place(x=80, y=150)
        Label(self, text='User Name:',
              font='Verdana 10 bold').place(x=80, y=220)
        Label(self, text='Password:',
              font='Verdana 10 bold').place(x=80, y=260)

        name_entry = Entry(self, width=40,
                           textvariable=self.name_type)
        name_entry.place(x=200, y=223)
        name_entry.focus()

        password = Entry(self, width=40,
                         textvariable=self.pass_type, show='*')
        password.place(x=200, y=260)
        btn_login = Button(self, text="Login", font="Verdana 10 bold",
                           command=self._login)
        btn_login.place(x=200, y=293)
        btn_signup = Button(self, text="Signup", font="Verdana 10 bold",
                            command=self.switch)
        btn_signup.place(x=300, y=293)

    def switch(self):
        switch_screens(self)


class SignupUi(Tk):
    ERROR = 'Error.TLabel'
    SUCCESS = 'Success.TLabel'

    def __init__(self):
        super().__init__()
        # form Variables
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.password_var = StringVar()
        self.confirm_password_var = StringVar()
        self.confirm_password_var.trace('w', self.validate)
        self.style = ttk.Style(self)
        self.style.configure('Error.TLabel', foreground='red')
        self.style.configure('Success.TLabel', foreground='green')
        self.message_label = ttk.Label(self,
                                       font='Verdana 12 bold')
        self.screen_framework()
        self.sign_up()

    def set_message(self, message, type=None):
        self.message_label['text'] = message
        if type:
            self.message_label['style'] = type

    def validate(self, *args):
        password = self.password_var.get()
        confirm_password = self.confirm_password_var.get()

        if confirm_password == password:
            self.set_message("Success: message", self.SUCCESS)
            return
        if password.startswith(confirm_password):
            self.set_message("Warning: keep")

        self.set_message("Error:don't match", self.ERROR)

    def screen_framework(self):
        # app title
        self.title("Signup Form")
        # win size
        self.maxsize(width=500, height=500)
        self.minsize(width=500, height=500)

    def sign_up(self):
        Label(self, text='Register',
              font='Verdana 25 bold').place(x=160, y=100)
        Label(self, text='Name:',
              font='Verdana 10 bold').place(x=80, y=150)
        name_entry = Entry(self, width=40,
                           textvariable=self.name_var)
        name_entry.place(x=200, y=153)
        name_entry.focus()
        Label(self, text='Email:',
              font='Verdana 10 bold').place(x=80, y=200)
        email_entry = Entry(self, width=40,
                            textvariable=self.email_var)
        email_entry.place(x=200, y=203)

        Label(self, text='Password:',
              font='Verdana 10 bold').place(x=80, y=260)

        password = Entry(self, width=40,
                         textvariable=self.password_var, show='*')
        password.place(x=200, y=260)
        Label(self, text='retype Password:',
              font='Verdana 10 bold').place(x=68, y=300)

        password2 = Entry(self, width=40,
                          textvariable=self.confirm_password_var,
                          show='*')
        password2.place(x=200, y=303)
        self.message_label.place(x=200, y=320)
        btn_login = Button(self, text="Login", font="Verdana 10 bold",
                           command=self.switch)
        btn_login.place(x=300, y=350)

    def switch(self):
        switch_screens(self)


if __name__ == '__main__':
    var = LoginUi()
    var.mainloop()
