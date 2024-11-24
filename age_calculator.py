def AgeCalculator(y,m,d):
    import datetime
    today=datetime.datetime.now().date()
    dob=datetime.date(y,m,d)
    age=int((today-dob).days/365.25)
    print(age)

y=int(input("Enter Year of Birth:"))
m=int(input("Enter Month of Birth:"))
d=int(input("Enter Date of Birth:"))
AgeCalculator(y,m,d)
  