social-sign-in
==============

Install Python
--------------
To check if Python is already on your system, open Command Prompt (Windows) or Terminal (Mac, Linux) and type:

    python --version
  
If it reports back a version number, you have python installed. If it complains, go install python.

Running the Program
-------------------
Open a Terminal / Command Prompt window and navigate to this directory.
(Sometimes you can right-click or shift right-click in a folder to open a console there).

Then type:

    python -B -O SocialSignInApp.py

This may open your browser and ask you to sign in and give the program permission to talk to Google Sheets. Do it.

For those who care, the `-B` tells python not to create a billion complied bytecode `.pyc` files and dump them in your directory, making it difficult to tell which files are the real source code.

The `-O` disables debug mode. Leave it out if you want to see a bunch more garbage fly by on the console window as you operate the program.
