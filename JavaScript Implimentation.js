vid_count = 0
del_count = 0
priv_count = 0
b = document.title
playlist_title=b.split(" - ")[0]

c = (document.body).getElementsByTagName("yt-next-continuation")[0]
if (c != undefined)
{
	c.scrollIntoView()
}
console.log("No more continuations!")

a = ((document.body).getElementsByTagName("ytd-playlist-video-renderer"))
for (i=0; i<a.length;i++)
{
	try{
		console.log(a.item(i).getElementsByTagName("span")[1].title)
		vid_count++
	}
	catch{
		title = a.item(i).getElementsByTagName("span").item(0).title
		console.log(title) 
		if (title === "[Deleted video]")
		{
			del_count++
		}
		
		else if (title === "[Private video]")
		{
			priv_count++
		}
    }	
}
console.log("playlist title: " + playlist_title)
console.log("total videos in playlist: " + vid_count)
console.log(del_count + " videos deleted.")
console.log(priv_count + " videos private.")
