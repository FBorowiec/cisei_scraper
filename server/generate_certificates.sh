#!/usr/bin/env bash

set -e

DOMAIN="$1"

((!$#)) && echo No domain name supplied! && exit 1

docker compose run --rm certbot certonly --webroot --webroot-path /var/www/certbot/ -d "$DOMAIN"
