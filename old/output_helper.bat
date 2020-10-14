@echo off

:menu
mode con cols=40 lines=20
color 06
cls
echo        Manim output tool
echo.
echo.
echo   1.High quality
echo   2.low quality
echo   3.¹ØÓÚ
echo   4.ÍË³ö
echo.
echo.
echo.
echo.


:menuInput

set /p i= : 
if "%i%"=="1" goto HighOut
if "%i%"=="2" goto LowOut
goto menu

set Filename="PrintTexts"

:HighOut
python "C:\Program Files\Python37\Lib\manim\manim.py" test.py PrintTexts -p --high_quality
copy /-Y .\media\videos\test\1080p60\%Filename%.mp4 .\output
pause

:LowOut
python "C:\Program Files\Python37\Lib\manim\manim.py" test.py PrintTexts -p -l
copy .\media\videos\test\480p15\%Filename%.mp4 .\output
pause
:end