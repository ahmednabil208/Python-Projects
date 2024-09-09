
" For color printed messages "
from colorama import Fore, Style
#print(Fore.RED + "This is a red message!" + Style.RESET_ALL)

count=1
def create_id():
    global count
    id = count
    count +=1
    return id

import re
def gmail_is_valid(gmail):
    gmail_pattern = r'^[a-zA-Z0-9._%+-]+@gmail\.com$'
    if re.match(gmail_pattern,gmail):
        return True
    else:
        return False

def Read_Valid_Str(massege):
    value=input(massege)

    if value.isdigit() or value.isspace() or not value:
        print(Fore.RED + "Please Enter Correct value for string" + Style.RESET_ALL)
        return Read_Valid_Str(massege)

    return value


def Read_Valid_int(massege):
    value = input(massege)

    if value.isdigit() :
        return int(value)

    print(Fore.RED + "Please Enter Correct value for int" + Style.RESET_ALL)
    return Read_Valid_int(massege)


def UserData():
    my_dic={
        "FirstName":"",
        "LastName":"",
        "email":"",
        "MobileNumber": "",
        "Password":"",
        "validatePass":""
    }

    for key in my_dic.keys():
        if key == "MobileNumber":
            my_dic[key]=input(f"{key}: ")
            while not (my_dic["MobileNumber"].startswith("011") or my_dic["MobileNumber"].startswith("010") or my_dic["MobileNumber"].startswith("012") or my_dic["MobileNumber"].startswith("015")) or len(my_dic["MobileNumber"]) != 11:
                print(Fore.RED + "Mobile Number Must be 11 digits and Starts with (010), (011), (012) or (015)" + Style.RESET_ALL)
                my_dic[key] = input(f"{key}: ")

            #my_dic[key]=int(my_dic[key])   #convert number into int but remove 0 in the left

        elif key == "email":
            my_dic[key] = Read_Valid_Str(f"{key}: ")
            while not gmail_is_valid(my_dic[key]):
                print(Fore.RED + "Invalid Gmail Format. Please enter a valid Gmail address. ex: abc@gmail.com" + Style.RESET_ALL)
                my_dic[key] = Read_Valid_Str(f"{key}: ")
        else:
            my_dic[key]=Read_Valid_Str(f"{key}: ")

    if my_dic["Password"] == my_dic["validatePass"]:
        print(Fore.GREEN + "Registration Successfully" + Style.RESET_ALL )
    else:
       while True:
            print(Fore.RED +"validatePass is not identical " + Style.RESET_ALL)
            my_dic["validatePass"]=Read_Valid_Str(f"{"validatePass"}: ")
            if my_dic["Password"] == my_dic["validatePass"]:
                print(Fore.GREEN + "Registration Successfully" + Style.RESET_ALL)
                break

    owner_pass=my_dic["Password"]
    del my_dic["validatePass"]
    user_id=create_id()
    my_dic["User_ID"]=user_id
    my_dic=f"{my_dic["User_ID"]}:{my_dic["FirstName"]}:{my_dic["LastName"]}:{my_dic["email"]}:{my_dic["MobileNumber"]}:{my_dic["Password"]}:\n"
    return my_dic


def Registration():
    user_data=UserData()
    try:
        fileobject=open("Users.txt","a")
    except Exception as e:
        print(e)
        return False
    else:
        fileobject.writelines(user_data)

        fileobject.close()

def getAllUsers(place):
    try:
        fileobject=open(f"{place}.txt","r")
    except Exception as e:
        print(e)
        return False
    else:
        users=fileobject.readlines()
        return users

def SearchInfile(place,value,index):
    all_data=getAllUsers(place)
    for user in all_data:
        user_info=user.split(":")
        if str(value) == user_info[index]:
            user_index=all_data.index(user)
            return (user_index+1)  # +1 --> when return index 0 --> False



def login_mode():
    Email=Read_Valid_Str("Enter Your Email: ")
    if SearchInfile("Users",Email,3):
        password=Read_Valid_Str("Enter Your Password: ")
        if SearchInfile("Users",password,5):
            owner_pass=password
            print(Fore.GREEN + f"Welcome "+ Style.RESET_ALL)
        else:
            while True:
                print(Fore.RED +"Incorrect Password " + Style.RESET_ALL)
                password = Read_Valid_Str("Enter Your password: ")
                if SearchInfile("Users",password,5):
                    print(Fore.GREEN + "Welcome" + Style.RESET_ALL)
                    break

    else:
        print(Fore.RED +"Your Email Not Found ..." + Style.RESET_ALL)
        return login_mode()

