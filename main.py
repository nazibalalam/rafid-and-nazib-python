secret_message = "My name is Nazib Al Alam"

password = "I forgot the password"

while True :
  input_message = "Enter the password : "
  guess = input()  

  if not guess == secret_message :

    input_message = "Wrong password! Try again : "
    
    

  if guess == secret_message :

    print("Congratulations! you figured out the password!")
    print('Here is the "secret_message" :')
    print(secret_message)
    break