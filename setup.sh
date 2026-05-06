#!/bin/bash


default_directory=$(pwd)
update_everything()
{
    echo "Updating Package Repo"
    sudo add-apt-repository ppa:deadsnakes/ppa -y >/dev/null
    sudo apt update -y >/dev/null
    echo "Installing Python 3.11 And Latest Java"
    sudo apt install python3 openjdk-25-jdk curl -y
    echo -e "\n Packages Installed Successfully!"

}

download_server()
{
    if [ ! -d server ]; then
        echo "Downloading Latest Fabric Server To server Folder"
        mkdir -p server
        curl -sL https://meta.fabricmc.net/v2/versions/loader/26.1.2/0.19.2/1.1.1/server/jar --output server/server.jar
        echo "Downloaded"
    else
        echo "Server Directory Already Exists Skipping Download!"
    fi
}

edit_server_config()
{
    echo "Editing Default Server Configs"
    sed -i 's/max-players=20/max-players=50/' server.properties
    sed -i 's/online-mode=true/online-mode=false/' server.properties
    sed -i 's/enable-query=false/enable-query=true/' server.properties
    sed -i 's/difficulty=easy/difficulty=hard/' server.properties
    sed -i 's/simulation-distance=10/simulation-distance=12/' server.properties
    sed -i 's/view-distance=10/view-distance=16/' server.properties
    sed -i 's/pause-when-empty-seconds=60/pause-when-empty-seconds=0/' server.properties
    
}
running_server()
{
    cd server
    echo "Accepting Eula Agreement"
    echo "eula=true" > eula.txt
    echo "Running Downloaded Server With 16gb Ram Once To Generate Server Config"
    java -Xmx16G -jar server.jar nogui >/dev/null & 
        PID=$!
        sleep 20
        kill $PID
        clear
    echo "Killed"
    edit_server_config
    echo "Server Configured Successfully!"
    cd $default_directory

}

#update_everything
download_server
running_server
sleep 5
clear
echo "Use python3 -m bot To Start The Bot"
echo ""