#!/usr/bin/env bash
#Here we run all the DB mock data population
cd app
flask init-db
flask run --host=0.0.0.0