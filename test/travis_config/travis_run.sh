#!/usr/bin/env bash

python -m coverage run  test/test_all.py
python -m coverage combine
python -m coverage report -m 2>&1