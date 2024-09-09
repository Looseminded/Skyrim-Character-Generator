# Skyrim-Character-Generator
Offline character generator for Skyrim with file-saving functionality.  Written in Python.  Tested on both Windows and Debian-based Linux Systems.

Python 3.7.7 or later is required to run this.

If running Python 3.11.5, you will receive syntax errors in several lines regarding the use of "is" rather than "==". This will still operate as expected.

If running this from command line:

  python skyrimGenerator.py
  
  python3 skyrimGenerator.py
  
If running this via double-clicking:
  
  Program will operate as expected.

In either case, your terminal or command prompt will hang for 5 seconds as a result of time.sleep(5) at the end if you have chosen to save your generated stats.

This is intentional so that users have time to see where their file has been saved.

This has been written with the option of minorRolls.py being entirely optional.  If minorRolls does not exist, the program will skip over that functionality entirely.

skyrim.txt and skyrimModified.txt have been provided as examples of what output will look like.  It is not necessary that they exist prior to running the script.
