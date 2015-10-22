print "hello world"

#This test script creates a function that prints the values of a list and changes those values outside of the function. 


# Function definition is here
mylist = []
def changeme( mylist ):
   #This changes a passed list into this function
   mylist = [1,2,3,4]; # This would assig new values in mylist
   print "Values inside the function: ", mylist
   return

#Outside of the function we change the values of the list   
mylist = [10,20,30];

# Now you can call changeme function using the new list values 
changeme( mylist );

print "Values outside the function: ", mylist