# Makefile

ImageServ_Tag := fred1653/imageserv

build:
	DOCKER_BUILDKIT=1 docker build -f Dockerfile -t $(ImageServ_Tag) .

PHONY: build