#!/bin/bash

sudo apt-get install software-properties-common
sudo apt-add-repository universe
sudo apt-get update
sudo apt-get install python3-pip

export SLUGIFY_USES_TEXT_UNIDECODE=yes

sudo pip install apache-airflow --user

PATH=$PATH:root/.local/bin

airflow db init