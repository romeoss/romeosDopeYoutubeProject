import feedparser                                                                                     #This will make life easier

class color:                                                                                          #These make things pretty
	YELLOW = '\033[93m'
	RED = '\033[91m'
	BLUE = '\033[94m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
	END = '\033[0m'

posts = 5                                                                                             #Maximum number of recent videos that will be read
feeds = "./feeds.txt"                                                                                 #Example: https://www.youtube.com/feeds/videos.xml?channel_id=UC_ZSVTRRC5p3ed6hu8Y8z7A
history = "./history.txt"                                                                             #NEEDS AT LEAST ONE LINE TO START OUT


##THIS IS THE PART WHERE THE HISTORY IS LOADED INTO THE LIST historyList
file = open(history)                                                                                  #Opening this so that we can read the history
historyList = []                                                                                      #Creating lists needed to document history
newHistory = []
with file as historyFile:
	for line in historyFile:
		url = line
		historyList += [url]                                                                  #Take each line from history.txt and write it to an element in historyList
file.close()                                                                                          #Close the file so that we can open the next one


##THIS IS THE PART WHERE THE SHIT IS PRINTED
file = open(feeds)                                                                                    #Open the feeds.txt so that we can go through it and get each channel's feed
with file as feedsFile:
	for line in feedsFile:
		i = 0
		url = line                                                                            #Each line is a url that we will process
		parsedfeed = feedparser.parse(url)                                                    #Actually getting the RSS feed itself using the URL
		print(color.YELLOW + color.BOLD + parsedfeed.channel.title + color.END)               #Displaying the channel name in a pretty way.
		atLeastOneVideo = "nope"
		while i < posts:
			videoURL = parsedfeed.entries[i].link + "\\n"                                  #We need to do this b/c historyList loads the newline characters and we want to match to that. Alternative solution: Remove the newline character from each entry in historyList
			print(videoURL),
			print(historyList),
			#print(newHistory)
			newHistory += [parsedfeed.entries[i].link]
			#print(isinstance(videoURL, str))
			#print(isinstance(historyList[1], str))
			if videoURL not in historyList:                                               #Check to see if the video link is in the historyList
#				print(color.BOLD + parsedfeed.entries[i].title + color.END)           #Print the name of the video
#				print(color.UNDERLINE + parsedfeed.entries[i].link + color.END)       #Print the link to the video
				atLeastOneVideo = "yeah"
				print("not in list")
			#if videoURL == historyList[1]:
			#	print("HEY LOOK AT THIS BRAH LASDFLASDLKFASDKFKASDFKASDFHKLASDHFKLASDHKLHF?")
			i += 1
#		if atLeastOneVideo == "nope":
#			print(color.BLUE + "No new videos from " + parsedfeed.channel.title + " :'(" + color.END)
		print("")                                                                              #Put a newline between channels so that the link to Garcatch's latest video doesn't touch ViHart's name
file.close()                                                                                          #Close the feeds file so that we can open history back up. 


##THIS IS THE PART WHERE SHIT GETS ADDED TO history.txt
file = open(history, 'a')                                                                             #Open history in writable mode so that we can add to it. 
with file as historyFile:
	for m in range(0, len(newHistory)):                                                           #For each element in newHistory
		videoURL = newHistory[m] + "\n"
		if videoURL not in historyList:
			historyFile.write(newHistory[m])                                              #Write that element to history.txt
			historyFile.write("\n")                                                       #Put a newline so that they can be read by historyList next time
file.close()                                                                                          #Close the file

print(color.RED + "THANK YOU FOR USING ROMEO'S DOPE YOUTUBE PROJECT!")
print("==IT WAS MADE WITH HELP FROM ~GAMAH AND MITFREE==" + color.END)
