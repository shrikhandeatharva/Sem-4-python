from random import shuffle
print("*********Three cup monte game*********")
#Empty cup is defined by 'empty'
#Cup containing ball is defined as 'ball'
sample_list = ["empty","ball","empty"]
print("Initially cups are arranged as : ",sample_list)
shuffle(sample_list)
print("Now cups are shuffled!")
choice = int(input("Enter your choice from 1 to 3(for position of cup) : "))
if(sample_list[choice-1] == "ball"):
    print("You guessed correctly!!")
else:
    print("Sorry,You guessed wrong!")    

