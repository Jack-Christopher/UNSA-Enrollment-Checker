import winsound
from time import sleep
import urllib.request
from datetime import datetime
import re

def is_enabled(data):
    if "no habilitado" in data:
        return [False, "Not enabled school"]
    else:
        pattern = re.compile(r'<td>.+?</td>')
        match = pattern.findall(data)[0]
        temp = match.replace("<font color=red>", "").replace("</font>", "").replace("<td>", "").replace("</td>", "").replace(school, "").replace(" ", "").replace("<br>", "")
        if temp == "":
            return [True, "OK"]
        else:
            return [False, "There are some processes your school must do before you can enroll"]


school = input("Enter the exact name of your school: ").lower()
minutes = int(input("Enter the number of minutes between each query: "))
while True:
    TIME = minutes*60 if minutes >= 5 else 300
    with urllib.request.urlopen('http://extranet.unsa.edu.pe/sisacad/visualiza_fechas_b.php') as response:
        html = response.read().decode('utf-8').lower()
        # pattern = r"<td>.+?</td>"
        pattern = r"<tr>.+?</tr>"
        found = re.findall(pattern, str(html))
        answer = [False, "School not found"]
        for i in range(1, len(found)):
            # print(found[i])
            if school in found[i]:
                answer = is_enabled(found[i])
                break
        # print(html)

        now = datetime.now().strftime("%H:%M:%S")
        print( '(' + now + ')' + ' ' + answer[1])

        if answer[0]:
            TIME = 10
            winsound.Beep(440, 2000)
        else: 
            winsound.Beep(440, 100)
    sleep(TIME)