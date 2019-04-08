hours = input('Enter Hours: ')
rate = input('Enter Rate: ')
try:
    fh = float(hours)
    fr = float(rate)
except:
    print("Error, please enter numeric input")
    quit()

if fh > 40:
    regularPay = fh * fr
    overtimPay = (fh-40) * (fr*0.5)
    pay = regularPay + overtimPay
else:
    pay = fh * fr
print('Pay:', pay)
