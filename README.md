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

Create the actual running image using the previously built `cplex` image:1

```bash
docker build -t cplex-demo .
```

Run and shell into the container (for demo purposes)

```bash
docker run --rm -it cplex-demo /bin/bash
```

Now compile the `HelloCplex.java` and run it:

> [!Note]
> You have probably to adjust the last part of the `java.library.path` to your architecture.
> I.e. Probably `x86-64_linux` instead of `arm64_linux`.

```bash
javac -cp javac -cp .:/opt/ibm/ILOG/CPLEX_Studio_Community2212/cplex/lib/cplex.jar HelloCplex.java
java -Djava.library.path=/opt/ibm/ILOG/CPLEX_Studio_Community2212/cplex/bin/arm64_linux/\
     -cp .:/opt/ibm/ILOG/CPLEX_Studio_Community2212/cplex/lib/cplex.jar\
     HelloCplex
```
