users =[{'user':'ashish' , 'tweets':'Eng Vs Australia'},
{'user':'ajij' , 'tweets':'LOC'},
{'user':'Ashok' ,'tweets':'yoga,pranayam'}]

f_user=filter(lambda u:u['user'] == 'ashish',users)
print(f_user)


num=[1,2,3,4,5,6,7,8,9,10]
#list of even numbers:
f_even=filter(lambda n: n%2==0,num)
print("Even Numbers List is:{} \s".format(f_even))

#list of odd numbers:
f_odd=filter(lambda n: n%2!=0,num)
print("Odd Numbers List is:{}".format(f_odd))