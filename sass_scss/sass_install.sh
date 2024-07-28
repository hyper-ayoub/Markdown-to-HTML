#!/bin/bash

# Install Sass/Scss 
echo -e "start installing ..."

sudo apt-get install -y ruby2.5 ruby2.5-dev
sudo apt-get install ubuntu-dev-tools
gem install sass -v 3.7.4
sass --version

echo "Sass has benn installing"


