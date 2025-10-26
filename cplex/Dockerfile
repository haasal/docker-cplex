FROM eclipse-temurin:21

ARG CPLEX_INSTALLER
RUN if [ -z "$CPLEX_INSTALLER" ]; then echo "Error: CPLEX_INSTALLER build argument not set" >&2; exit 1; fi

COPY ${CPLEX_INSTALLER} /cplex/${CPLEX_INSTALLER}
COPY installer.properties /cplex/installer.properties

RUN chmod u+x /cplex/${CPLEX_INSTALLER}
RUN /cplex/${CPLEX_INSTALLER} -f /cplex/installer.properties
RUN rm -rf /cplex
