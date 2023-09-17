# unraid-json-api-external

Simple Express service for exposing your Unraid JSON API (by CyanLabs) without needing auth.

Requires installing this plugin on your Unraid server:
https://cyanlabs.net/applications/jsonapi-unraid/

## Usage

1. Install the plugin from CyanLabs on your Unraid server
2. Install this docker container in host mode
3. Fetch the API at `http://<unraid_ip>:<docker_port>/{query}`

## Available queries

- cpuload.ini
- devs.ini
- diskload.ini
- disks.ini
- monitor.ini
- network.ini
- sec.ini
- sec_afp.ini
- sec_nfs.ini
- shares.ini
- users.ini
- var.ini
