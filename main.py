import winsound
from time import sleep
import urllib.request
from datetime import datetime

school = input("Enter the exact name of your school: ").lower()
while True:
    TIME = 0
    with urllib.request.urlopen('http://extranet.unsa.edu.pe/sisacad/matint22a1/acad_login.php') as response:
        html = response.read().decode('utf-8').lower()
        # print(html)
        now = datetime.now().strftime("%H:%M:%S")
        if school in str(html):
            TIME = 15
            print( '(' + now + ')' +" Found it!")
            winsound.Beep(440, 2000)
        else:
            TIME = 60
            print( '(' + now + ')' +" Nothing yet")
            winsound.Beep(440, 100)
    sleep(TIME)