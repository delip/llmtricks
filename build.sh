conda activate readertools
rm -Rf build dist llmtricks.egg-info
python update_version.py
python setup.py sdist bdist_wheel
twine upload dist/*