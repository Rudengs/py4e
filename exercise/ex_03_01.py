hours = input('Enter Hours: ')
rate = input('Enter Rate: ')
fh = float(hours)
fr = float(rate)
#print(fh, fr)
if fh > 40:
    #print("overtime")
    regularPay = fh * fr
    overtimPay = (fh-40) * (fr*0.5)
    #print(regularPay, overtimPay)
    pay = regularPay + overtimPay
else:
    #print("regular")
    pay = fh * fr
print('Pay:', pay)
