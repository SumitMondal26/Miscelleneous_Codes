def validity(date,month,year):
    if date>=32 :
        print("invalid date ")
    elif month>12:
        print("invalid month")
    elif (date_input[2] and date_input[5] != "-"):
        print("invalid format")
    else:
        print("valid date input ")
        output(date,month,year)

def output(date,month,year):
    month_name=(" ","jan","feb","march","april","may","june","july","aug","sept","oct","nov","dec")
    month_days=(0,31,29,31,30,31,30,31,31,30,31,30,31)

    leap=bool(year%400==0 and year%100==0 or year%4==0)

    for i in range(1,13):
        if month==i :
            if leap==True and i==2:
                print(month_name[i],"has 28 days")
            else:
                print(month_name[i],"has",month_days[i])

date_input=input("enter date in dd-mm-yyyy format :")
date_input=list(date_input)

date=int(date_input[0]+date_input[1])
month=int(date_input[3]+date_input[4])
year=int(date_input[6]+date_input[7]+date_input[8]+date_input[9])

validity(date,month,year)


