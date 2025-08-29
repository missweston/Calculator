x= float(input("what is x? "))
y= float(input("What is y? "))

print("1.) Add " 
      
    "2.) Subtract " 

    "3.) Multiply " 

    "4.) Divide ")

choice= int(input("Enter Choice:"))

if choice == 1:
    z= (x+y)
elif choice == 2:
    z= (x-y)

elif choice == 3:
    z= (x*y)

elif choice == 4:
    z= (x/y)

else:
    print("Invalid choice")
  
print(f"{z:,}" )