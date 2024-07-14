import initial
import balance
import saving
import withdraw

print("Welcome To The ABC Bank\n")
print("this is the main operatins of our bank\ninitial acccount press 1\ncheck the balance prss 2\ndeposit money in the account press 3\nwithdraw money in the account press 4\n")
try:
    argument=int(input("enter the operatinon index number:"))

    if argument==1:
        initial.account_initialization()
    elif argument==2:
        balance.check_balance()
    elif argument==3:
        saving.saving()
    elif argument==4:
        withdraw.withdraw()
except ZeroDivisionError:
    print("Thats not the operation index pleace try again")
except ValueError:
    print("Are you shuwar \nsome thig is wrong input correct value")
except:
    print("try again laiter")