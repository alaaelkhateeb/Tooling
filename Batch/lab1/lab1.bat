@echo off

if [%3]==[] goto INEntry
if [%2]==[] goto INEntry
if [%1]==[] goto INEntry
set text=%1
set file=%2
set folder=%3
if exist %folder% (

goto dir
)
mkdir %folder%

:dir
cd %folder%
attrib -r %file%
echo %text%>%file%
attrib +r %file%
cd..

goto end
:INEntry
echo Invalid INPUT

:end