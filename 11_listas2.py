l = [1,2,3,4]
s = ["H","O","L","A"]

l2 =[c*num for c in s 
               for num in l
                   if num> 0]

print (l)
print (l2)