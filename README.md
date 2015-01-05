Simple Search Engine
============================================
### About this project
 * Inspired and learn from [Udacity CS 101](https://www.udacity.com/course/cs101)
 * Practice Python
 * [Diagram of Search Engine](https://www.udacity.com/wiki/CS101/Diagram)

--------------------------------------------
### Steps
 1. extract a link (function: get_next_target)
 2. get all the links from a page (function: print_all_links)

--------------------------------------------
### Enable Python CGI in apache2:
#### 1. check file permission to be executable
 ```
 ls -al
 chmod +x test.py
 chmod 755 test.py
 ```
#### 2. check conf
 ```
 cd /etc/apache2
 vim apache.conf
 ```
  in apache.conf, add following 
 ```
 <Directory /var/www>
     Options +ExecCGI
     AddHandler cgi-script .cgi .py
 </Directory>
 ```

#### 3. check module
 ```
 apache2ctl -M
 cgid_module (shared)
 a2enmod cgid
 ```

#### 4. ``` service apache2 restart ```
