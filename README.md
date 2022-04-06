# UNSA Enrollment Checker

**Description**:  
This is a simple program that checks if a school is ready to enroll in the UNSA.
It's really tedious to check if a school is ready to enroll every few minutes and have to wait until it's ready, so this program is designed to help you check if a school is ready to enroll in the UNSA automatically every minute.


## Dependencies

- urllib3: It is used to make the requests to webpages.

## Installation

You should have installed Python 3 and the dependencies before using this software.
For that you should run the following command in the terminal:

```
pip install -r requirements.txt
```

## Usage

- The program will ask you for the school's name (you should be careful to write it correctly) 
- Every minute:
    - A little beep will sound to notify you that the program is running.
    - The program will check if the school is ready to enroll.
    - If the school is ready to enroll, the program will beep again for a longer time.
- This program will beep until you stop it.

----

## License
This project is licensed under the MIT license.