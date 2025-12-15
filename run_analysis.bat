@echo off
echo ========================================
echo Marketing Campaign Analysis
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8 or higher
    pause
    exit /b 1
)

echo Checking for dataset...
if not exist "data\bank-marketing.csv" (
    echo.
    echo WARNING: Dataset not found!
    echo.
    echo Option 1: Download real dataset from Kaggle
    echo   https://www.kaggle.com/datasets/janiobachmann/bank-marketing-dataset
    echo   Place it in data\bank-marketing.csv
    echo.
    echo Option 2: Generate sample data for testing
    set /p choice="Generate sample data? (y/n): "
    if /i "%choice%"=="y" (
        echo Generating sample data...
        python src\generate_sample_data.py
        if errorlevel 1 (
            echo Failed to generate sample data
            pause
            exit /b 1
        )
    ) else (
        echo Please download the dataset and try again
        pause
        exit /b 1
    )
)

echo.
echo Installing required packages...
pip install -r requirements.txt
if errorlevel 1 (
    echo Failed to install packages
    pause
    exit /b 1
)

echo.
echo ========================================
echo Running Analysis...
echo ========================================
echo.

python src\main_analysis.py

echo.
echo ========================================
echo Analysis Complete!
echo ========================================
echo.
echo Check the outputs\figures folder for visualizations
echo.
pause
