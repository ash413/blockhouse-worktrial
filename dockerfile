# python runtime
FROM python:3.9-slim

#working directory
WORKDIR /app

# requirements file
COPY requirements.txt .

# install dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

#everything else
COPY . .

#expose port for fast api
EXPOSE 80

#run aspplication
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]

