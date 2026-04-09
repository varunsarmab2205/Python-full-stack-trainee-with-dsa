'::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::LAMBDA FUNCTION:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::'
'''
THIS IS ALSO CALLED ANONYMOUS FUNCTION.
A LAMBDA FUNCTION CAN TAKE N NUMBER OF ARGUMENTS NUT HAVE ONLY ONE  EXPRESSION.
CAN BE WRITTEN IN A SINGLE LINE

"SYNTAX ----- lambda (keyword) arguments : expression"


'EXAMPLE-1'

'---''Single Variable'

any = lambda so : so+ 10
print(any(6))



'EXAMPLE-2'

'--- ''Double variable'

n = lambda a,b : a<b
print(n(10,20))

'EXAMPLE-3'

'---''Three Variable'

n = lambda a,b,c : a+b+c
print(n(10,20,30))


'EXAMPLE-4'

'---''Difference'

diff = lambda a,b : a-b
print(diff(20,10))



'EXAMPLE-5'

'---''Product'

product = lambda a,b : a*b
print(product(20,10))



'EXAMPLE-6'

'---''Division'

result = lambda a,b : a/b
print(result(200,10))

'''

'::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::LIST COMPREHENSION::::::::::::::::::::::::::::::::::::::::::::;::::::::::::::::::::::::::'
'''
'--------> THIS OFFERS THE SHORTEST SYNTAX WHEN YOU WANT TO CREATE A NEW LIST FROM THE'
'EXISTING LIST.'

'"SYNTAX" : Variable_name = [expression loop and condition]'


'EXAMPLE-1'

'---''Even odd'

my_list = [22,14,4,26,27,4,18,30,19,10,11,31]
derived_list = [j  for j in my_list if j%2 == 0]
print(derived_list)



'EXAMPLE-2'

'---"Greater than'

my_list = [22,26,27,31,12,3,19,14,15,18]
derived_list = [j for j in my_list if j>12 ]
print(derived_list)
'''








      








