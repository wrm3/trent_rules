@echo off

REM === Shared template root ===
set SHARED=G:\trent_rules\template_v2

REM === Current project folder (folder this script is in) ===
set PROJECT=%~dp0

echo.
echo Project folder detected as:
echo %PROJECT%
echo.

echo Creating junction links...

mklink /J "%PROJECT%.agent" "%SHARED%\.agent"
mklink /J "%PROJECT%.claude" "%SHARED%\.claude"
mklink /J "%PROJECT%.codex" "%SHARED%\.codex"
mklink /J "%PROJECT%.cursor" "%SHARED%\.cursor"
mklink /J "%PROJECT%.opencode" "%SHARED%\.opencode"
mklink /J "%PROJECT%.platforms" "%SHARED%\.platforms"

echo.
echo Done.
pause
