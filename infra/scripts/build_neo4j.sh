#! /usr/bin/env bash

#############
### BUILD ###
#############

set -e

# Change current working directory to be the root, regardless of how this script is invoked
cd "$(dirname "${BASH_SOURCE[0]}")/../.." || exit 1

pwd

# cd into source folder
cd src

# WORKAROUND: remove credsStore from .docker/config.json 

sed -i '' '/credsStore/d' ~/.docker/config.json 

# Build the docker image
docker build \
--tag "graph:latest" \
. || die "Failed to build"


#############
###  RUN  ###
#############

cd "$(dirname "${BASH_SOURCE[0]}")/.." || exit 1

# load env variables from .env file
export $(cat .env | xargs)

# stop any currently running containers and delete them
docker compose -f ./docker/docker-compose.yml down --volumes --remove-orphans

# start new containers
docker compose -f ./docker/docker-compose.yml up
