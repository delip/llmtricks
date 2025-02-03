source activate readertools
sh clean.sh
pip install -r requirements.txt
python update_version.py
# check if update_version.py failed
if [ $? -ne 0 ]; then
    echo "update_version.py failed"
    exit 1
fi
VERSION=`cat pyproject.toml | grep version | cut -d'=' -f2 | tr -d ' '`
echo "Building version $VERSION"
python -m build
twine upload dist/*
git add .
git commit -m "Bump version to $VERSION"
git push