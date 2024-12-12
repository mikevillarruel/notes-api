override SHELL := /bin/bash

.PHONY: help
help: ## Show this help message
	@echo 'Usage:'
	@echo '  make [target] ...'
	@echo
	@echo 'Targets:'
	@grep --no-filename -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
	 sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
	@echo "------------------------------------"

.PHONY: build
build: ## Build images
	docker-compose --profile dev build

.PHONY: up
up: ## Run app and initialize database
	docker-compose --profile dev up -d

.PHONY: down
down: ## Remove containers
	docker-compose --profile "*" down --volumes --remove-orphans

.PHONY: clean
clean: ## Remove all (containers and images)
	docker-compose --profile "*" down --volumes --remove-orphans --rmi all

.PHONY: stop
stop: ## Stop app
	docker-compose --profile "*" stop

.PHONY: logs
logs: ## Show logs
	docker-compose --profile "*" logs -f

.PHONY: db_migrate
db_migrate: ## Create a new migration (e.g., make db_migrate comment="What did you change?")
	docker-compose --profile dev exec backend_dev alembic revision --autogenerate -m "$(comment)"

.PHONY: db_upgrade
db_upgrade: ## Upgrade database schema to the latest version
	docker-compose --profile dev exec backend_dev alembic upgrade head

.PHONY: db_downgrade
db_downgrade: ## Downgrade database schema to the previous version
	docker-compose --profile dev exec backend_dev alembic downgrade -1
