# unraid-json-api-external

Simple Python server that exposes Unraid's emhttp `.ini` state files as JSON without needing auth.

It reads the files directly from `/var/local/emhttp` (the same output the CyanLabs JSON API plugin used to give), since Unraid 7 puts the plugin's endpoint behind the web UI login.

## Usage

1. Install this docker container and mount `/var/local/emhttp` (host) to `/emhttp` (container) read-only
2. Fetch the API at `http://<unraid_ip>:<docker_port>/{query}`

Only `disks.ini` is served by default. Set `ALLOWED_FILES` to a comma-separated list to expose more.

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
