import time
import playsound

print('Study period in minutes?')
studyMin = float(input())
print('Break period in minutes?')
breakMin = float(input())
print('How many repetitions?')
repi = int(input())

for i in range(repi):
    print('You have ' + str(repi) + ' repititions left!')
    playsound('StudyTimer/Assets/Sound/repitition.wav')
    print('Study!')
    time.sleep(studyMin  * 60)
    playsound('StudyTimer/Assets/Sound/repitition.wav')
    print('Take a break!')
    time.sleep(breakMin  * 60)

playsound('StudyTimer/Assets/Sound/finish.wav')
print('Peace out, girl scout!')
