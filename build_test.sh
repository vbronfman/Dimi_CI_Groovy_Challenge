#!/usr/bin/env bash
# bogus test prints the hash of the current git commit and waits ~3 min It is expected to always pass 

echo Test on commit
echo $(git rev-parse HEAD)
sleep ${timeout=3}



