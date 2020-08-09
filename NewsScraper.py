
import urllib.request,sys,time
from bs4 import BeautifulSoup
import requests
from datetime import date


print("A PRDUCT MADE BY GAJANAN GITTE");
print("MIT LICENSE 2020. COPYRIGHT GAJANAN GITTE")


while True:

	# print("\nPLEASE ENTER A SEARCH TERM(PRESS ENTER WHEN DONE).\n (TO EXIT, JUST PRESS ENTER) \n ->>")
	# Change the terms to show results
	term = input("\nPLEASE ENTER A SEARCH TERM(PRESS ENTER WHEN DONE).\n (TO EXIT, JUST PRESS ENTER) \n ->>")

	pagesToGet= 1


	#  TOI, Hindustan Times, Aaj Tak hindi, Indian Express, NDTV


	if term:

		# SET UP THE FILE to store data
	    filename="NEWS " + str(date.today())+ ' ' + term  +" .csv"  
	    f=open(filename,"w", encoding = 'utf-8')
	    headers="Term,Source,Statement,Content, Date, Link\n"
	    f.write(headers)


	    #######################
	    # Times of India
	    #####################
	    for pageNo in range(1,pagesToGet+1):
	        print('processing page :', pageNo)
	        url = 'https://timesofindia.indiatimes.com/topic/' + term +'/'+str(pageNo)
	        print(url)
	        

	        try:
	            page=requests.get(url)                           
	        
	        except Exception as e:                                   # this describes what to do if an exception is thrown
	            error_type, error_obj, error_info = sys.exc_info()      # get the exception information
	            print ('ERROR FOR LINK:',url)                          #print the link that cause the problem
	            print (error_type, 'Line:', error_info.tb_lineno)     #print error info and line that threw the exception
	            continue 

	         # Wait for 2 seconds 
	        time.sleep(2)         

	         # Get page links 
	        soup = BeautifulSoup(page.text, "html.parser")
	        links = soup.find_all('li', attrs={'class': 'article'} )
	        print( "Page "+str(pageNo) +" : " + str(len(links)) + " articles")


	        for j in links: 
	            Term = term.capitalize()
	            Source = 'Times of India'
	            Statement = j.find("meta", attrs={'itemprop': 'name'})['content'].strip()
	            Link = j.find('meta', attrs={'itemprop': 'url'})['content'].strip()
	            Content = j.find('div', attrs={'class': 'content'}).find('a').find('p').text.strip()
	            Date = j.find('div', attrs={'class': 'content'}).find('a').find('span', attrs={'class' : 'meta'}).text.strip()
	            
	            f.write(Term + "," +Source + "," + Statement.replace(',', '|') + "," + Content.replace(',', '|') + "," + Date.replace(',', '|') + "," + Link + "\n")
	     


	    # # #######################
	    # # Hindustan Times
	    # # #######################
	    for pageNo in range(1,pagesToGet+1):
	        print('processing page :', pageNo)
	        url = 'https://www.hindustantimes.com/search?q='+ term #+ "&pageno=" +str(pageNo)
	        print(url)
	        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36', "Upgrade-Insecure-Requests": "1","DNT": "1","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate"}


	        try:
	            page=requests.get(url,headers=headers)                           
	        
	        except Exception as e:                                   # this describes what to do if an exception is thrown
	            error_type, error_obj, error_info = sys.exc_info()      # get the exception information
	            print ('ERROR FOR LINK:',url)                          #print the link that cause the problem
	            print (error_type, 'Line:', error_info.tb_lineno)     #print error info and line that threw the exception
	            continue 

	         # Wait for 2 seconds 
	        time.sleep(2)         
	        print(page)
	         # Get page links 
	        soup = BeautifulSoup(page.text, "html.parser")
	        links = soup.find_all('div', attrs={'class': 'media-body'} )

	        print( "Page "+str(pageNo) +" : " + str(len(links)) + " articles")


	        for j in links: 
	            Term = term.capitalize()
	            Source = 'Hindustan Times'
	            if(j.find('div', attrs={'class': 'media-heading'})):
	                Statement = j.find('div', attrs={'class': 'media-heading'}).find("a").text.strip()
	            else:
	                continue
	            if (j.find('div', attrs={'class': 'media-heading'})):
	                Link = j.find('div', attrs={'class': 'media-heading'}).find("a")['href'].strip()
	            else:
	                Link = " "
	            if(j.find('div', attrs={'class': 'para-txt'})):
	                Content = j.find('div', attrs={'class': 'para-txt'}).text.strip()
	            else:
	                Content= " "
	            if(j.find('span', attrs={'class': 'time-dt'})):
	                Date = j.find('span', attrs={'class': 'time-dt'}).text.strip()
	            else:
	                Date = " "
	            # print(Source, Statement, Link, Content, Date)
	            f.write(Term + "," + Source + "," +  Statement.replace(',', '|') + "," + Content.replace(',', '|') + "," + Date.replace(',', '|') + "," + Link + "\n")
	     

	    # #######################
	    # Aaj Tak HOINDIII
	    # #######################
	    pagesToGet = 2
	    for pageNo in range(1,pagesToGet+1):
	        print('processing page :', pageNo)
	        url = 'https://aajtak.intoday.in/topic/'+ term + "-page-"+ str(pageNo) + ".html"
	        print(url)
	        # headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36', "Upgrade-Insecure-Requests": "1","DNT": "1","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate"}


	        try:
	            page=requests.get(url)#,headers=headers)                           
	        
	        except Exception as e:                                   # this describes what to do if an exception is thrown
	            error_type, error_obj, error_info = sys.exc_info()      # get the exception information
	            print ('ERROR FOR LINK:',url)                          #print the link that cause the problem
	            print (error_type, 'Line:', error_info.tb_lineno)     #print error info and line that threw the exception
	            continue 

	         # Wait for 2 seconds 
	        time.sleep(2)         
	        # print(page.text)
	         # Get page links 
	        soup = BeautifulSoup(page.text, "html.parser")
	        links = soup.find_all('div', attrs={'class': 'scc_kv_st'} )

	        print( "Page "+str(pageNo) +" : " + str(len(links)) + " articles")


	        for j in links: 
	            Term = term.capitalize()
	            Source = 'AAJ TAK HINDI'
	            Statement = j.find('div', attrs={'class': 'scc_kv_all'}).find('h3').find("a").text
	            Link = j.find('div', attrs={'class': 'scc_kv_all'}).find('h3').find("a")['href'].strip()
	            Content = j.find('span', attrs={'class':'scc_st'}).text
	            Date = j.find('div', attrs={'class': 'scc_kv_all'}).find('cite').text
	            
	            # print(Source, Statement, Link, Content, Date)
	            f.write(Term + "," + Source + "," +  ' '.join(Statement.replace(',', ' ').split()) + "," + ' '.join(Content.replace(',', ' ').split()) + "," + Date.replace(',', ' ') + "," + Link + "\n")

	    # # #######################
	    # # INdian Express
	    # # #######################
	    pagesToGet = 2
	    for pageNo in range(1,pagesToGet+1):
	        print('processing page :', pageNo)
	        url = 'https://indianexpress.com/?s='+ term
	        print(url)
	        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36', "Upgrade-Insecure-Requests": "1","DNT": "1","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate"}


	        try:
	            page=requests.get(url,headers=headers)                           
	        
	        except Exception as e:                                   # this describes what to do if an exception is thrown
	            error_type, error_obj, error_info = sys.exc_info()      # get the exception information
	            print ('ERROR FOR LINK:',url)                          #print the link that cause the problem
	            print (error_type, 'Line:', error_info.tb_lineno)     #print error info and line that threw the exception
	            continue 

	         # Wait for 2 seconds 
	        time.sleep(2)         
	        print(page)
	         # Get page links 
	        soup = BeautifulSoup(page.text, "html.parser")
	        links = soup.find_all('div', attrs={'class': 'details'} )

	        print( "Page "+str(pageNo) +" : " + str(len(links)) + " articles")


	        for j in links: 
	            Term = term.capitalize()
	            Source = 'Indian Express'
	            Statement = j.find('h3').find('a').text.strip()
	            Link = j.find('h3').find("a")['href'].strip()
	            Content = j.find('p').text.strip()
	            Date = j.find('time').text.strip()
	            
	            # print(Source, Statement, Link, Content, Date)
	            f.write(Term + ',' + Source + "," +  " ".join(Statement.replace(',', '|').split()) + "," + " ".join(Content.replace(',', '|').split()) + "," + " ".join(Date.replace(',', '|').split()) + "," + " ".join(Link.split()) + "\n")

	    # # #######################
	    # # THE HINDU
	    # # #######################
	    pagesToGet = 2
	    for pageNo in range(1,pagesToGet+1):
	        print('processing page :', pageNo)
	        url = 'https://www.thehindu.com/search/?q=' + term + '&order=DESC&sort=publishdate'
	        print(url)
	        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36', "Upgrade-Insecure-Requests": "1","DNT": "1","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate"}


	        try:
	            page=requests.get(url,headers=headers)                           
	        
	        except Exception as e:                                   # this describes what to do if an exception is thrown
	            error_type, error_obj, error_info = sys.exc_info()      # get the exception information
	            print ('ERROR FOR LINK:',url)                          #print the link that cause the problem
	            print (error_type, 'Line:', error_info.tb_lineno)     #print error info and line that threw the exception
	            continue 

	         # Wait for 2 seconds 
	        time.sleep(2)         
	        print(page)
	         # Get page links 
	        soup = BeautifulSoup(page.text, "html.parser")
	        links = soup.find_all('div', attrs={'class': 'story-card-news'} )

	        print( "Page "+str(pageNo) +" : " + str(len(links)) + " articles")


	        for j in links:
	            Term = term.capitalize()
	            Source = 'The Hindu'
	            Statement = j.find("a", attrs={'class' : 'story-card75x1-text'}).text.strip()
	            Link = j.find("a", attrs={'class' : 'story-card75x1-text'})['href']
	            Content = j.find('span', attrs={'class': 'light-gray-color'}).text.strip()
	            Date = j.find('span', attrs={'class': ''}).find('span', attrs={'class' : 'dateline'}).text.strip()
	            
	            # print( Source, Statement, Link, Content, Date)
	            f.write(Term + ',' + Source + "," +  " ".join(Statement.replace(',', '|').split()) + "," + " ".join(Content.replace(',', '|').split()) + "," + " ".join(Date.replace(',', '|').split()) + "," + " ".join(Link.split()) + "\n")


	    # # #######################
	    # # NDTV NEWS
	    # # #######################
	    pagesToGet = 1
	    for pageNo in range(1,pagesToGet+1):
	        print('processing page :', pageNo)
	        url = 'https://www.ndtv.com/search?searchtext=' + term
	        print(url)
	        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36', "Upgrade-Insecure-Requests": "1","DNT": "1","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate"}


	        try:
	            page=requests.get(url,headers=headers)                           
	        
	        except Exception as e:                                   # this describes what to do if an exception is thrown
	            error_type, error_obj, error_info = sys.exc_info()      # get the exception information
	            print ('ERROR FOR LINK:',url)                          #print the link that cause the problem
	            print (error_type, 'Line:', error_info.tb_lineno)     #print error info and line that threw the exception
	            continue 

	         # Wait for 2 seconds 
	        time.sleep(2)         
	        print(page)
	         # Get page links 
	        soup = BeautifulSoup(page.text, "html.parser")
	        links = soup.find_all('li')

	        print( "Page "+str(pageNo) +" : " + str(len(links)) + " articles")


	        for j in links:
	            # print(j.get('style'))
	            # print(j)
	            if j.get('style') == "padding: 5px;":
		            Term = term.capitalize()
		            Source = 'NDTV NEWS'
		            Statement = j.find("p", attrs={'class' : 'header fbld'}).find('a')['title'].strip()
		            Link = j.find("p", attrs={'class' : 'header fbld'}).find('a')['href'].strip()
		            Content = j.find('p', attrs={'class': 'intro'}).text.strip()
		            Date = j.find('p', attrs={'class': 'list_dateline'}).text.split('|')[2]
		            
		            # print( Source, Statement, Link, Content, Date)
		            f.write(Term + ',' + Source + "," +  " ".join(Statement.replace(',', '|').split()) + "," + " ".join(Content.replace(',', '|').split()) + "," + " ".join(Date.replace(',', '|').split()) + "," + " ".join(Link.split()) + "\n")
	    f.close()
	else:
		#  THE END
		break
		f.close()

