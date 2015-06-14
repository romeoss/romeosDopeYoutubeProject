import feedparser #This will make life easiehttps://i.imgur.com/k79LuE1.pngr

class color: #These make things pretty
	YELLOW = '\033[93m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
	END = '\033[0m'

posts = 5 #Maximum number of recent videos that will be read
feeds = "feeds.txt" #Example: https://www.youtube.com/feeds/videos.xml?channel_id=UC_ZSVTRRC5p3ed6hu8Y8z7A
history = "history.txt" #NEEDS AT LEAST ONE LINE TO START OUT



##THIS IS THE PART WHERE THE HISTORY IS LOADED INTO THE LIST historyList
file = open(history) #Opening this so that we can read the history
historyList = [] #Creating lists needed to document history
newHistory = []
with file as g:
	for line in g:
		url = line
		historyList+=[url] #Take each line from history.txt and write it to an element in historyList
file.close() #Close the file so that we can open the next one


##THIS IS THE PART WHERE THE SHIT IS PRINTED
file = open(feeds)#Open the feeds.txt so that we can go through it and get each channel's feed
with file as f:
	for line in f:
		i = 0
		url = line#Each line is a url that we will process
		parsedfeed = feedparser.parse(url)#Actually getting the RSS feed itself using the URL
		print color.YELLOW + color.BOLD + parsedfeed.channel.title + color.END#Displaying the channel name in a pretty way.
		while i < posts:
			#print newHistory
			#print historyList
			videoTitle = parsedfeed.entries[i].link + "\\n"
			if videoTitle not in historyList:#Check to see if the video link is in the historyList
				print color.BOLD + parsedfeed.entries[i].title + color.END#Print the name of the video
				print color.UNDERLINE + parsedfeed.entries[i].link + color.END#Print the link to the video
				#print "VIDEO NOT FOUND IN HISTORY"
				newHistory+=[parsedfeed.entries[i].link]#Add the video's link to the list that will be written to history.txt later
				i+=1
				#print i
			else:
				i = posts
				#print i
				#print "VIDEO FOUND IN HISTORY"

		print ""#Put a newline between channels so that the link to Garcatch's latest video doesn't touch ViHart's name
file.close()#Close the feeds file so that we can open history back up. 


##THIS IS THE PART WHERE SHIT GETS ADDED TO history.txt
file = open(history, 'a')#Open history in writable mode so that we can add to it. 
with file as h:
	for m in range(0, len(newHistory)):#For each element in newHistory
		h.write(newHistory[m])#Write that element to history.txt
		h.write("\n")#Put a newline so that they can be read by historyList next time
##TODO: DON'T ADD THE URL TO HISTORY IF IT'S ALREADY IN THERE
file.close()#Close history.txt like a good Python skiddie
