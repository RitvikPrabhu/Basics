#!/bin/bash

USERNAME="RitvikPrabhu"
REPO="CS6704-VT/Basics-Workshop"

# Prompt 1: Find all the starred repos for a specific (RitvikPrabhu) user

echo "All starred repos by $USERNAME are stored in starred_repos.json"
./githubapi-get.sh $GITHUBTOKEN "/users/$USERNAME/starred" | grep '"name":' > starred_repos.json

echo 

# Prompt 2: Find a list of open issues for a specific repository

echo "List of open issues in the $REPO repo are storred in open_issues.json"
./githubapi-get.sh $GITHUBTOKEN "/repos/$REPO/issues?state=open" | grep '"title":' > open_issues.json
