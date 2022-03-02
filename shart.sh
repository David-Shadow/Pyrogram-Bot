if [ -z $UPSTREAM_REPO ]
then
  echo "COULD NOT FOUND UPSTREAM REPO... EXITING..."
  exit
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /RBot
fi
cd /RBot
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 -m bot
