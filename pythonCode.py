print("Hello World")
a=20
b=40
c=50
quantityA = int(input("Enter the number of QuantityA "))
quantityB = int(input("Enter the number of QuantityB "))
quantityC = int(input("Enter the number of QuantityC "))
wrapped = input("Is product is wrapped or Not (Y/N)? ")


totalA = quantityA*a
totalB = quantityB*b
totalC = quantityC*c 

totalSum = totalA+totalB+totalC

 
if(totalSum>200):
    flat10 = totalSum-10
    discountFirst= 10


discountSecond =0
discountA =0
discountB =0
discountC=0
if(quantityA>10 or quantityB>10 or quantityC >10):
    if(quantityA>10):
        totalAAfter =totalA -(totalA*0.05)
        
        discountA =totalA -totalAAfter
    elif(quantityB>10):
        totalBAfter =totalB -(totalB*0.05)
        
        discountB =totalB -totalBAfter
    elif(quantityC>10):
        totalCAfter =totalC -(totalC*0.05)
        
        discountC =totalC -totalCAfter

    discountSecond = discountA+discountB+discountC
    

totalQuantity = quantityA+quantityB+quantityC

discountThird =0
if(totalQuantity>20):
    totalSumAfter=(totalSum)-(totalSum*0.1)
    discountThird = totalSum - totalSumAfter

discountForth =0
discountFourthA =0
discountFourthB =0
discountFourthC =0
if (totalQuantity >30):
    if(quantityA>15 or quantityB>15 or quantityC >15):
        if(quantityA>15):
            remaingProductA = quantityA -15
            totalpriceA = (a*15)+(remaingProductA*a*0.5)
            
            discountFourthA=(a*quantityA)-totalpriceA

        elif(quantityB>15):
            remaingProductB = quantityB -15
            totalpriceB = (b*15)+(remaingProductB*b*0.5)
            
            discountFourthB=(b*quantityB)-totalpriceB

        elif(quantityC>15):
            remaingProductC = quantityC -15
            totalpriceC = (c*15)+(remaingProductC*c*0.5)
            
            discountFourthC=(c*quantityC)-totalpriceC

        discountForth = (discountFourthA+discountFourthB+discountFourthC)




if (wrapped =="Y") :
    giftWrappPrice =   totalQuantity
else :
    giftWrappPrice =0

if(int(totalQuantity) %10 == 0):
    shippingFee = (int(totalQuantity)/ 10 )*5
else:
    shippingFee =(int((totalQuantity/ 10)) +1) *5

print ("----------------------------------------------------------")

print("ProductA : ", quantityA , totalA)
print("ProductB : ", quantityB , totalB)
print("ProductC :", quantityC, totalC)



print(totalSum)



maxDiscount = max(discountFirst,discountSecond,discountThird,discountForth)
print("Discount is ",maxDiscount)
if(maxDiscount==discountFirst):
    print("flat_10_discount")

if(maxDiscount==discountSecond):
    print("bulk_5_discount")

if(maxDiscount==discountThird):
    print("bulk_10_discount")

if(maxDiscount==discountForth):
    print("tiered_50_discount")


print("ShippingFee :" , shippingFee , "Wrapped Fee :", giftWrappPrice)

FinalPrice = (totalSum- maxDiscount) + shippingFee + giftWrappPrice 

print(FinalPrice)