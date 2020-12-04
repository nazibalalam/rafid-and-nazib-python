secret_message = "My name is Nazib Al Alam"

password = "I forgot the password"

while True :
  guess = input("Please enter the password")

  if not guess == secret_message :
    print("Wrong password! Please try again.")
    continue

  if guess == secret_message :
    print("Congratulations! you figured out the password!")
    print('Here is the "secret_message" :')
    print(secret_message)
    break