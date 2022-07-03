:: script to run from wsl bash
@echo on
title This is your first batch script!
echo Welcome to batch scripting!
echo Running python script!
call C:\Users\jf_mo\Desktop\automation\venv\Scripts\activate.bat
echo %2
pause
call python google.py %1 %2
echo "final"
pause