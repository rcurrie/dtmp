build:
	docker build -t robcurrie/dtmp .

debug:
	docker-compose -f docker-compose-debug.yml up

run:
	docker-compose up -d

down:
	docker-compose -f docker-compose-debug.yml down

shell:
	docker exec -it dtmp_hub_1 /bin/bash

test:
	docker exec -it dtmp_hub_1 py.test -p no:cacheprovider -s -x
