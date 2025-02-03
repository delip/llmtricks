source activate readertools
sh clean.sh
pip install -r requirements.txt
python update_version.py
# check if update_version.py failed
if [ $? -ne 0 ]; then
    echo "update_version.py failed"
    exit 1
fi
python -m build
twine upload dist/*