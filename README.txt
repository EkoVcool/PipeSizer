1. Copy the "Pipe Sizer" folder located in the same folder as this README file into: C:\Program Files

2. Install Miniconda 3 for Windows and Python 3.8 from this location: https://docs.conda.io/en/latest/miniconda.html

3. Once Miniconda 3 is installed, type 'Anaconda' in the "Type here to search" area on the task bar.

4. Open the Anaconda Command Prompt.

5. Copy and paste this text into the command prompt and hit enter: conda install pyinstaller

6. Wait for the installation to finish. If it fails install do to permissions then you need to open the command prompt as an administrator.

7. Copy and paste this text into the command prompt and hit enter: cd C:\Program Files\Pipe Sizer

8. Copy and paste this text into the command prompt and hit enter: pyinstaller --onefile --icon=icons8-piping-96.ico PipeSizer.py

9. Wait for it to finish installing.

10. Navigate in your file explorer to: C:\Program Files\Pipe Sizer\dist

11. Create a shortcut of the "PipeSizer" file.

12. Move the shortcut to your desktop.

13. Check to make sure the shortcut works.

14. You are now done! If it isn't working get Erik.

15. For updates, simply copy the new "PipeSizer.py" file from the folder on the server and use it to replace to file on your PC, then open the "Anaconda Command Prompt" and repeat step 8 above. Make sure you are replacing the file in the main "Pipe Sizer" folder and NOT the application in the dist folder.