#!/bin/bash

#yum install -y git libffi-devel zlib-devel bzip2-devel readline-devel sqlite-devel ncurses-devel openssl-devel lzma-sdk-devel redhat-rpm-config wget curl llvm
#curl -L  https://raw.github.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash

#echo '
#export PYENV_ROOT="$HOME/.pyenv"
#export PATH="$PYENV_ROOT/bin:$PATH"
#eval "$(pyenv init -)"
#eval "$(pyenv virtualenv-init -)"
#' >> ~/.bashrc
#source ~/.bashrc

pyenv install 3.7.5
pyenv install 2.7.17

pyenv virtualenv 3.7.5 phardzeyeu3
pyenv virtualenv 2.7.17 phardzeyeu2

pyenv versions
