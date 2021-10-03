#!/usr/bin/env bash
pip freeze | grep -v "grapejuice" > requirements.txt
echo "Requirements were compiled"