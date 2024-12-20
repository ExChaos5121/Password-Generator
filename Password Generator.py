#Simple Password Generator that asks for guidelines for password generation
#Created by Ethan Yeany 12/20/24

import random
import string
import keyboard

class PasswordGenerator:
    def main(self):

      #Main that will ask for the users password requirements
        print("Welcome to my pasword generator")
        passwordLength = int(input("Please insert your desired password length from 8 to 26: "))

        #Rejects any insufficent password lengths and also rejects invalid answers such as YEs or NO for example
        while passwordLength <= 8 or passwordLength > 26:

            passwordLength = None
            print("Please enter a valid password length")
            passwordLength = int(input("Please insert your desired password length from 8 to 26: "))

        print("Valid password length accepted")

        validYes = "Yes"
        validNo = "No"
        print("Please answer the next following questions as Yes or No")
        capsIncluded = input("Would you like capitialized letters? ")

        while capsIncluded != validYes and capsIncluded != validNo:
            
            capsIncluded = None 
            print("Please answer the next question as Yes or No")
            capsIncluded = input("Would you like capitialized letters? ")


        if capsIncluded == validYes:
                
                capsAllowed = True

        else:
                capsAllowed = False

        charsIncluded = input("Would you like special characters included? ")
        while charsIncluded != validYes and charsIncluded != validNo:
            
            charsIncluded = None 
            print("Please answer the next question as Yes or No")
            charsIncluded = input("Would you like special characters included? ")


        if charsIncluded == validYes:
                
                charsAllowed = True

        else:
                charsAllowed = False

        numbsIncluded = input("Would you like numbers included? ")
        while numbsIncluded != validYes and numbsIncluded != validNo:
            
            numbsIncluded = None 
            print("Please answer the next question as Yes or No")
            numbsIncluded = input("Would you like numbers included? ")


        if numbsIncluded == validYes:
                
                numbsAllowed = True

        else:
                numbsAllowed = False

        #Generates password according to user specification and then prompts the user again 
        print("Generating password")
        obj = PasswordGenerator()
        obj.generator(passwordLength, capsAllowed, charsAllowed, numbsAllowed)
        print("Press the ENTER KEY to generate a new password or any other key to exit")

        while True:

            event = keyboard.read_event()
            if event.name == 'enter' and event.event_type == keyboard.KEY_DOWN:

                  obj.generator(passwordLength, capsAllowed, charsAllowed, numbsAllowed)
                  event.name = 'none'
                  event = keyboard.read_event()
            else:
                  break

             
    #Method that generates the password based on what the user wanted              
    def generator(self, passwordLength, capsAllowed, charsAllowed, numbsAllowed):

        options = []

        if capsAllowed == True:
              options = [string.ascii_letters]
        else:
              options = [string.ascii_lowercase]

        if charsAllowed == True:
              options.append(string.punctuation)     

        if numbsAllowed == True:
              options.append(string.digits)
      
        choices = ''.join(options)
      
        randompassword = ''.join([random.choice(choices) for n in range(passwordLength)]) 
        print(randompassword)
  

mainobj = PasswordGenerator()
mainobj.main()
