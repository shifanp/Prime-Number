# Program to print all prime numbers

start = int(input('enter a number start:-'))
end = int(input('enter a number stop :-'))
print ('prime number' ,start,'and' ,end, 'number')
for num in range (start,end+1):
    if num > 1:  
        prime_number =True
        for i in range(2,int(num**0.5)+1):
            if num %i==0:
                prime_number =False
                break
        if prime_number:
            print(num)