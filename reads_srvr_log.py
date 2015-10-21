# Queries the logs to find the average draw time for a given map service

# For Http calls
import httplib, urllib, json

# For system tools
import sys

# For reading passwords without echoing
import getpass

#Defines the entry point into the script
def main(argv=None):
    # Print some info
    print
    print "This tool is a sample script that queries the ArcGIS Server logs."
    print
    
    # Ask for admin/publisher user name and password
    username = raw_input("Enter user name: ")
    password = getpass.getpass("Enter password: ")
    
    # Ask for server name
    serverName = raw_input("Enter Server name: ")
    serverPort = 6080

    # Ask for map service name
    mapService = raw_input("Enter map service name, using a forward slash / to denote a folder: ")
    if mapService.endswith(".MapServer"):
        pass
    else:
        mapService += ".MapServer"
    
    # Get a token
    token = getToken(username, password, serverName, serverPort)
    if token == "":
        print "Could not generate a token with the username and password provided."
        return
    
    # Construct URL to query the logs
    logQueryURL = "/arcgis/admin/logs/query"
    logFilter = "{'services': ['" + mapService + "']}"
    
    # Supply the log level, filter, token, and return format
    params = urllib.urlencode({'level': 'FINE', 'filter': logFilter, 'token': token, 'f': 'json'})
    
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    
    # Connect to URL and post parameters    
    httpConn = httplib.HTTPConnection(serverName, serverPort)
    httpConn.request("POST", logQueryURL, params, headers)
    
    # Read response
    response = httpConn.getresponse()
    if (response.status != 200):
        httpConn.close()
        print "Error while querying logs."
        return
    else:
        data = response.read()

        # Check that data returned is not an error object
        if not assertJsonSuccess(data):          
            print "Error returned by operation. " + data
        else:
            print "Operation completed successfully!"

        # Deserialize response into Python object
        dataObj = json.loads(data)
        httpConn.close()

        # Need these variables to calculate average draw time for an ExportMapImage call
        mapDraws = 0
        totalDrawTime = 0 
        
        # Iterate over messages        
        for item in dataObj["logMessages"]:
                       
            if item["message"] == "End ExportMapImage":
                print "Server drew map in " + item["elapsed"] + " seconds."
                mapDraws +=1
                totalDrawTime += float(item["elapsed"])

        print "Total number of draws found in logs: " + str(mapDraws)

        if mapDraws == 0:
            return
        
        print "Average draw time: " + str(1.0*(totalDrawTime / mapDraws)) + " seconds."      
            
        return

#A function to generate a token given username, password and the adminURL.
def getToken(username, password, serverName, serverPort):
    # Token URL is typically http://server[:port]/arcgis/admin/generateToken
    tokenURL = "/arcgis/admin/generateToken"
    
    # URL-encode the token parameters
    params = urllib.urlencode({'username': username, 'password': password, 'client': 'requestip', 'f': 'json'})
    
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    
    # Connect to URL and post parameters
    httpConn = httplib.HTTPConnection(serverName, serverPort)
    httpConn.request("POST", tokenURL, params, headers)
    
    # Read response
    response = httpConn.getresponse()
    if (response.status != 200):
        httpConn.close()
        print "Error while fetching tokens from admin URL. Please check the URL and try again."
        return
    else:
        data = response.read()
        httpConn.close()
        
        # Check that data returned is not an error object
        if not assertJsonSuccess(data):            
            return
        
        # Extract the toke from it
        token = json.loads(data)       
        return token['token']            
        

#A function that checks that the input JSON object
#  is not an error object.    
def assertJsonSuccess(data):
    obj = json.loads(data)
    if 'status' in obj and obj['status'] == "error":
        print "Error: JSON object returns an error. " + str(obj)
        return False
    else:
        return True
    
        
# Script start
if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))