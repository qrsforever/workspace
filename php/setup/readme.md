
 
# 管理php包
# https://www.phpcomposer.com/composer-the-new-age-of-dependency-manager-for-php/
curl -sS https://getcomposer.org/installer | php
sudo mv composer.phar /usr/local/bin/composer
composer install

sudo apt-get install mysql-server mysql-client
sudo apt-get install apache2

sudo apt-get install php5-dev
sudo apt-get install php5-mysql
# dpkg-query --status php5-mysql | grep Status
