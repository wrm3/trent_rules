@echo off

REM === Shared template root ===
set SHARED=G:\trent_rules\shared

REM === Current project folder (folder this script is in) ===
set PROJECT=%~dp0

echo.
echo Project folder detected as:
echo %PROJECT%
echo.

echo Creating junction links...

mklink /J "%PROJECT%.agent" "%SHARED%\.agent"
mklink /J "%PROJECT%.claude" "%SHARED%\.claude"
mklink /J "%PROJECT%.cursor" "%SHARED%\.cursor"
mklink /J "%PROJECT%.platforms" "%SHARED%\.platforms"

echo.
echo Done.
pause
