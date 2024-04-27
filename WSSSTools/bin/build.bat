pyinstaller -i ../icon.ico -F ../main.py --distpath=../../dist-version/WarpearDropSSTools/WSSSTools
xcopy /E /I /Y "..\res" "..\..\dist-version\WarpearDropSSTools\WSSSTools\res\"
xcopy /Y "..\..\README.md" "..\..\dist-version\WarpearDropSSTools\"