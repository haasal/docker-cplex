# Dockerized CPLEX Setup

# Building the Docker Image

Copy your installer into the `cplex` directory.
Then build the docker image with the following command, replacing the installer name to your specific installer file:

```bash
cd cplex
docker build\
  -t cplex\
  --build-arg CPLEX_INSTALLER=cos_installer_preview-22.1.2.R4-M0N99ML-linux-arm64.bin\
  .
```

The docker image should now be available locally under `cplex`.

# Running java code

Create the actual running image using the previously built `cplex` image

```bash
docker build -t cplex-demo .
```

Run the demo container with the python script in the `src` directory

```bash
docker run --rm -it cplex-demo
```
