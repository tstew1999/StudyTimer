import time
from playsound import playsound

print('Study period in minutes?')
studyMin = float(input())
print('Break period in minutes?')
breakMin = float(input())
print('How many repetitions?')
repe = int(input())

for i in range(repe):
    print('You have ' + str(repe - i) + ' repetitions left!')
    playsound('Assets/Sound/repetition.wav')
    print('Study!')
    time.sleep(studyMin  * 60)
    playsound('Assets/Sound/repetition.wav')
    print('Take a break!')
    time.sleep(breakMin  * 60)
    
print('Peace out, girl scout!')
playsound('Assets/Sound/finish.wav')
