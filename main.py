queue=[]
queueData=[]
count=0
def addQueue():
	print("Move the file into the \"Queue\" folder")
	filename=input("Filename: ")
	type=input("use \"a\" for animation, \"f\" for a singl frame\nType: ").lower()
	command="blender "+filename+" -o "+str(len(queue))+"/####.png"
	if type=="a":
		print("Leave the following blank to use the data in the blender file")
		start=input("Start frame:")
		if start!="":
			command=command+" -s "+start
		end=input("End frame:")
		if end!="":
			command=command+" -e "+end
		command=command+" -a"
	else:
		frames=input("Enter a list of frames to render. (eg \"106\" or \"127,149,156\"\nFrames: ")
		command=command+" -f "+frames
	print(command)
while True:
	print("0. Render\n1. View queue\n2. Add to queue\n3. Remove from queue\n4. Reorder queue\n5. Clear queue\n6. Quit")
	choice=input("><>")
	if choice=="0":
		render()
	elif choice=="1":
		listQueue()
	elif choice=="2":
		addQueue()
	elif choice=="3":
		deleteQueue()
	elif choice=="4":
		reorder()
	elif choice=="5":
		clearQueue()
	elif choice=="6":
		print("Bye!")
		break

