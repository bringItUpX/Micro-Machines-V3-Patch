#!/usr/bin/env python3
import os

begin = 0     # 0 sets the reference point at the beginning of the file
current = 1   # 1 sets the reference point at the current file position
end = 2       # 2 sets the reference point at the end of the file 

# Syntax: filemicro.seek(offset, from_what), where filemicro is file pointer

patchnum=bytes(b"\x68")
orig=bytes(b"\x28")


print("This Python-Script alter the game Micro Machines V3 to run at speed of an 120MHz Pentium I -")
print("but on a modern PC in the Year 2020. But in the game you have to additionally slow down")
print("the speed by pressing the Key 'F7' - also for a higher resolution of the game.")
print("For this script, the version of the game has to be from the date 12. May 1998.")
print("This script is made for the german version of the game executable.")
print("Perhaps it patches also the other languages of the game executable.")
print("------Hack:------")
print("The game has three occurrences of an assembler 'CMP 0x28, eax' command.")
print("This CMP command can handle numbers approximately till 0x7F")
print("This script alter the 0x28 to 0x68, to reduce the speed of the game")
print("------Hints:-----")
print("At the beginning of the calculation of the next frame during playing, the game MMV3")
print("calls the Win32 API function 'GetTickCount'. The return value of this function is stored,")
print("and compared with an earlier value of the function.")
print("'eax' = 'current_time' - 'last_time'")
print("after the above calculation the CMP command above is executed.")
print("If the difference of the two time values is lower than 0x28 the game does not calculate")
print("a new frame und returns to Windows.")
print("If the difference is greater than 0x28 the next frame will be calculated")
print("------Usage:-----")
print("To work with this script you have to place the german file micro.exe of the game")
print("in the same directory like this python script.")
print("")
print("------now it runs the script:---------")
if os.path.exists("micro.exe"):
    print("a file micro.exe is there -> right")
    file_length_in_bytes = os.path.getsize("micro.exe")
    print("File has this amount of bytes:")
    print(file_length_in_bytes)
    print("File should have 558080 bytes for the german micro.exe executable")
    if (file_length_in_bytes == 558080):
        rightcontent = True
        with open("micro.exe", "r+b") as filemicro:
            filemicro.seek(253190, begin)
            if (filemicro.read(1) == orig):
                print("1. occurrence in the file has 0x28 -> right")
            else:
                rightcontent = False
            filemicro.seek(253224, begin)
            if (filemicro.read(1) == orig):
                print("2. occurrence in the file has 0x28 -> right")
            else:
                rightcontent = False
            filemicro.seek(253272, begin)
            if (filemicro.read(1) == orig):
                print("3. occurrence in the file has 0x28 -> right")
            else:
                rightcontent = False
            writepatch = True
            if (rightcontent == True):
                print("it is the right micro.exe -> now patching the file.")
                filemicro.seek(253190, begin)
                if filemicro.write(patchnum) == 1:
                    print("has changed the 1. occurrence")
                else:
                    writepatch = False
                filemicro.seek(253224, begin)
                if filemicro.write(patchnum) == 1:
                    print("has changed the 2. occurrence")
                else:
                    writepatch = False
                filemicro.seek(253272, begin)
                if filemicro.write(patchnum) == 1:
                    print("has changed the 3. occurrence")
                else:
                    writepatch = False
                if writepatch == True:
                    print("-----micro.exe successfully patched----------")
            else:
                print("I do not patch. This is not the right micro.exe executable")

    else:
	    print("I do not patch, wrong file size!")
else:
    print("I do not patch, file is not there!")
