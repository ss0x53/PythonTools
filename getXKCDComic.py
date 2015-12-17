#coding=utf-8
import urllib
import re

#start page number
start = 1
#end page number
end = 1613

prevUrl = 'http://xkcd.com/'

#download html file
def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

#parse comic image url from html
def getImgUrl(html):
	reg = r'src="(.+?\.png)" title='
   	imgre = re.compile(reg)
   	imglist = re.findall(imgre,html)
   	if(len(imglist) > 0):
   		return imglist

   	reg = r'src="(.+?\.jpg)" title='
   	imgre = re.compile(reg)
   	imglist = re.findall(imgre,html)
   	
   	return imglist    


#down load comic image and save it to file with name
def getImg(url,name):
	conn = urllib.urlopen(url)
	f = open(name,'wb')
	f.write(conn.read())
	f.close()
	

#test function
def loopPrintUrl(imglist):
	for imgurl in imglist:
		url = 'http:' + imgurl
		print (url)


#append image download url
def getImgFileNameFromUrl(url):
	strlist = url.split('/')
	return strlist[4]
	


# download xkcd comic image
def loopDownLoadXKCDImg():
	for i in range(start,end + 1):
		downloadUrl = prevUrl + str(i) + '/'
		#print(downloadUrl)
		html = getHtml(downloadUrl)
		#print(html)
		urlList = getImgUrl(html)
		for tmpurl in urlList:
			filename = str(i)+ "_" + getImgFileNameFromUrl(tmpurl)
			imgDownLoadurl = "http:" + tmpurl
			getImg(imgDownLoadurl,filename)
			print (str(i) + "    " + imgDownLoadurl + " -> down")


loopDownLoadXKCDImg()

