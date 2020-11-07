# Micro-Machines-V3-Patch
Patch for slowing down the speed of the game Micro Machines V3 on modern Windows / Linux(wine) computers.

Run this script with "python3 patch_micro_exe_german.py".

The executable of the game has to be in the same directory. Please make a backup before. The executable of the MMV3 game which is patched is micro.exe (choose german during the installation of the game, because this script is written with that version in mind.) The executable should from the date 12. May 1998. A verifying is running in the python script before running the patch, but there is no backup made.

If the patch script runs successfully, copy the file micro.exe back to your game directory (don't overwrite your backup of the orginal file), and start the game normally (you should choose Software Rendered).

In the game then all players are on the road and the light is green (all players can move theire cars) then press the key F7 to more slow down the game and to increase the screen resolution.

Through the patch you can play the game like in the old times with an Pentium I at 120MHz Clock. I think a better used screen (really full screen) is made only when you run this game on Linux with Wine. But it's not easy to configure, because you have to enable Win32 mode before you create the .wine directory (in the user folder), and you have to set full screen. I used this with Wine 4.0.2 on Linux Mint 19. But also other versions should work. The .wine folder is normally created in WinWoW (Win64) mode automatically then you start wine first and if there is no .wine dirctory in your home folder.

You can play the game with 6 usb controllers and 2 players at the keyboard - therefore a maximum of 8 players.

With the key F10 you can exit the game.
