[Simple Search Engine](http://104.131.95.18/SSE/)
============================================
### About this project
 * [Demo Page](http://104.131.95.18/SSE/)
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


============================================
## Reference:

--------------------------------------------
### About MySQL

[mysql error reference](http://mustgeorge.blogspot.com/2011/11/mysql-error-1045-28000-using-password.html)

run mysql
```
mysql -u root -p
```

[phpmyadmin](https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-phpmyadmin-on-ubuntu-14-04)

[MySQL reset pw](http://emn178.pixnet.net/blog/post/87659567-mysql%E4%BF%AE%E6%94%B9%E5%AF%86%E7%A2%BC%E8%88%87%E5%BF%98%E8%A8%98%E5%AF%86%E7%A2%BC%E9%87%8D%E8%A8%AD)


