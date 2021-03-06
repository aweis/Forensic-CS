#!/bin/sh
PYTHON='/usr/bin/python'
GIT_FILENAME='git-1.7.7.3-intel-universal-snow-leopard'
GIT_VOLUME='/Volumes/Git 1.7.7.3 Snow Leopard Intel Universal/'
GFORTRAN='gcc-42-5666.3-darwin11.pkg'
SUDO='sudo'

if [ -z "$VIRTUAL_ENV" ]; then
    # Standard Python env
    PYTHON=/usr/bin/python
    SUDO=${SUDO}
else
    # Virtualenv
    PYTHON=python
    SUDO="" #${SUDO} is not required in a virtualenv
fi

echo 'Are you installing from a repository cloned to this machine (if unsure, answer no)? (y/n)'
read local
if  [ "$local" == "y" ] || [ "$local" == "Y" ]; then
    
    SUPERPACK_PATH='.'
    
elif [ "$local" == "n" ] || [ "$local" == "N" ]; then
    
    SUPERPACK_PATH='ScipySuperpack'
    
    hash git &> /dev/null
    if [ $? -eq 1 ]; then
        echo 'Downloading Git for OS X ...'
        curl -o ${GIT_FILENAME}.dmg http://git-osx-installer.googlecode.com/files/${GIT_FILENAME}.dmg
        echo 'Installing Git ...'
        hdiutil mount ${GIT_FILENAME}.dmg
        ${SUDO} installer -pkg "${GIT_VOLUME}${GIT_FILENAME}.pkg" -target '/'
        hdiutil unmount "${GIT_VOLUME}"
        echo 'Cleaning up'
        rm ${GIT_FILENAME}.dmg
        echo 'Cloning Scipy Superpack'
        /usr/local/git/bin/git clone git://github.com/fonnesbeck/ScipySuperpack.git
    else
        echo 'Cloning Scipy Superpack'
        git clone git://github.com/fonnesbeck/ScipySuperpack.git
    fi
    
else
    echo 'Did not recognize input. Exiting'
    exit 0
fi

# hash gfortran &> /dev/null
# if [ $? -eq 1 ]; then
echo 'Downloading gFortran ...'
curl -o ${GFORTRAN} http://r.research.att.com/tools/${GFORTRAN}
echo 'Installing gFortran ...'
${SUDO} installer -pkg ${GFORTRAN} -target '/'
# fi

hash easy_install &> /dev/null
if [ $? -eq 1 ]; then
    echo 'Downloading ez_setup ...'
    curl -o ez_setup.py http://peak.telecommunity.com/dist/ez_setup.py
    echo 'Installing ez_setup ...'
    ${SUDO} "${PYTHON}" ez_setup.py
    rm ez_setup.py
fi

echo 'Installing Scipy Superpack ...'
${SUDO} "${PYTHON}" -m easy_install -N -Z ${SUPERPACK_PATH}/*.egg

echo 'Installing readline ...'
${SUDO} "${PYTHON}" -m easy_install -N -Z readline
echo 'Installing nose ...'
${SUDO} "${PYTHON}" -m easy_install -N -Z nose
echo 'Installing DateUtils'
${SUDO} "${PYTHON}" -m easy_install -N -Z DateUtils

if  [ "$local" == "n" ] || [ "$local" == "N" ]; then  
    echo 'Cleaning up'  
    rm -rf ${SUPERPACK_PATH}
fi

echo 'Done'