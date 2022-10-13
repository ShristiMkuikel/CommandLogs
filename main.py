import json
import math

# get input json file location from user
filelocation=input("Please enter input.json file location:")
file = open(filelocation, 'r')
inputJson = json.load(file)
lengthOfData = len(inputJson)
dataset = []
UserList = []
times = []
load_data = []
endLIST = []

# getting userlist
for row in inputJson:
    for key, value in row.items():
        if key == "user":
            user_value = value
    dataset.append(user_value)
    UserList = [*set(dataset)]  # remove duplicate users
    UserList.sort()  # sort in ascending order
# print(UserList)

# program to loop through the objects in input.json and store timestamp data for respective users

with open("output.json", 'w') as outputfile:  # creating output.json file to dump the final data
    for k in range(len(UserList)):
        times = {"red": '', "Blue": '', "Green": '', "Yellow": ''}
        YELLOWtimeset = []
        REDtimeset = []
        GREENtimeset = []
        BLUEtimeset = []

        for r in inputJson:
            for key, value in r.items():
                # looping through the input data to collect command-timestamp info for each user
                if value == UserList[k]:
                    command = r['command']
                    timestamp = r['timestamp']

                    if command == "yellow":
                        YELLOWtimeset.append(timestamp)
                    if command == "red":
                        REDtimeset.append(timestamp)
                    if command == "green":
                        GREENtimeset.append(timestamp)
                    if command == "blue":
                        BLUEtimeset.append(timestamp)

                times = {"red": REDtimeset, "Blue": BLUEtimeset, "Green": GREENtimeset, "Yellow": YELLOWtimeset}

        load_data = {UserList[k]: times}
        copy = load_data.copy()
        endLIST.append(copy)

    json.dump(endLIST, outputfile, indent=4)  # dump to output.json file


# Looking up a command log for a particular user
# prints all the red, yellow, blue, green commands for the particular user
# Prints the total number of red, yellow, blue, green commands sent by the user
def UserLookup(outputfile, username):

    print(lengthOfData)
    for n in outputfile:
        for key, value in n.items():
            if key == username:
                print("Log info for: ", key)
                print(value)  # prints the whole log
                valueitems = value
                for key, value in valueitems.items():
                    print(key, ": ", len(value))  # prints total commands
                    percentage=(((len(value))/lengthOfData)*100)
                    f=round(percentage,2)
                    print(" Total Percent",key," logs created: ",f,"%")


# Create individual user logs
def CreateUserlogs(outputfile, username):
    loadval = []
    for n in outputfile:
        for key, value in n.items():
            if key == username:
                loadval = {key: value}
                print("Log file created for: ", key)
                with open("userlog.json", 'w') as f:  # creating output.json file to dump the final data
                    json.dump(loadval, f, indent=4)  # dump to output.json file
                    print("******************JSON file created******************")
                    input4 = input("Would you like to continue?(Y/N)")
                    if input4 == "Y" or input4 == "y":
                        getUserInput()
                    else:
                        print("----------End of Program----------")


# get input from the user
def getUserInput():
    print("***************Userlist****************************")
    print(UserList)
    print(" ")
    userinput = input("please enter the user you would like to look up from the Userlist above:")
    if userinput in UserList:
        UserLookup(endLIST, userinput)  # looking up user_5's command-timestamp log
        userinput2 = input("Would you like to create user file for this user?(Y/N)")
        if userinput2 == "Y" or userinput2 == "y":
            CreateUserlogs(endLIST, userinput)
        else:
            userinput3 = input("Would you like to look up another user?(Y/N)")
            if userinput3 == "Y" or userinput3 == "y":
                getUserInput()
            else:
                print("----------End of Program----------")

    else:
        print("incorrect user info")
        getUserInput()


getUserInput()
