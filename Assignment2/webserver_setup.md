Objective:
	Set up an Apache web server on an Ubuntu instance to serve a file named `comp370_hw2.txt` from the www root, accessible via port 8008.



Step 1:	Connect to Your Lightsail Instance
Use SSH to connect to your Lightsail instance.

	$ ssh -i .ssh/id_comp370 ubuntu@3.96.210.148

Step 2: Update and Install Apache
pdate package lists and install Apache web server

	$ sudo apt update
	$ sudo apt install apache2

Step 3: Configure Apache to Listen on Port 8008
Edit the Apache ports configuration file.

	$ sudo nano /etc/apache2/ports.conf
	(can use vim or anything tp edit the file, inside the file there was a line saying Listen 80, changed it to 8008, saved and exit the file)

Step 4: Create a Virtual Host Configuration for Port 8008
Create a new virtual host configuration file.

	$ sudo nano /etc/apache2/sites-available/8008.conf
	(Again using vim or nano added the following configuration:
		     <VirtualHost *:8008>
         		DocumentRoot /var/www/html
        		 <Directory /var/www/html>
             			AllowOverride All
             			Require all granted
         		</Directory>
         		ErrorLog ${APACHE_LOG_DIR}/error.log
         		CustomLog ${APACHE_LOG_DIR}/access.log combined
    		     </VirtualHost>

	save and exit the file.)

Step 5: Enable the New Site Configuration

	$ sudo a2ensite 8008.conf
	(in some case you need to this:
	$ sudo systemctl reload apache2
	then try the 
	$ sudo a2ensite 8008.conf)

Step 6: Add the File to the Document Root
Create or modify the file `comp370_hw2.txt` in the `/var/www/html` directory.
	
	$ sudo nano /var/www/html/comp370_hw2.txt
	(Add the data you want and save and exit)

Step 7: Restart Apache to Apply Changes

	$ sudo systemctl restart apache2

Step 8: Update Security Rules on lightsail instance to allow inbound traffic on port 8008

	(lightsail console -> go to the instance -> "Networking" tab -> Click "Add rule" -> 
		"Application": Custom   	
		"Protocol": TCP
		"Port or range": 8008
		save)

Step 9: Verify
go to http://X.Y.Z.W:8008/comp370_hw2.txt , where X.Y.Z.W is my instance’s public IP address.



























	
