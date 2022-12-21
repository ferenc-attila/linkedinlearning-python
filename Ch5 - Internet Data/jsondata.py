# 
# Example file for parsing and processing JSON
# LinkedIn Learning Python course by Joe Marini
#

import urllib.request 
import json

separator = "----------------\n"


def print_results(data):
    # Use the json module to load the string data into a dictionary
    the_json = json.loads(data)
    
    # now we can access the contents of the JSON like any other Python object
    if "title" in the_json["metadata"]:
        print(the_json["metadata"]["title"])
    
    # output the number of events, plus the magnitude and each event name  
    count = the_json["metadata"]["count"]
    print(count, "events recorded")
    
    # for each event, print the place where it occurred
    for feature in the_json["features"]:
        print(feature["properties"]["place"])
    print(separator)
    # print the events that only have a magnitude greater than 4
    for feature in the_json["features"]:
        try:
            magnitude = float(feature["properties"]["mag"])
        except ValueError as ve:
            print(ve)
            print("Invalid magnitude value:", feature["properties"]["mag"])
            magnitude = 0.0
        if magnitude >= 4.0:
            print(feature["properties"]["place"])
    print(separator)

    # print only the events where at least 1 person reported feeling something
    print("\nEvents that were felt:\n")
    for feature in the_json["features"]:
        felt_reports = feature["properties"]["felt"]
        if felt_reports is not None:
            print(feature["properties"]["place"], felt_reports, "times")
    print(separator)

  
def main():
    # define a variable to hold the source URL
    # In this case we'll use the free data feed from the USGS
    # This feed lists all earthquakes for the last day larger than Mag 2.5
    url_data = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"

    # Open the URL and read the data
    web_url = urllib.request.urlopen(url_data)
    print ("result code: " + str(web_url.getcode()))
    if web_url.getcode() == 200:
        data = web_url.read()
        print_results(data)
    else:
        print("Received an error from the server, cannot print results", web_url.getcode())


if __name__ == "__main__":
    main()
