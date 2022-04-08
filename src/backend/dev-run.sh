#!/usr/bin/sh
cd "$(dirname "$0")"
echo "CWD: $(pwd)"

./.venv/bin/python3 -m uvicorn server:api --reload
