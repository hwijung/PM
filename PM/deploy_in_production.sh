# Copy this script to root directory you want to deploy and execute.
wget https://github.com/hwijung/PM/archive/master.zip
unzip master.zip
mv /home/hwijung/workspace/PM-master/PM /home/hwijung/workspace/PM
rm -r PM-master
rm master.zip

# authorize directories
chown www-data:www-data /home/hwijung/workspace/PM
chown www-data:www-data /home/hwijung/workspace/PM/db.sqlite3

