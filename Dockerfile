FROM cplex

COPY src/ /app/

WORKDIR /app

ENTRYPOINT ["python3", "HelloPython.py"]
