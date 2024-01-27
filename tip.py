def main():
    price=dollartofloat(input("how mush did you pay : "))
    percentage=percenttofloat(input("what percentage would you tip : "))
    tip=price*percentage
    print(f"Your tip is {tip} dollars")

def dollartofloat(d):
    withoutsign=d.replace("$"," ")
    return float(withoutsign)

def percenttofloat(p):
    withoutpercent=p.replace("%"," ")
    realpercentage=float(withoutpercent)/100
    return float(realpercentage)


main()



