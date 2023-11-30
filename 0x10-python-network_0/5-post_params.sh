#!/bin/bash
# This script sends a POST request and two variables.
curl -sX POST "$1" -d "email=hr@holbertonschool.com&subject=I will always be here for PLD"
