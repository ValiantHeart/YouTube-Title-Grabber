#YouTube Title Grabber by Jeffrey Wilhite
#Currently YTG is GUI-less, Command line version
#V2


#necessary imports
import tkinter 
import pytube
import os.path
import datetime 
import codecs

from tkinter import *
from pytube import *

#initialize global vars
videoTitles = []
playlistTitle = ""
playlistAuthor = ""
currentTime = datetime.datetime.now()
exit = False

def validateURL(playlist_url):
	#Checks the playlist URL to ensure it's a valid one
	if "/playlist?" and "www.youtube.com" in playlist_url:
		print("URL Valid \n\r")
		return True
	else:
		print("URL is not a valid URL")
		return False

def collectInfo(playlistURL):
	#creates a Playlist object and collects the desired information from it. 
	p = Playlist(playlistURL)
	global playlistTitle 
	playlistTitle = p.title
	global playlistAuthor 
	playlistAuthor = p.owner
	for vid in p.videos:
		print(vid.title)
		videoTitles.append(vid.title)
	
def printInfo():
	#prints the gathered information
	print("Playlist loaded: " + playlistTitle)
	print("Number of Videos: " + str(len(videoTitles)))
	print("Playlist Author: " + playlistAuthor)
	print("Playlist Retrieved: " + str(currentTime))

def saveToFile(list):
	#writes the contents of the provided list to a file with an appropriate data header
	filename = playlistTitle+".txt"
	try:
		file = codecs.open(filename, "w", "utf-8")
	except:
		print("THERE WAS AN ERROR LOADING THE FILE.")
	file.write("****PLAYLIST NAME: %s****\r\n" % playlistTitle)
	file.write("Playlist Author: " + playlistAuthor + "\r\n")
	file.write("Number of Videos: " + str(len(videoTitles)) + "\r\n")
	file.write("Playlist Retrieved: " + str(currentTime) + "\r\n" + "\r\n" + "\r\n")
	if len(list)>0:
		for items in list:
			file.write(items + "\r\n")
	else:
		file.write("There were no video\'s in this playlist...")
	if os.path.isfile(os.getcwd() + "/" + filename):
		print("file successfully saved")
		print("file located at: " + os.getcwd() + "\\" + filename)
	else:
		print("File didn't save successfully!!")
	file.close()

#GUI CODE:


def main():
	print("This program will gather all the titles from a YouTube Playlist and print them out to a file.")
	print("Provide a YouTube Playlist URL or type in \"EXIT\" to quit")
	global exit
	while not exit:
		playlistURL = input("Enter Playlist URL: ")
		if playlistURL.upper() == "EXIT":
			exit = True
		else:
			if validateURL(playlistURL):
				print("Collecting Video Information...")
				print("This may take a while...")
				collectInfo(playlistURL)
				printInfo()
				if input("Save Playlist to file? (Y/N) ").upper() == "Y":
					saveToFile(videoTitles)

if __name__ == "__main__":
	#for when running direct
	main()
else:
	#for when imported into a program
	pass