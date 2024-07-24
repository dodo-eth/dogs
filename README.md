1) clone repo 
2) pip3 install -r requirements.txt
3) mv folder to /root/Dogs/
4) mv Dogs.service /etc/systemd/system/
5) sudo systemctl daemon-reload
6) systemctl start Dogs.service && systemctl enable Dogs.service