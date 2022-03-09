#!/usr/bin/sh
cd "$(dirname "$0")/src/frontend"
echo "CWD: $(pwd)"

if [ ! -f "./node_modules" ]  # test if virtual environment exists
then
  echo "Node modules not found. installing..."
  npm install
  echo "Node modules installed."
  echo
fi
