while(True):
  password = input("Enter password : ")
  if(len(password)>=8):  
      print("Your password "+password+" fulfills all the criterias and  is set successfully")
      break
  else:
      print("Your entered password is less than 8 characters!")    
      
# print("Your password :",password)