#!/usr/bin/sh
cd "$(dirname "$0")"
echo "CWD: $(pwd)"

uvicorn server:api --reload
