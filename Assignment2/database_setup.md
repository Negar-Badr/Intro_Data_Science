Objective:
Set up a MariaDB database server on an Ubuntu lightsail instance to be accessible from the public internet on port 6002. 
The database will be named `comp370_test`, and the user `comp370` will have access with the password `$ungl@ss3s`.


Step 1:	Connect to Your Lightsail Instance
Use SSH to connect to your Lightsail instance.

	$ ssh -i .ssh/id_comp370 ubuntu@3.96.210.148

Step 2: Update and Install MariaDB server

	$ sudo apt update
	$ sudo apt install mariadb-server

Step 3: Configure MariaDB to run on external port
Edit MariaDB configuration

	$ sudo nano /etc/mysql/mariadb.conf.d/50-server.cnf
	( after the [mysqld] line add the port = 6002, or if it already exists just change it)
	( blind to all IP addresses: set the blind-address to 0.0.0.0 to allow external connections)

Step 4: restart MariaDB service:

	$ sudo systemctl restart mariadb

Step 5: Create an Empty Dataabse Named: comp370-test
login to MariaDB
		
	$ sudo mysql
	(inside the file: 
		CREATE DATABASE comp370_test;
	and then type exit)

Step 6: Add a new user to the Database
login to MariaDB

	$ sudo mysql
        (inside the file:
		CREATE USER 'comp370'@'%' IDENTIFIED BY '$ungl@ss3s';
		GRANT ALL PRIVILEGES ON comp370_test.* TO 'comp370'@'%';
		FLUSH PRIVILEGES;
	 and then type exit)

Step 7: Ensure MAriaDB is publicly accessible
	
	(lightsail console -> go to the instance -> "Networking" tab -> Click "Add rule" -> 
		"Application": Custom   	
		"Protocol": TCP
		"Port or range": 6002
		save)

Step 8: Ensure local firewall allows Port 6002
	
	$ sudo ufw allow 6002/tcp

Step 9: Download a database client in this case : DBeaver on the local machine

	(Once installed, click on the plus to add a new data base -> 
		Choose MariaDB -> Next -> in the new page change the following:
			Server Host: the pub IP address (3.96.210.148)
			Username: Comp370
			Password: $ungl@ss3s
			Port: 6002
		then Test the Connection, once it's connected check ok and it's done)
	







	
