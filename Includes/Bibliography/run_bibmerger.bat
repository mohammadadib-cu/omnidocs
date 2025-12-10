@echo off
set "PYTHON_SCRIPT=%~dp0\bibmerger.py"

if exist "%PYTHON_SCRIPT%" (
    echo Running bibmerger...
    python "%PYTHON_SCRIPT%"
) else (
    echo bibmerger.py not found at %PYTHON_SCRIPT%
)