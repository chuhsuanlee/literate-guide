DOCKER := docker

PROJECT_NAME := literate-guide
IMAGE_NAMESPACE := chuhsuanlee
IMAGE_VERSION := 0.1.0
IMAGE_REPO := $(IMAGE_NAMESPACE)/$(PROJECT_NAME):$(IMAGE_VERSION)

# APP_ENV is fetched from CI server depending on the environment
APP_ENV ?= dev

WORKDIR := $(shell pwd)
FLAG := \
	-v /etc/localtime:/etc/localtime \
	-v $(WORKDIR)/sources:/usr/src/sources


.PHONY: help
help:
	@echo "Usage:"
	@echo "    make <target>"
	@echo
	@echo "Targets:"
	@echo "    build"
	@echo "        Build docker image."
	@echo
	@echo "    clean"
	@echo "        Remove docker image."
	@echo
	@echo "    exec (CMD=<cmd>)"
	@echo "        Create container and execute specified command (default: bash)."
	@echo
	@echo "    run"
	@echo "        Create container and perform task."
	@echo

.PHONY: build
build:
	$(DOCKER) build \
		-f ops/Dockerfile \
		-t $(IMAGE_REPO) \
		.

.PHONY: clean
clean:
	$(DOCKER) rmi $(IMAGE_REPO) || true

.PHONY: exec
exec: build
	$(eval CMD ?= bash)
	$(DOCKER) run \
		--rm -it ${FLAG} \
		--entrypoint $(CMD) \
		$(IMAGE_REPO)

.PHONY: run
run: build
	$(DOCKER) run \
		--rm ${FLAG} \
		$(IMAGE_REPO)

.PHONY: publish
publish: build
	$(DOCKER) push $(IMAGE_REPO)

.PHONY: ci_master
ci_master: publish

.PHONY: ci_deploy
ci_deploy: kubectl apply -f "http://kubernetes-manifest-repos/$(PROJECT_NAME)?env=$(APP_ENV)"
