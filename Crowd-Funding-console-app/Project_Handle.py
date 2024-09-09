from Modes_handler import Read_Valid_Str,Read_Valid_int,SearchInfile

from colorama import Fore, Style

count=1
def create_id():
    global count
    id = count
    count +=1
    return id

def ReadDate(messege):
    print(messege)

    Day = Read_Valid_int("Day: ")
    while Day >31 or Day<1:
        print(Fore.RED+ "== Please Entar a Valid Day (1-31) ==" + Style.RESET_ALL)
        Day=Read_Valid_int("Day: ")

    Month = Read_Valid_int("Month: ")
    while Month > 12 or Month < 1:
        print(Fore.RED+ "== Please Entar Valid Month (1-12)==" + Style.RESET_ALL)
        Month = Read_Valid_int("Month: ")

    Year=Read_Valid_int("Year: ")
    while Year <2024:
        print(Fore.RED+ "== Please Entar Valid Year ==" + Style.RESET_ALL)
        Year=Read_Valid_int("Year: ")

    return Day, Month, Year

def Project_data():
    ProjTitle=Read_Valid_Str("Please Enter The Project Title: ")
    Details=Read_Valid_Str("Please Enter The Project Details: ")
    Target=Read_Valid_int("Please Enter The Project Target: ")
    StartTime=ReadDate("Please Enter The Start Time: ")
    EndTime=ReadDate("Please Enter The Expected End Time: ")

    while EndTime[2] < StartTime[2] or (EndTime[2] == StartTime[2] and  EndTime[1] < StartTime[1]) or (EndTime[2] == StartTime[2] and EndTime[1] == StartTime[1] and EndTime[0] < StartTime[0]) :
        print("Fore.RED + Invaild dates" + Style.RESET_ALL)
        StartTime = ReadDate("Please Enter The Start Time: ")
        EndTime = ReadDate("Please Enter The Expected End Time: ")

    User_id=Read_Valid_int("Your ID: ")
    Project_Pass=Read_Valid_Str("Create A Project Password: ")
    validate_Pass=Read_Valid_Str("Validate Password: ")
    if Project_Pass == validate_Pass:
        print(Fore.GREEN + "Validated Successfully" + Style.RESET_ALL )
    else:
       while True:
            print(Fore.RED +"validation Failed " + Style.RESET_ALL)
            validate_Pass=Read_Valid_Str(f"{"Validate Password: "}: ")
            if Project_Pass == validate_Pass:
                print(Fore.GREEN + "Validated Successfully" + Style.RESET_ALL)
                break
    Group_id=create_id()

    return  Project_Pass,User_id,Group_id,ProjTitle,Details,Target,StartTime,EndTime

def InsertProjectIntoFile(project):
    try:
        fileobject=open("Projects.txt","a")
    except Exception as e:
        print(Fore.RED + e + Style.RESET_ALL)
        return False
    else:
        fileobject.writelines(project)
        fileobject.close()
        return True

def WriteAllProjectsIntoFile(project):
    try:
        fileobject=open("Projects.txt","w")
    except Exception as e:
        print(e)
        return False
    else:
        fileobject.writelines(project)
        fileobject.close()
        return True

def CreateProject():
    Project_info=Project_data()
    Project_format_info=f"{Project_info[0]}:{Project_info[1]}:{Project_info[2]}:{Project_info[3]}:{Project_info[4]}:{Project_info[5]}:{Project_info[6]}:{Project_info[7]}\n"
    if InsertProjectIntoFile(Project_format_info):
        print(Fore.GREEN + "Project Created Successfully" + Style.RESET_ALL)

def get_all_projects():
    try:
        fileobject=open("Projects.txt","r")
    except Exception as e:
        print(e)
        return False
    else:
        projects=fileobject.readlines()
        return projects


def ViewProjects():
    print("\t\tUser Id\tGroup Id	     Project Title  	\tDetails\t\tTarget	\tStart Date\t    End Date")
    print(Fore.BLUE+ "=======================================================================================================================================" +Style.RESET_ALL)
    # for element in get_all_projects():
    #     for val in element.split(":")[1:]:
    #         print(f"\t{val}\t\t", end="")
    # Assuming each project info has 8 fields separated by colons.
    for element in get_all_projects():
        # Split the element into a list of values
        values = element.strip().split(":")

        # Print the values in properly formatted columns
        # Adjust column widths based on expected data length
        print(
            f"\t\t{values[1]:<10} {values[2]:<15} {values[3]:<20} {values[4]:<12} {values[5]:<10} {values[6]:<15} {values[7]:<15}")

    print()


def delete_my_project():
    project_id= Read_Valid_int("Project ID: ")
    project_id=str(project_id) #project_id Covcerted to string because my SearchInfile function take strings
    project_index= SearchInfile("Projects",project_id,2)
    if project_index != None: #Ensure SearchInfile function returned value not None
        project_index -= 1         # reduce 1 in increased in SearchInfile
    else:
        print(Fore.RED+ "Project Not Found" +Style.RESET_ALL)
        return
    project_pass = Read_Valid_Str("Project Password: ")
    project_pass = str(project_pass)
    for tries in range(3):  #check project password with 3 tries
        if SearchInfile("Projects",project_pass,0):
            break
        else:
            print(Fore.RED + "Incorrect Project Password"+Style.RESET_ALL)
            project_pass = Read_Valid_Str("Project Password: ")
            project_pass = str(project_pass)

    else:
        print(Fore.RED + "Incorrect Project Password, PLease Try Later"+Style.RESET_ALL)
        return
    allprojrcts=get_all_projects()
    del allprojrcts[project_index]
    WriteAllProjectsIntoFile(allprojrcts)
    print(Fore.GREEN + "Project Deleted Successfully"+Style.RESET_ALL)

def edit_in_my_project():
    project_id= Read_Valid_int("Project ID: ")
    project_id=str(project_id) #project_id Converted to string because my SearchInfile function take strings
    project_index= SearchInfile("Projects",project_id,2)
    if project_index != None: #Ensure SearchInfile function returned value not None
        project_index -= 1         # reduce 1 in increased in SearchInfile
    else:
        print(Fore.RED+ "Project Not Found" +Style.RESET_ALL)
        return

    # check project password with 3 tries
    project_pass = Read_Valid_Str("Project Password: ")
    project_pass = str(project_pass)
    for tries in range(3):  #check project password with 3 tries
        if SearchInfile("Projects",project_pass,0):
            break
        else:
            print(Fore.RED + "Incorrect Project Password"+Style.RESET_ALL)
            project_pass = Read_Valid_Str("Project Password: ")
            project_pass = str(project_pass)

    else:
        print(Fore.RED + "Incorrect Project Password, PLease Try Later"+Style.RESET_ALL)
        return



    allprojects=get_all_projects()
    print(allprojects[project_index])
    newData=Project_data()
    print(newData[1:])
    newData2=f"{newData[0]}:{newData[1]}:{newData[2]}:{newData[3]}:{newData[4]}:{newData[5]}:{newData[6]}:{newData[7]}:\n"
    allprojects[project_index]=newData2
    WriteAllProjectsIntoFile(allprojects)
    return True

