# Dockerized CPLEX Setup

> [!Important]
> This is a fork by [Alexander Haas](https://github.com/haasal) of the original project by [Victor San Kho Lin](https://github.com/victorskl/docker-cplex).
> This fork makes some changes to the Docker image and adds python support.

# Building the Docker Image

```bash
cd cplex
docker build\
  -t cplex\
  --build-arg CPLEX_INSTALLER=cos_installer_preview-22.1.2.R4-M0N99ML-linux-arm64.bin\
  .
```

The docker image should now be available under `cplex`.

# Running java code

Create the actual running image using the previously built `cplex` image

```bash
docker build -t cplex-demo .
```

Run the demo container with the python script in the `src` directory

```bash
docker run --rm -it cplex-demo
```
