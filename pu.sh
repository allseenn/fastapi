#!/usr/bin/bash
# Script push on githab local repo and pull updates on remote SWEB host
WORK_DIR=$(dirname "$0")
TOKENS_FILE=$WORK_DIR/tokens.py
# UNCOMMENT FOR DEBUG
# LOG_FILE=$WORK_DIR/duck.log
# exec > $LOG_FILE 2>&1  
# set -x
# Set MAX_TRIES of every loop
SWEB_HOST=$(grep SWEB_HOST $TOKENS_FILE | awk '{print $3}' | sed s/\"//g)
SWEB_LOGIN=$(grep SWEB_LOGIN $TOKENS_FILE | awk '{print $3}' | sed s/\"//g)
SWEB_PASSWORD=$(grep SWEB_PASSWORD $TOKENS_FILE | awk '{print $3}' | sed s/\"//g)
SWEB_TOKEN=$(curl -s -H 'Content-Type: application/json; charset=utf-8' \
     -H 'Accept: application/json' \
     --data "{\"jsonrpc\":\"2.0\",\"method\":\"getToken\",\"params\":{\"login\":\"$SWEB_LOGIN\",\"password\":\"$SWEB_PASSWORD\"},\"id\":1}" \
     https://api.sweb.ru/notAuthorized/ | grep -oP '(?<="result":")[^"]*')
url="https://api.sweb.ru/vh/utils"
headers=(-H "Content-Type: application/json; charset=utf-8" -H "Accept: application/json" -H "Authorization: Bearer $SWEB_TOKEN")
payload='{"jsonrpc":"2.0","method":"sshOn","params":{"period":"24"}}'
response=$(curl -s -X POST "${headers[@]}" -d "$payload" "$url")

echo $response
git pull
git add .
git commit
git push

ssh sweb "cd fastapi && git pull"

if [ -n $1 ]; then
    ssh sweb "./fastapi.sh $1"
fi
