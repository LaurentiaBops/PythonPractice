#Game where players fill in blanks of a 
#story with random words, creating a silly narrative

#Story ending will differ depending on the 
#initial letter of the user's name

user_name = input("What is your name?: ")
user_name_letters = list(user_name) #Turn username into individual list of letters
verb = input("Enter a verb ending in -ing (present particle): ")
adjective = input("Enter an adjective: ")

message = f"Hi my name is {user_name}. On {adjective} days, my favourite activity to do is {verb}."
if len(user_name_letters) >= 5:
    ending =" This is how I have gotten to be so smart"
else:
    ending = " This is why I struggle in school"

print(message+ending)