#!/bin/bash


default_directory=$(pwd)


create_service() {
    echo "Creating systemd service..."

    service_name="mc-bot"
    service_file="$service_name.service"

    cat <<EOF > $service_file
[Unit]
Description=Minecraft Server Manager Bot
After=network.target

[Service]
User=$USER
WorkingDirectory=$default_directory
ExecStart=/bin/bash start.sh
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
EOF

    echo "Moving service file..."
    sudo mv $service_file /etc/systemd/system/

    echo "Reloading systemd..."
    sudo systemctl daemon-reexec
    sudo systemctl daemon-reload

    echo "Enabling service..."
    sudo systemctl enable $service_name

    echo "Starting service..."
    sudo systemctl start $service_name

    echo "Service created and started!"
}



update_everything()
{
    echo "Updating Package Repo"
    sudo apt update -y >/dev/null
    echo "Installing Python 3.11 And Latest Java"
    sudo apt install python3 openjdk-25-jdk curl python3-pip python3-venv ufw -y >/dev/null
    echo "Starting venv To Install Python Packages"
    python3 -m venv .venv
    source .venv/bin/activate
    echo "Installing Python Packages"
    pip3 install -r requirements.txt >/dev/null
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
        sleep 30
        kill $PID
        clear
    echo "Killed"
    edit_server_config
    echo "Server Configured Successfully!"
    cd $default_directory

}

setup_firewall()
{
    echo -e "Enabling Port Forwarding\nEnter SUDO Password When Prompted!"
    sleep 1
    sudo iptables -P INPUT ACCEPT 
    sudo iptables -P FORWARD ACCEPT 
    sudo iptables -P OUTPUT ACCEPT 
    sudo iptables -F 
    sudo iptables-save 
    sudo ufw allow 25565/tcp
    sudo ufw --force enable
    sleep 1
    echo "Done"
}




update_everything
download_server
running_server
setup_firewall
sleep 5
clear
echo "Use python3 -m bot To Start The Bot"
echo ""
echo ""
echo "Do You Want To Add This Bot To Start Automatically On The Boot? Y/N"
read service
case $service in
        [Yy]* ) create_service;;
        [Nn]* ) exit;;
        * ) echo "Please answer Y or N.";;
esac
