# Local messenger
## This messenger for local secure send message between two users

## To get started
### 1.  For one computer
Enter the IP address of the local network in the 'settings.ini' file, first run the file 'main_server.py', then 'main_client.py' 
### 2.  For two users
Enter the server IP address of the local network in the 'settings.ini' file, first user run the file 'main_server.py', which have a server computer. 
Сan run 'main.py', in terminal you must write Server (first user) or Client (second user)
 


## To exe file
### To convert the program to an exe file, follow these steps:
1. pip install auto-py-to-exe
2. In terminal 'auto-py-to-exe'
3. Choice .py file:
   1. if you choose 'main.py' to convert, in "Console Windows" choice "Console Based"
   2. if you choose 'main_server.py' and 'main_client.py' to convert, you can choose "Window Based" in "Console Windows"
4. In "Additional Files" add 'settings.ini' file
After convert, if chosen "One File" in "Onefile", in output directory add 'settings.ini' file and enter the IP address of the local network in this file

### After that you can send message in the local network

## Application
This project was created in mvc where are used:
1. Window with PyQt6
2. Threads from QThread
3. pyqtSignal and pyqtSlot from QtCore
4. Creating a server and client from socket
5. Using symmetric encryption with Fernet from cryptography
6. Reading ini file with configparser

