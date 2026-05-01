#!/usr/bin/env bash

set -o errexit
set -o nounset

alembic upgrade head
uvicorn app.main:app --host=0.0.0.0 --port=${PORT:-5000} --workers 4 --reload
