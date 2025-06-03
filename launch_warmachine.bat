@echo off
REM Set working directory to project root
cd /d C:\Users\default.DESKTOP-H89VL85\Desktop\halal_warmachine

REM Activate virtual environment
call .venv\Scripts\activate

REM Launch Commander with logging
echo Starting Halal Warmachine... > commander_console_log.txt
python -m core.commander >> commander_console_log.txt 2>&1

REM Pause if crashed, keep command prompt open
echo.
echo [!!!] Halal Warmachine terminated or crashed.
echo [!!!] Check commander_console_log.txt for error details.
pause
