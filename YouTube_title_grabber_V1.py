#YouTube Title Grabber by Jeffrey Wilhite
#V1.0

#program functionality wish list:
# make it able to retrieve info with url as only imput

#imports for later features:
#import argparse
#from urllib.parse import urlparse

#necessary imports
import codecs
from apiclient.discovery import build

#initialize global vars
V_titles = []
del_vid_count = 0

playlist_ID = str(input("What is the Playlist ID for the playlist you'd like to scan? \n Playlist_ID:"))
service = build('youtube','v3',developerKey = "AIzaSyBHa9w8rO9woENPKio1p2DiApMFKzau4Y4")
snippit_request = service.playlistItems().list(part="snippet", playlistId=playlist_ID, maxResults=50)
#^ grabs first 50 items in the playlist

snippit_response = snippit_request.execute()
#goes through first grabbed list of videos
for item in snippit_response['items']:
	V_titles.append(item['snippet']['title'])
	#count deleted videos while building list
	if item['snippet']['title'] == "Deleted video": 
		del_vid_count+=1

# V--iterate until break condition is met though entire playlist and grab vid titles--V
while True:
	#requests the next 50 items 
	snippit_request = service.playlistItems().list(part="snippet", playlistId=playlist_ID, maxResults=50, pageToken = snippit_response.get('nextPageToken'))
	snippit_response = snippit_request.execute()
	
	#grab the next 50 titles and add them to the list
	for item in snippit_response['items']:
		V_titles.append(item['snippet']['title'])
		if item['snippet']['title'] == "Deleted video":
			del_vid_count+=1
		
	#		V---loop break condition---V
	#...When there are no more parts to the list...
	if snippit_response.get('nextPageToken') is None:
		break

#Offer to save info gathered to a file

print("All video titles retrieved")
print(str(len(V_titles)) + " titles in list. " + str(del_vid_count) + " vids deleted.")

input = str(input("Would you like to save this to a text file? \n (Y/N):"))

if (input == "Y") or (input=="y"):
	del input
	default_filename = "YouTube Playlist Video Titles"
	filename = str(input("What filename would you like your file to have? \n Filename:"))

	if filename == "" or filename =="default":
		filename = default_filename

	filename += ".txt"
	file = codecs.open(filename, "w", "utf-8")
	file.write("****PLAYLIST ID: %s****\r\n" % playlist_ID)
	for title in V_titles:
		if title != "Deleted video":
			file.write(title + "\r\n")
	
	file.close()