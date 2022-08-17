#! /bin/bash

echo "Compiling resources file..."
pyside6-rcc resources/resources.qrc -o resources/resources_rc.py
echo "Compiling user interface file..."
pyside6-uic ui/form.ui -o ui/ui_form.py
sed -i '/import resources_rc/d' ui/ui_form.py
sed -i '/from resources import resources_rc/d' ui/ui_form.py
sed -i '21i from resources import resources_rc' ui/ui_form.py
echo "Executing application!"
python3 main.py