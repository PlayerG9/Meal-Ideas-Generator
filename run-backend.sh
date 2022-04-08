#!/usr/bin/sh
cd "$(dirname "$0")/src/backend"
echo "CWD: $(pwd)"

./.venv/bin/python3 -B -O ./server
# -B     : don't write .pyc files on import
# -O     : remove assert and __debug__-dependent statements
