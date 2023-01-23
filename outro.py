#Code From Arty06
#Github --> github.com/ArtyETH06
#©Arty06

#Import
import os
import time
from colorama import init, Fore, Style
import pyfiglet
#For audio
import winsound
import sounddevice as sd
import soundfile as sf

#Initialisation
init()

#Clear auto du terminal (trop usefull)
os.system('cls||clear')

message = pyfiglet.figlet_format("PC Outro", font = "big")

print(Fore.CYAN + Style.BRIGHT+ "============================================================================================================================================================================================================================================\n\n\n")
print(message,"\n\nCoded By Arty06, open source code\n Github --> github.com/ArtyETH06")
print(Fore.CYAN + Style.BRIGHT +  "============================================================================================================================================================================================================================================\n\n")
a = 10

#Start the AUDIO
array, smp_rt = sf.read("outro.mp3", dtype = 'float32') 
# start the audio
sd.play(array, smp_rt)

#Shutdown the PC
os.system('shutdown -s -t 11') 




for i in range(1,11):
    print(Fore.GREEN + Style.BRIGHT + "Shutting down pc in ", a , "seconds...")
    a = a - 1
    time.sleep(1)

message2 =  pyfiglet.figlet_format("GoodBye ;)", font = "big")
print(Fore.RED + Style.BRIGHT + message2)


# Wait until file is done playing
status = sd.wait() 




