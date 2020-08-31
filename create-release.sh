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

git add setup.py
git commit -m "Releasing $VERSION"
git tag "$VERSION"

while true; do
  read -p "Next developer version: " NEXT_VERSION
  if [ -z "${RELEASED_VERSIONS##*NEXT_VERSION*}" ]; then
    echo "This version has already been released! Pick another one";
  else
    break;
  fi
done

sed -i "s/version='.*',/version='$NEXT_VERSION.dev1',/" setup.py
git add setup.py
git commit -m "Set the next development version."

./build.sh

echo $REMOTE

while true; do
  read -p "Push? [y|n] " PUSH
  case $PUSH in
    [Yy]* ) git push -u origin --all && git push -u origin --tags; break;;
    [Nn]* ) exit;;
    * ) echo "Please answer yes or no.";;
  esac
done

