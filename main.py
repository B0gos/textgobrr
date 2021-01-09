import importlib
import os


print("loading user data...")
if(os.path.exists('settings.py') == True):
    import settings
    setting = settings.settings

else:
    print("ERROR: user settings file is missing!")
    print("would you like me to generate one?")
    input = input("[y/N]: ")
    if(input == "y"):
        print("Generating config...")
        with open("settings.py", "w") as file:
            file.write('# textgobrr Settings File:\nsettings = {\n    "user": "user",\n    "level": 0\n}\n')
        if(os.path.exists('settings.py') == True):
            import settings
            setting = settings.settings
            print("Success!")
        else:
            print("error: could not generate config file ):")
            print('no progress will be saved')
            setting = {
                "user": "default",
                "level": 0
            }

    else:
        setting = {
            "user": "default",
            "level": 0
        }
        print("proceding without settings file...")
        print('no progress will be saved')

def main():
    print("Hello {}, welcome to".format(setting['user']))
    
    print("  _______ ________   _________ _____  ____  ____  _____  _____   ")
    print(" |__   __|  ____\ \ / /__   __/ ____|/ __ \|  _ \|  __ \|  __ \  ")
    print("    | |  | |__   \ V /   | | | |  __| |  | | |_) | |__) | |__) | ")
    print("    | |  |  __|   > <    | | | | |_ | |  | |  _ <|  _  /|  _  /  ")
    print("    | |  | |____ / . \   | | | |__| | |__| | |_) | | \ \| | \ \  ")
    print("    |_|  |______/_/ \_\  |_|  \_____|\____/|____/|_|  \_\_|  \_\ ")
                                                    
                                                                                                                                                                             
    print("\n")
    print("Please choose one of the following:")
    print("1. Start Game")
    print("2. Settings")
    print("3. Exit")
    choice = input('Choice [1/2/3]:')
    if(choice == "1"):
        print("hello, {}".format(setting['user']))
        start()
    elif(choice == "2"):
        print("menu")
        setup()
    elif(choice == "3"):
        print("Goodbye!")
        exit(0)
    else:
        print("invalid choice")
        main()

    
def start():
    print("sorry {}, im not done yet on this part yet".format(setting['user']))
    choice = input("would you like to go to the main menu [Y/n]:")
    if(choice == "n"):
        print("okay?")
        print("are you sure you want to play this game?")
        answer = input("[y/N]: ")
        if(answer == "y"):
            really = "really"
            while(answer != "n"):
                really = really + " really"
                print("are you {} sure you want to play this game?".format(really))
                answer = input("[Y/n]: ")
        else:
            main()
    else:
        main()
        
        
def setup():
    os.system("nano settings.py")
    print("loading new config...")
    global setting
    importlib.reload(settings)
    setting = settings.settings


print("loading complete!")


while True:
    main()