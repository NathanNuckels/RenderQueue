import os
import sys

qu=[]
if len(sys.argv)==2:
	if sys.argv[1]=="help":
		print("Useage: python main.py [files...]")
		print("\tItems in the program arguments will be prioritized over files in the Queue folder")
if not len(sys.argv)==1:
	for item in sys.argv:
		if os.path.exists(item):
			if item.split(".")[len(item.split("."))-1]=="blend":
				qu.append(item)
			else:
				print("ERR: Not a blender file ("+item+")")
		else:
			print("ERR: Not a file ("+item+")")
for file in os.listdir("Queue"):
	if os.path.isfile("Queue/"+file):
		if file[len(file)-6:]==".blend":
			qu.append("Queue/"file)
bt=[]
for i in range(len(qu)):
	bt.append("blender "+qu[i]+" -b -o renders/"+str(i)+"/####.png -a")
for line in bt:
	print(line)
print("OK?")
if input("[y/N] > ")=="y":
	for line in bt:
		os.system(line)
