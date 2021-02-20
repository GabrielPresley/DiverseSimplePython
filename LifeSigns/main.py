age = int(input("What is your age (Years 0-18):"))
age += 1
breaths_low = breaths_high = beats = 0

print(breaths_low)
for i in range(age):
    print(i)
    if 0 >= i:
        breaths_low += (525600*25)
        breaths_high += (525600*60)
        beats += (67.5*525600)
        print(breaths_low, "0-1")
    if 1< i+1 <=4 :
        breaths_low += (525600*20)
        breaths_high += (525600*30)
        beats += (67.5*525600)
        print(breaths_low, "1-4")
    if 4< i+1 <14 :
        breaths_low += (525600*15)
        breaths_high += (525600*25)
        beats += (67.5*525600)
        print(breaths_low,"4-14")
    if 14< i+1 <18 :
        breaths_low += (525600*11)
        breaths_high += (525600*18)
        beats += (67.5*525600)
        print(breaths_low,"14-18")

print("you have breathed", breaths_low, "-", breaths_high, "times")
print("heart beated", beats, "times")

#infant 25–60
#1–4 years 20–30
#5–14 years 15–25
#15–18 years 11–23
#For heart rate, use an average of 67.5 beats per minute.
