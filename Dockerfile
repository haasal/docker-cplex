FROM cplex

COPY src/ /app/

WORKDIR /app

ENTRYPOINT ["/bin/bash"]
