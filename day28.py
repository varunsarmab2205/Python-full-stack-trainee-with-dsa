'''Access Specifiers :
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Access specifiers control visibility of variables and methods
1.public - Accessible from anywhere
2.protected - Meant for internal use (convention) ,
                      Can still be accessed outside (not strict)
3.private - More restricted using name mangling

self ---> this is a keyword is instance variable and unique for each object
----
                  Summary Table
                 ---------------------
  Type           Syntax                          Access Level
  ------        ------------                         -----------------
Public	         var                        	Anywhere
Protected       _var	                              Internal use (convention)
Private	     __var                             Restricted (name mangling

'''

                                                           
class some:
    def  __init__(self):
        self.public = "public"
        self.protected = "protect"                                                                                              
        self.private="private"
any = some ( )
print(any.public)
print(any.protected)
print(any.private)
        
