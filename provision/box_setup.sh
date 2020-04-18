#!/usr/bin/env bash

update_packages() {
    echo "Updating packages"
    sudo apt-get update -y
}

install_python() {
    echo "Installing Python"
    sudo apt-get install -y python3 > /dev/null 2>&1
    sudo apt-get install -y python3-pip > /dev/null 2>&1
    sudo apt-get install -y python3-venv > /dev/null 2>&1
}

create_venv() {
    echo "Creating Venv"
    sudo mkdir MusifyVenv
    cd MusifyVenv
    sudo python3 -m venv venv
    source venv/bin/activate
}

install_grpc() {
    echo "Installing gRPC"
    sudo pip install --no-cache-dir --upgrade pip
    # sudo pip install --no-cache-dir --trusted-host pypi.org --trusted-host files.pythonhosted.org --upgrade pip
    sudo python -m pip install grpcio --no-cache-dir
    sudo python -m pip install grpcio-tools --no-cache-dir
}

install_java() {
    sudo apt-get install -y default-jre
    sudo apt-get install -y default-jdk
}

clean_up() {
    echo "Cleaning"
    sudo apt -y autoremove && sudo apt autoclean > /dev/null 2>&1
}

setup() {
    update_packages
    install_python
    create_venv
    install_grpc
    install_java
    clean_up
}

setup "$@"
