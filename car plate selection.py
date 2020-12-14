'''load plate no.
monday, wed and fridays for odd plates
tues,thrus and sat for even plates
sunday for all plates'''
car_plates=['AB1234','CD5678','EF901','Qh234','JK567','LM90']
odd_days=['MO','WE','FR']
even_days=['TU','TH','SA']
pass_list=[]
today=input("Enter day of a week(SUnday to SAt):")
for plate in car_plates:
    last_digit=int(plate[-1])
    if today in odd_days and last_digit%2!=0:
        pass_list.append(plate)
    elif today in even_days and last_digit%2==0:
        pass_list.append(plate)
    elif today=='SU':
        pass_list.append(plate)
print(*pass_list,sep='\n')

OUTPUT:-
>>> 
========================== RESTART: C:/python37/car.py =========================
Enter day of a week(SUnday to SAt):SA
AB1234
CD5678
Qh234
LM90
>>> 
===================================================================== RESTART: C:/python37/car.py =====================================================================
Enter day of a week(SUnday to SAt):MO
EF901
JK567
>>> 
