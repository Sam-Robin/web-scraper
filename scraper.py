# Python 3 Web Scraper
#
# Author: Sam Robinson
# Last Update: 28/04/2020

import urllib.request

while True:

    # Ask for a URL
    url = input("URL: ")
    print("URL is " + url)
    request = None

    try:
        # Send a GET request using that URL
        request = urllib.request.urlopen(url, data=None, cafile=None,
                                         capath=None, cadefault=False,
                                         context=None)
        # Output the data from the GET request
        print(request.read())

        # Create a new file
        file = open("webpage.html", "w")

        # Iterate through the response data
        for c in request.read():
            file.write(c)
            
        file.write("cock")
        
        file.close()
    except Exception as e:
        print(str(e))

