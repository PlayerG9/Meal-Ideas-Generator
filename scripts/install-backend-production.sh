#!/usr/bin/sh
cd "$(dirname "$0")/../src/backend"
echo "CWD: $(pwd)"

if [ ! -f "./.venv/bin/python" ]  # test if virtual environment exists
then
  echo "virtual environment not found. creating one..."
  python3 -m venv .venv
  echo "virtual environment created."
  echo
fi

echo "Updating/Installing pip-packages"
./.venv/bin/pip install --isolated --upgrade pip
./.venv/bin/pip install --isolated -r ./requirements-production.txt

echo
echo "Project is ready to go"
echo
