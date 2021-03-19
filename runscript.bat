@echo on
SET check_version=3.0
SET python_version=$(python -V 2>&1)
echo $python_version
: " install the dependencies needed for the application to run"


pip install pip
pip3 install -r requirements.txt
: " gives permission for the execution file and runs it "
chmod +x %CD%\runscript.bat
chmod +x %CD%\main.py
python main.py
EXIT /B 0