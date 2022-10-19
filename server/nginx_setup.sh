#!/bin/bash

DOMAIN="$1"

((!$#)) && echo No arguments supplied! && exit 1

apt install nginx certbot python3-certbot-nginx
cp /etc/nginx/sites-available/default /etc/nginx/sites-available/"$DOMAIN"
touch /etc/nginx/sites-available/"$DOMAIN"

echo "server {
    listen 80 ;
    listen [::]:80 ;
    root /var/www/${DOMAIN};
    index index.html index.htm index.nginx-debian.html;
    server_name ${DOMAIN} www.${DOMAIN};
    location / {
        try_files \$uri \$uri/ =404;
    }
}" >/etc/nginx/sites-available/"$DOMAIN"

ln -s /etc/nginx/sites-available/"$DOMAIN" /etc/nginx/sites-enabled/default
mkdir -p /var/www/"$DOMAIN"
#
# Add your website inside `/var/www/domain`
echo "<h1>DOMAINEXAMPLE Hello World!</h1>" >>/var/www/"$DOMAIN"/index.html
systemctl reload nginx
### Install certbot
certbot --nginx -d "$DOMAIN" -d www."$DOMAIN"
