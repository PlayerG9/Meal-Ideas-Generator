#!/usr/bin/sh
echo "Hello World"
cd "$(dirname "$0")/src/backend"
echo "CWD: $(pwd)"

npm start
