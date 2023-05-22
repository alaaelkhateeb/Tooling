@echo off
setlocal EnableDelayedExpansion
SET inputFile=progress.txt
if not exist %inputFile% ( echo 0 > %inputFile% )


if exist %inputFile% ( 
	FOR /F "tokens=* delims=" %%x in (progress.txt) DO (
		set /A text =%%x+14
		echo !text! > %inputFile%
		
)
)

exit /B



