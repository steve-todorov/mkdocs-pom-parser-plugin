#!/bin/sh

RELEASED_VERSIONS=$(git tag -l)
REMOTE=$(git remote -v)

set -ex
while true; do
  read -p "Version: " VERSION

  if [ -z "${RELEASED_VERSIONS##*$VERSION*}" ]; then
    echo "This version has already been released! Pick another one";
  else
    break;
  fi
done

sed -i "s/version='.*',/version='$VERSION',/" setup.py

./build.sh

git tag "$VERSION"

echo $REMOTE

while true; do
  read -p "Push? [N|y]" PUSH
  case $yn in
    [Yy]* ) git push -u origin --all; break;;
    [Nn]* ) exit;;
    * ) echo "Please answer yes or no.";;
  esac
done

