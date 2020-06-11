import os

#Usernames and verifaction codes
userNames = {
  'backDoor' : "I am your creator!",
  'userOne' : "Horacio",
  'userTwo' : "Jenesis",
  'userThree' : "Julie",
  'userFour' : "Saiz",
  'userFive' : "Rocio",
}

verCodes = {
  'userOne' : "3425",
  'userTwo' : "6722",
  'userThree' : "0315",
  'userFour' : "4612",
  'userFive' : "7465",
}


#Global Variables
nameEntered = None

#main function
def users():
    global nameEntered

    nameEntered = input("What is your name? ")
    
    if nameEntered == userNames["backDoor"]:
      print("Welcome my Creator who came from the backdoor.")
      encryption()

    else:
        verCodeEntered = input("What is your verifaction code? ")
        if nameEntered == userNames["userOne"]:
          if verCodes["userOne"] == verCodeEntered:
            os.system('cls')  # For Windows
            os.system('clear')  # For Linux/OS X
            print('Welcome my creator!')
            encryption()
          else:
            print("You're not a Donut Crew member! Who are you?")
            print("\n")
            users()
        elif nameEntered == userNames["userTwo"]:
          if verCodes["userTwo"] == verCodeEntered:
            os.system('cls')  # For Windows
            os.system('clear')  # For Linux/OS X
            print('Welcome Jenesis!')
            encryption()
          else:
            print("You're not a Donut Crew member! Who are you?")
            print("\n")
            users()
        elif nameEntered == userNames["userThree"]:
          if verCodes["userThree"] == verCodeEntered:
            os.system('cls')  # For Windows
            os.system('clear')  # For Linux/OS X
            print('Welcome Julie!')
            encryption()
          else:
            print("You're not a Donut Crew member! Who are you?")
            print("\n")
            users()
        elif nameEntered == userNames["userFour"]:
          if verCodes["userFour"] == verCodeEntered:
            os.system('cls')  # For Windows
            os.system('clear')  # For Linux/OS X
            print('Welcome Saiz!')
            encryption()
          else:
            print("You're not a Donut Crew member! Who are you?")
            print("\n")
            users()
        elif nameEntered == userNames["userFive"]:
          if verCodes["userFive"] == verCodeEntered:
            os.system('cls')  # For Windows
            os.system('clear')  # For Linux/OS X
            print('Welcome Rocio!')
            encryption()
          else:
            print("You're not a Donut Crew member! Who are you?")
            print("\n")
            users()
        else:
          print("You're not a Donut Crew member! Who are you?")
          print("\n")
          users()

#Encryption
def encryption():
  while True:
      print('\n')
      answer = input('Do you want to encrypt, decrypt, or terminate? ')
      if answer.lower().startswith("e"):
          alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*(),.?1234567890 "
          key = 3
          newMessage = ''
          message = input('Please enter a message: ')
          length = 3

          for character in message:
              position = alphabet.find(character)
              newPosition = (position + key) % 76
              newCharacter = alphabet[newPosition]
              newMessage += newCharacter

          print('Your encrypted message is: ', newMessage[::-1])

      elif answer.lower().startswith("d"):
        if nameEntered == userNames["backDoor"]:
          decryption()
        
        else:
          reVerCode()
          decryption()

      elif answer.lower().startswith("t"):
          os.system('cls')  # For Windows
          os.system('clear')  # For Linux/OS X
          exit()

      else:
        print('Invalid, please try again!')

#Decryption
def decryption():
  alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*(),.?1234567890 "
  key = 3
  newMessage = ''
  message = input('Please enter encrypted message: ')

  for character in message:
      position = alphabet.find(character)
      newPosition = (position - key) % 76
      newCharacter = alphabet[newPosition]
      newMessage += newCharacter

  print('Your decrypted message is: ', newMessage[::-1])

#Reverifaction
def reVerCode():
  verCodeEntered = input("What is your verifaction code? ")

  if verCodes["userOne"] == verCodeEntered:
      os.system('cls')  # For Windows
      os.system('clear')  # For Linux/OS X
      print("Thank you for your reverifaction!")
      decryption()
      encryption()
  elif verCodes["userTwo"] == verCodeEntered:
      os.system('cls')  # For Windows
      os.system('clear')  # For Linux/OS X
      print("Thank you for your reverifaction!")
      decryption()
      encryption()
  elif verCodes["userThree"] == verCodeEntered:
      os.system('cls')  # For Windows
      os.system('clear')  # For Linux/OS X
      print("Thank you for your reverifaction!")
      decryption()
      encryption()
  elif verCodes["userFour"] == verCodeEntered:
      os.system('cls')  # For Windows
      os.system('clear')  # For Linux/OS X
      print("Thank you for your reverifaction!")
      decryption()
      encryption()
  elif verCodes["userFive"] == verCodeEntered:
      os.system('cls')  # For Windows
      os.system('clear')  # For Linux/OS X
      print("Thank you for your reverifaction!")
      decryption()
      encryption()
  else:
      os.system('cls')  # For Windows
      os.system('clear')  # For Linux/OS X
      print("You're not a Donut Crew member! Who are you?")
      print("\n")
      users()

users()