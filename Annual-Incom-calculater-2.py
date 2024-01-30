def main():

    income=finalincomeCalculater(float(input("what is your total annual income : ")))

def finalincomeCalculater(i):

    taxpercentage=10,15,20,30
    if i <= 10000:
        print("no taxes on you poor nigga : ")
    elif 10001<i<20000:
         taxpercentage=10
    elif 20001 < i < 50000:
         taxpercentage=15
    elif 10001 < i < 20000:
         taxpercentage=20
    elif 10000 < i < 99999999999999:
         taxpercentage=30

    if taxpercentage == 10:
            income1 = float(i * taxpercentage / 100)
            finalincome1 = float(i - income1)
            print("Your final income is ", finalincome1)
    elif taxpercentage == 15:
            income2 = float(i * taxpercentage / 100)
            finalincome2 = float(i - income2)
            print("Your final income is ", finalincome2)
    elif taxpercentage == 20:
            income3 = float(i * taxpercentage / 100)
            finalincome3 = float(i - income3)
            print("Your final income is ", income3)
    elif taxpercentage == 30:
            income4 = float(i * taxpercentage / 100)
            finalincome4 = float(i - income4)
            print("Your final income is ", income4)
main()



