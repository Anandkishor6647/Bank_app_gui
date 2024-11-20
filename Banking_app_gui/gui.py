import tkinter
from tkinter import *
from tkinter import ttk
from classes import Account, total_acc
import database
import hash

acc_control = []


# fill account list from database#######################################################
def fill_data():
    if len(total_acc) == 0:
        data_out = database.show_db()
        print(data_out)
        for i in range(0, len(data_out)):
            ex_acc = Account(data_out[i][1], data_out[i][2], data_out[i][3], data_out[i][4])
            ex_acc.balance = data_out[i][5]
            ex_acc.account_num = data_out[i][0]
            total_acc.append(ex_acc)


fill_data()


# #########################################page1 Create Account##########################

def create_account():
    # Creating account Class and adding into acc_control List

    def create():
        acc_control.clear()
        user_name = name_entry.get()
        user_email = email_entry.get()
        user_mob = mob_entry.get()
        user_pass = pass_entry.get()
        # hashing password###############
        user_pass = hash.hashed(user_pass)
        # #############################creating an Account object####################
        new_account = Account(user_name, user_email, user_mob, user_pass)
        user_num = new_account.account_num
        user_bal = new_account.balance
        # #######################################################################
        # database update################
        database.write([(user_num, user_name, user_email, user_mob, user_pass, user_bal)])
        # ############################
        acc_control.append(new_account)
        # ##################################################################
        if len(acc_control) > 0:
            message_label = Label(window, text=acc_control[0].message)
            message_label.place(x=20, y=180)

        name_entry.delete(0, "end")
        email_entry.delete(0, "end")
        mob_entry.delete(0, "end")
        pass_entry.delete(0, "end")
        create_window.destroy()
        window.deiconify()
        login_page()

    window.withdraw()
    create_window = tkinter.Toplevel(window)
    create_window.title("Create New Account")
    create_window.geometry("500x300")
    name_label = Label(create_window, text="Name:")
    name_label.place(x=50, y=10)
    name_entry = Entry(create_window)
    name_entry.place(x=100, y=10)
    email_label = Label(create_window, text="Email")
    email_label.place(x=50, y=30)
    email_entry = Entry(create_window)
    email_entry.place(x=100, y=30)
    mob_label = Label(create_window, text="Phone")
    mob_label.place(x=50, y=50)
    mob_entry = Entry(create_window)
    mob_entry.place(x=100, y=50)
    pass_label = Label(create_window, text="Password")
    pass_label.place(x=43, y=70)
    pass_entry = Entry(create_window, show="*")
    pass_entry.place(x=100, y=70)
    create_button = Button(create_window, text="Create", command=create)
    create_button.place(x=100, y=100)


# ###########################Login Authentication page Before Login Page###################
def authenticate():
    # check for password
    def check_and_log():
        in_pass = pas_entry.get()
        for k in range(0, len(total_acc)):
            if hash.authenticate(total_acc[k].password, in_pass):
                acc_control.append(total_acc[k])
                login_page()
                auth_window.destroy()
                break
            elif not hash.authenticate(total_acc[k].password, in_pass) and k == len(total_acc) - 1:
                print("failed")

    auth_window = tkinter.Toplevel()
    auth_window.title("Authenticate")
    auth_window.geometry("500x100")
    pas_label = Label(auth_window, text="Password")
    pas_label.place(x=20, y=20)
    pas_entry = Entry(auth_window)
    pas_entry.place(x=100, y=20)
    submit_button = Button(auth_window, text="Submit", command=check_and_log)
    submit_button.place(x=250, y=20)


# ########################page 2 login#########################################################################
def login_page():
    window_name = f"{acc_control[len(acc_control) - 1].name},{acc_control[len(acc_control) - 1].account_num}"

    # attribute widget's functions
    def check_bal():
        def back():
            # closing the previous window and restore previous
            login_window.deiconify()
            check_balance_window.destroy()

        login_window.withdraw()
        check_balance_window = tkinter.Toplevel()
        check_balance_window.title(window_name)
        check_balance_window.geometry("500x200")
        balance_label = Label(check_balance_window,
                              text=f"Your Current Balance:{acc_control[0].balance} Rupees",
                              font=("Arial", 16))
        balance_label.place(x=40, y=50)
        back_to_previous = Label(check_balance_window, text="back to a/c Page", font=("Arial", 10, "underline"),
                                 fg="blue", cursor="hand2")
        back_to_previous.place(x=40, y=100)
        back_to_previous.bind("<Button-1>", lambda e: back())

    def acc_deposit():
        def proceed():
            amount = int(amount_entry.get())
            curr_acc = acc_control[len(acc_control) - 1]
            curr_acc.deposit(amount)
            message_label = Label(login_window, text=curr_acc.message)
            message_label.place(x=20, y=80)
            amount_entry.delete(0, "end")
            # writing into database
            database.update(curr_acc.balance, curr_acc.account_num)
            # ###########################
            login_window.deiconify()
            deposit_window.withdraw()

        login_window.withdraw()
        deposit_window = tkinter.Toplevel()
        deposit_window.title(window_name)
        deposit_window.geometry("500x200")
        amount_label = Label(deposit_window, text="Amount")
        amount_label.place(x=30, y=30)
        amount_entry = Entry(deposit_window)
        amount_entry.place(x=100, y=30)
        proceed_button = Button(deposit_window, text="Proceed", command=proceed)
        proceed_button.place(x=250, y=26)

    def acc_withdraw():
        def proceed():
            amount = int(amount_entry.get())
            curr_acc = acc_control[len(acc_control) - 1]
            curr_acc.withdraw(amount)
            message_label = Label(login_window, text=curr_acc.message)
            message_label.place(x=20, y=80)
            amount_entry.delete(0, "end")
            # writing into database
            database.update(curr_acc.balance, curr_acc.account_num)
            # ###########################
            withdraw_window.destroy()
            login_window.deiconify()

        login_window.withdraw()
        withdraw_window = tkinter.Toplevel()
        withdraw_window.title(window_name)
        withdraw_window.geometry("500x200")
        amount_label = Label(withdraw_window, text="Amount")
        amount_label.place(x=30, y=30)
        amount_entry = Entry(withdraw_window)
        amount_entry.place(x=100, y=30)
        proceed_button = Button(withdraw_window, text="Proceed", command=proceed)
        proceed_button.place(x=250, y=26)

    # login pages attribute widgets
    login_window = tkinter.Toplevel()
    login_window.title(f"Hello {acc_control[0].name}")
    login_window.geometry("500x300")
    check_balance = Label(login_window, text="Check_balance", cursor="hand2", font=("Arial", 12, "underline"))
    check_balance.place(x=20, y=20)
    check_balance.bind("<Button-1>", lambda e: check_bal())
    deposit = Label(login_window, text="Deposit", cursor="hand2", font=("Arial", 12, "underline"))
    deposit.place(x=200, y=20)
    deposit.bind("<Button-1>", lambda e: acc_deposit())
    withdraw = Label(login_window, text="Withdraw", cursor="hand2", font=("Arial", 12, "underline"))
    withdraw.place(x=290, y=20)
    withdraw.bind("<Button-1>", lambda e: acc_withdraw())


#  #################################Parent Window################################
window = Tk()
window.title("Worlds No1 Bank")
window.geometry("600x300")
create_label = Label(text="Create A New Account", font=("Arial", 15, "underline"), cursor="hand2")
create_label.place(x=50, y=50)
login_label = Label(text="Login to your Account", font=("Arial", 15, "underline"), cursor="hand2")
login_label.place(x=280, y=50)
create_label.bind("<Button-1>", lambda e: create_account())
login_label.bind("<Button-1>", lambda e: authenticate())
window.mainloop()
