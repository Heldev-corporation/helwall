@echo off

if "%~1"=="" (
    echo Usage: %0 ^<target_ip/subnet^>
    exit /b 1
)

set target_ip=%1
nmap -sP %target_ip%
