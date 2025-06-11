import random as rand
import numpy as np
'''
number = []

for i in range (1,101):
  number.append(rand.uniform(1,100))
  
print(number)
print(np.mean(number))

with open ("data.dat","w") as file:
  for i in number:
    file.write(f"{round(i,1)}\n")    #####
    
file = open("pH.dat", "w")
file.write(f"H M S pH")

data = input("Entre time and pH in [HH <space> MM <space> SS <space> pH] format")

while(data.lower() != "stop"):
  parts = data.strip().split()
  if len(parts) == 4:
    h, m, s, ph = parts[0], parts[1], parts[2], parts[3]
  else:
    print("Error...!")
    print("Re-entre !")
file.write(f"{Hour} {Minutes} {Second} {pH} \n")
data = input("Entre time and pH in [HH <space> MM <space> SS <space> pH] format")
file.close()

'''
import matplotlib.pyplot as plt

x = np.linspace(-10.,10.,1000)
y = np.sin(x)

plt.figure(figsize=(15,10))
plt.plot(x,y,linestyle="-",label='sin(x)')
plt.grid(True)
plt.legend()
plt.show()
