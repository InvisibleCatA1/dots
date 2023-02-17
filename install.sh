#~/bin/bash

read -p "Press any key to install InvisibleCat's dotfiles..."
echo ""

echo "Moving to config dir..."
config="/home/$USER/.config"
cd $config

echo "Retriving files..."
git init
git pull https://github.com/InvisibleCatA1/dots.git

echo "Install done!"
