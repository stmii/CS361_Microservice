# much of this code was inspired by my microservice code from the first microservice assignment

import time

count = 0
tips = [
    "Wake up early to avoid crowds at sites and attractions.",
    "Learn a few key phrases in the local language to be able to communicate with people.",
    "Always pack a towel.",
    "Do some research before-hand; don't miss out on opportunities due to lack of planning!",
    "Always be willing to change plans if a new experience comes along!"
]

while True:
    time.sleep(1)
    val = 'null'
    with open('travel-tip-service.txt', 'r', encoding='utf-8') as tipFile:
        val = tipFile.read()
        tipFile.close()

    if val == 'tip':
        with open('travel-tip-service.txt', 'w', encoding='utf-8') as tipFile:
            val = tips[count % 5]
            count += 1
            tipFile.write(val)
            tipFile.close()


