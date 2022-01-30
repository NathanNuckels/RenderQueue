import os
qu=[]
for file in os.listdir("Queue"):
	if os.path.isfile("Queue/"+file):
		if file[len(file)-6:]==".blend":
			qu.append(file)
bt=[]
for i in range(len(qu)):
	bt.append("blender Queue/"+qu[i]+" -b -o renders/"+str(i)+"/####.png -a")
for line in bt:
	print(line)
print("OK?")
if input("[y/N] > ")=="y":
	for line in bt:
		os.system(line)
