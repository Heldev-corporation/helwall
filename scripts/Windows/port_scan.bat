@echo off

if "%~1"=="" (
    echo Usage: %0 ^<target_ip^>
    exit /b 1
)

set target_ip=%1
nmap -sS %target_ip%
