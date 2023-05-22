SETLOCAL enabledelayedexpansion

set folderTxt="Text Files"
set folderSource="Source Files"
set folderHeader="Header Files"

if not exist %folderTxt% mkdir %folderTxt%
if not exist %folderSource% mkdir %folderSource%
if not exist %folderHeader% mkdir %folderHeader%


for /f "tokens=1-4 delims= " %%i in (input.txt) do (
    if not exist "%%i" mkdir "%%i"
    cd %%i
    if not exist "%%j" (
      echo 0>"%%j"
    )else (
      SET /P count=<"%%j"
      SET /A count=count+1
      ECHO !count! >"%%j"
    )
	if not exist "%%k" (
      echo 0 >"%%k"
    )else (
      SET /P count=<"%%k"
      SET /A count=count+1
      ECHO !count! >"%%k"
    )
	if not exist "%%l" (
      echo 0 >"%%l"
    )else (
      SET /P count=<"%%l"
      SET /A count=count+1
      ECHO !count! >"%%l"
    )
    cd ..\
	COPY /Y %%i\*.txt %folderTxt%
	COPY /Y %%i\*.c %folderSource%
	COPY /Y %%i\*.h %folderHeader%
)