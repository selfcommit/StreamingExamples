BUILD_VERSION=2

set_project:
	gcloud config set project selfcommit-hello

dispatch:
	appcfg.py update_dispatch -A selfcommit-hello .

default:
	appcfg.py --version=${BUILD_VERSION} update gae_bundle/default

rando:
	appcfg.py --version=${BUILD_VERSION} update gae_bundle/rando
test:
	dev_appserver.py gae_bundle/default gae_bundle/rando dispatch.yaml

release: set_project default rando dispatch
	@echo Release successful!