digits= "232"

but2 = "abc"
but3 = "def"
but4 = "ghi"
but5= "jkl"
but6 = "mno"
but7 = "pqrs"
but8 = "tuv"
but9 = "wxyz"

resArr=[]
memArr=[]

# you can for d in digits and use chars[int(d)] since every but value
# placed in its resoective element number easier for iteration
chars= [0,0,but2,but3,but4,but5,but6,but7,but8,but9]




if len(digits) == 0:
    print("[]")

else :
    for i in range(len(digits)) :
        #goes thru digits
        if i == 0 :
            #for first digit initilize resArr
            resArr = chars[int(digits[i])]
        else :
            #then add other to end
            for j in range(len(resArr)):
                for k in chars[int(digits[i])]:
                    memArr.append(resArr[j]+k)
            #after adding completed 
            #get new res and reset mem
            resArr = memArr
            memArr = []

     
    
print(resArr)

