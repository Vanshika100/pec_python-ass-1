grossinc=int(input("enter gross income:"))
dependent=int(input("enter number of dependents:"))
taxin=grossinc-10000-(3000*dependent)
taxrate=20
tax=taxin*taxrate/100
print("income tax is",tax)