# ELK setup for COVID-19 SpaceApps challenge

## Prerequisites
- Prepare a VM or desktop PC with Docker runtime e.g. an Ubuntu droplet with min. of 2 GB memory --> in our case a DigitalOcean droplet with 8 GB Memory / 160 GB Disk / Ubuntu 18.04.3 (LTS) x64

## Instructions
- Clone the GIT repository "git clone https://github.com/deviantony/docker-elk"
- Extract archive to the Docker volumes location e.g. "/var/snap/docker/common/var-lib-docker/volumes/" by using "tar -xzvf var-lib-docker-volumes-docker_elk_elasticsearch.tar.gz"
- Switch to your "docker-elk" directory and run "docker-compose up"
- Login to Kibana web frontend e.g. "http://<IP>:5601/ using default credentials (username: elastic, password:changeme)
- Search for dashboard "COVID-19 Pandemic Integrated Simulator"
- Select timeframe 2020-01-01 to 2020-05-31