build_container:
	docker build . -t fluentnet_container

run_tests:
	docker-compose up 