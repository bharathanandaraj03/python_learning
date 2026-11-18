def mask_credit_Card(card_number):
    card_number = str(card_number)
    if len(card_number) < 16:
        print("Card num less than 16 digits")
    elif len(card_number) > 16:
        print("Card num greater than 16 digits")
    else:
        alldigits = card_number[:12]
        last4digits = card_number[12:]
        alldigits = alldigits.replace(alldigits,"************")
        print(alldigits)
        print(last4digits)
        return alldigits+last4digits

def pronic(inputnum):
    i=2
    count = 0
    mulnum = []
    for i in range(2,inputnum-1):
        if inputnum%i == 0:
            mulnum.append(i)
            #print(i)

    for j in range(len(mulnum)-1):
        #print(mulnum[j])
        if mulnum[j] == (mulnum[j+1]-1):
            print(mulnum[j],mulnum[j+1])
            product = mulnum[j]*mulnum[j+1]
            if product == inputnum :
                count += 1

    if(count==0):
        print("Number is not pronic")
    else:
        print("Number is pronic")

    
print(mask_credit_Card(9123123456789821))
pronic(72)
