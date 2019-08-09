#!/bin/bash

set -e

# check requirements
REQS=( curl jq )
echo "1"
echo $REQS
for REQ in ${REQS[@]}
do
  echo "loop"
  echo $REQ
  which ${REQ} >/dev/null
  if [ ! $? -eq 0 ]; then
    echo "requirement ${REQ} is missing"
    exit 1
  fi
done
echo "2"
# set vars in project settings
BASE_URL=${BASE_URL:-$(echo $CI_PROJECT_URL |  cut -d'/' -f1-3)}
VARS=( BASE_URL PRIVATE_TOKEN PROJECT STAGE )

. <(curl -fsSL https://gitlab.com/morph027/gitlab-ci-helpers/raw/master/check-vars.sh)

check_vars
echo "3"
# fetch last successful build

DEFAULT_FILTER=".[] | select(.status==\"success\")  | select(.stage==\"${STAGE}\") | select(.ref==\"${REF:-develop}\")"
FILTER="$DEFAULT_FILTER"
echo "4"
if [ ! -z $COMMIT ]; then
  FILTER+=" | select(.commit.short_id==\"$COMMIT\")"
fi
echo "5"
LAST_SUCCESSFUL_BUILD=$(curl -s -H "PRIVATE-TOKEN: ${PRIVATE_TOKEN}" "${BASE_URL}/api/v4/projects/${PROJECT}/jobs?per_page=${PER_PAGE:-50}" | jq -c ''"$FILTER"' | {id}' | head -n1 | grep -oE '[0-9]+')
echo $LAST_SUCCESSFUL_BUILD
echo "6"
# download
download_latest() {
  [ -z $OUT_FILE ] && OUT_FILE="artifacts.zip"
  curl -fksSL -o ${OUT_FILE} -H "PRIVATE-TOKEN: ${PRIVATE_TOKEN}" "${BASE_URL}/api/v4/projects/${PROJECT}/jobs/${LAST_SUCCESSFUL_BUILD}/artifacts"
}
echo "7"
download_latest
echo "8"
