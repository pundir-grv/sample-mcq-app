FROM python:3.10-alpine
RUN mkdir -p mcq_app
COPY src/requirments.txt /mcq_app/requirments.txt
RUN pip install -r /mcq_app/requirments.txt
ADD src/ /mcq_app/
WORKDIR /mcq_app
ENTRYPOINT ["python3", "app.py"]