# much of this code was inspired by my microservice code from the first microservice assignment

import time

print("Let's see if there are any travel tips!  Hmmmm....\n")

exit = False

while not exit:
    print("Whenever you're ready, enter '1' and press enter and we'll show you a travel tip!\n" +
        "If you're all done, press '2' and hit enter: ")
    
    num = input()

    if num == '2':
        print("Thanks for participating! Have a good day!")
        exit = True

    elif num == '1':
        # do stuff
        print('\n....one moment, please....\n')
        with open('travel-tip-service.txt', 'w', encoding='utf-8') as tipF:
            tipF.write('tip')
            tipF.close()

        time.sleep(4)

        with open('travel-tip-service.txt', 'r+', encoding='utf-8') as tipF:
            tip = tipF.read()
            tipF.truncate(0)
            print("Travel Tip: " + tip)
            tipF.close()
    
    else:
        print("Invalid entry.  Please enter either '1' to generate a travel tip or '2' to end!")

