#!/bin/bash
make build_container
docker-compose up
make run_tests