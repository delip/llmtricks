source activate readertools
rm -Rf build dist llmtricks.egg-info
python update_version.py
# check if update_version.py failed
if [ $? -ne 0 ]; then
    echo "update_version.py failed"
    exit 1
fi
python setup.py sdist bdist_wheel
twine upload dist/*