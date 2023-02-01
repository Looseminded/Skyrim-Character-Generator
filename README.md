# Skyrim-Character-Generator
Offline character generator for Skyrim with file-saving functionality.  Written in Python.  Tested on both Windows and Debian-based Linux Systems.

If running this from command line:

  python skyrimGenerator.py
  
  python3 skyrimGenerator.py
  
If running this via double-clicking:
  
  Program will operate as expected.

In either case, your terminal or command prompt will hang for 5 seconds as a result of time.sleep(5) at the end if you have chosen to save your generated stats.

This is intentional so that users have time to see where their file has been saved.

This has been written with the option of minorRolls.py being entirely optional.  If minorRolls does not exist, the program will skip over that functionality entirely.
