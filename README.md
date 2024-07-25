1) clone repo 
2) pip3 install -r requirements.txt
3) mv folder to /root/dogs/
4) mv dogs.service /etc/systemd/system/
5) sudo systemctl daemon-reload
6) systemctl start dogs.service && systemctl enable dogs.service
7) csv format disc,http proxy,tgid