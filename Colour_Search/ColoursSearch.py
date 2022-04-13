import json
from colorama import Fore, Back, Style

#open the JSON
def getResponse(file):
    with open(file) as json_file:
        jsonData = json.load(json_file)
    return jsonData

def main():

    fileData = "Colour_Data"
    missingKey = "type"
    jsonData = getResponse(fileData)
    pres = 0;

    print("================================================")
    print ("         Colour RGBA Code Searcher")
    print("================================================")
    val = input("Enter your colour: ")
    #convert for ease of use
    val = val.lower()
    print("================================================")

    #check against other colours
    for i in jsonData['colors']:

        if val in i["color"]:
            #status variable for if the colour was found
            pres = 1
            print(Fore.GREEN + "Name: ", i["color"])
            if missingKey in i:
                print("Type: ", i["type"])
            else:
                print("Type: ", "N/A")

            print("Code: ", i["code"]["rgba"])

    if (pres == 0):
        print(Fore.RED + "================================================")
        print("  The Colour You Are Searching For Is Missing")
        print("================================================")
        print(Style.RESET_ALL)
    else:
        print(Fore.RESET + "================================================")

if __name__ == '__main__':
    main()
