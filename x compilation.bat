start/w setversion.exe

pyinstaller -w -F -i "logo.ico" StatPro.py

xcopy %CD%\*.xltx %CD%\dist /H /Y /C /R

xcopy C:\vxvproj\tnnc-StaticProcess\StatProc\dist C:\vxvproj\tnnc-StaticProcess\ConsoleApp\ /H /Y /C /R

xcopy C:\vxvproj\tnnc-StaticProcess\StatProc\logo.ico C:\vxvproj\tnnc-StaticProcess\ConsoleApp\ /H /Y /C /R

::xcopy C:\vxvproj\tnnc-StaticProcess\StatProc\*.xltx C:\vxvproj\tnnc-StaticProcess\ConsoleApp\ /H /Y /C /R


