import os 
import msvcrt as m

def wait():
    print("Press any key to continue...") 
    m.getch()

os.system("pip install pyinstaller")

location_2 = os.path.dirname(__file__)

name = input("name of the python file:")
os.system("cd "+location_2 )
os.system("pyinstaller --onefile "+name)

wait()

