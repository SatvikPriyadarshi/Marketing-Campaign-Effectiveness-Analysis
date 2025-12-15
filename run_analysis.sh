#!/bin/bash

echo "========================================"
echo "Marketing Campaign Analysis"
echo "========================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    echo "Please install Python 3.8 or higher"
    exit 1
fi

echo "Checking for dataset..."
if [ ! -f "data/bank-marketing.csv" ]; then
    echo ""
    echo "WARNING: Dataset not found!"
    echo ""
    echo "Option 1: Download real dataset from Kaggle"
    echo "  https://www.kaggle.com/datasets/janiobachmann/bank-marketing-dataset"
    echo "  Place it in data/bank-marketing.csv"
    echo ""
    echo "Option 2: Generate sample data for testing"
    read -p "Generate sample data? (y/n): " choice
    if [ "$choice" = "y" ] || [ "$choice" = "Y" ]; then
        echo "Generating sample data..."
        python3 src/generate_sample_data.py
        if [ $? -ne 0 ]; then
            echo "Failed to generate sample data"
            exit 1
        fi
    else
        echo "Please download the dataset and try again"
        exit 1
    fi
fi

echo ""
echo "Installing required packages..."
pip3 install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "Failed to install packages"
    exit 1
fi

echo ""
echo "========================================"
echo "Running Analysis..."
echo "========================================"
echo ""

python3 src/main_analysis.py

echo ""
echo "========================================"
echo "Analysis Complete!"
echo "========================================"
echo ""
echo "Check the outputs/figures folder for visualizations"
echo ""
