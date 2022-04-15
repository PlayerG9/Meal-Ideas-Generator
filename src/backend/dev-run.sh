#!/usr/bin/sh
set -e
cd "$(dirname "$0")"
echo "CWD: $(pwd)"

./.venv/bin/python3 -m uvicorn server:api --reload
