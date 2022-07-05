chcp 65001
@echo off
call activate
call conda activate environment
streamlit run #主页.py
pause
