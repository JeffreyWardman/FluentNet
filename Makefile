build_container:
	docker build . -t fluentnet_container --no-cache

run_tests:
	docker-compose up 