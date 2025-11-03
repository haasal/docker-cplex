FROM eclipse-temurin:21

ARG CPLEX_INSTALLER
RUN if [ -z "$CPLEX_INSTALLER" ]; then echo "Error: CPLEX_INSTALLER build argument not set" >&2; exit 1; fi

COPY ${CPLEX_INSTALLER} /cplex/${CPLEX_INSTALLER}
COPY installer.properties /cplex/installer.properties

RUN chmod u+x /cplex/${CPLEX_INSTALLER}
RUN /cplex/${CPLEX_INSTALLER} -f /cplex/installer.properties
RUN rm -rf /cplex

# Python 3.10 installation (optional) dependencies
RUN apt-get update &&\ 
  apt-get install -y git build-essential gdb lcov pkg-config \
  libbz2-dev libffi-dev libgdbm-dev libgdbm-compat-dev liblzma-dev \
  libncurses-dev libreadline-dev libsqlite3-dev libssl-dev \
  lzma lzma-dev tk-dev uuid-dev zlib1g-dev libzstd-dev \
  inetutils-inetd

# Build and install Python 3.10 from source
RUN git clone -b 3.10 https://github.com/python/cpython
WORKDIR /cpython
RUN ./configure --enable-optimizations && \
  make -j $(nproc) && \
  make install
WORKDIR /
RUN rm -rf /cpython
