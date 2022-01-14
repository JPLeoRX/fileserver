FROM python:3.8

# Common dependencies
RUN pip install requests==2.25.1
RUN pip install fastapi==0.63.0
RUN pip install uvicorn==0.13.3
RUN pip install injectable==3.4.4
RUN pip install aiofiles==0.8.0
RUN pip install simplestr==0.4

# Main app
COPY . /app
WORKDIR /app
RUN mkdir /output

# Run command
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "9001", "--workers", "1"]