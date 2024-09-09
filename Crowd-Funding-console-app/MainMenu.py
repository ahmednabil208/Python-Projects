
from Modes_handler import Registration,login_mode
from Project_Handle import CreateProject,ViewProjects,edit_in_my_project,delete_my_project
from colorama import Fore, Style

#print(Fore.RED + "This is a red message!" + Style.RESET_ALL)

def MainMenu_fun():
    print(Fore.BLUE + "\t\t\t\t=========== Welcome To The Crowd-Funding Console App ===========\n" + Style.RESET_ALL)
    mode= input("""Please Select an option:
    R --> Registration
    L --> Login
    E --> Exit
    Enter Your Choice: """)

    if mode in ["R","r","L","l","E","e"]:
        if mode == "R" or mode == "r":    #Registration Mode
            print(Fore.GREEN +"=========== Welcome To Registration Page ===========" + Style.RESET_ALL)
            Registration()
        elif mode == "L" or mode == "l": #Login Mode
            print(Fore.GREEN + "=========== Welcome To Login Page ===========" + Style.RESET_ALL)
            login_mode()

            ch=input("""Choose Option
            C --> Create A Project
            V --> View All Projectsl
            E --> Edit Project
            D --> Delete Project
            L --> Logout
            Your Choise: """)
            while ch in ["c","C","v","V","e","E","D","d","L","l"]:
                if ch == "c" or ch == "C":
                    print(Fore.GREEN + "=========== Welcome To Create A Project Page ===========" + Style.RESET_ALL)
                    CreateProject()
                elif ch == "v" or ch == "V":
                    print(Fore.GREEN + "=========== All Projects Available  ===========" + Style.RESET_ALL)
                    ViewProjects()
                elif ch == "E" or ch == "e":
                    edit_in_my_project()
                elif ch == "D" or ch == "d":
                    delete_my_project()

                elif ch == "L" or ch == "l":
                    break
                ch = input("""Choose Option
                C --> Create A Project
                V --> View All Projects
                E --> Edit Project
                D --> Delete Project
                L --> Logout
                Your Choise: """)
            else:
                print("====== Invalid Option ========")

        elif mode == "E" or mode == "e":
            print(Fore.RED + "Exitting..." + Style.RESET_ALL)
            exit(1)

    else:
        print("Enter a valid option")
        return MainMenu_fun()



while True:
    MainMenu_fun()