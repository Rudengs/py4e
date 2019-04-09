hours = input('Enter Hours: ')
rate = input('Enter Rate: ')
fh = float(hours)
fr = float(rate)

def pay_calc(h,r):
    if fh > 40:
        regularPay = fh * fr
        overtimPay = (fh-40) * (fr*0.5)
        return regularPay + overtimPay
    else:
        return fh * fr

print('Pay:', pay_calc(fh,fr))
