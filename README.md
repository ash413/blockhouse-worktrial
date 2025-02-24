# Trade Order API

A simple REST API for managing trade orders, built with **FastAPI** and deployed using **Docker** on **AWS EC2**. This project demonstrates how to build, containerize, and deploy a backend service with a CI/CD pipeline using **GitHub Actions**.

---

## Features
- **Submit Trade Orders**: Accepts trade order details (e.g., symbol, price, quantity, order type) via `POST /orders`.
- **List Orders**: Returns the list of submitted orders via `GET /orders`.
- **Real-Time Updates**: WebSocket support for real-time order status updates (bonus).
- **Database**: Stores order data in **SQLite** (for simplicity) or **PostgreSQL** (for production).

---

## Technologies Used
- **Backend**: Python (FastAPI)
- **Database**: SQLite (local), PostgreSQL (production)
- **Containerization**: Docker
- **Deployment**: AWS EC2
- **CI/CD**: GitHub Actions

---

## Setup

### Prerequisites
- Python 3.9+
- Docker
- AWS EC2 instance
- GitHub account

---

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/blockhouse-worktrial.git
   cd blockhouse-worktrial
    ```

2. Install dependencies:
    ```
    pip install -r requirements.txt
    ```

3. Run the application locally:
    ```
    uvicorn app.main:app --reload
    ```

4. Open the Swagger UI:
    ```
    http://localhost:8000/docs
    ```

### Docker Setup

1. Build the Docker image:
    ```
    docker build -t trade-app .
    ```

2. Run the Docker container:
    ```
    docker run -d -p 80:80 --name trade-app trade-app
    ```

3. Open the Swagger UI:
    ```
    http://localhost:80/docs
    ```

### Deployment on AWS EC2

1. Launch an EC2 instance (Ubuntu).

2. Install Docker on the EC2 instance:
    ```
    sudo apt update
    sudo apt install docker.io -y
    sudo systemctl start docker
    sudo systemctl enable docker
    ```

3. Copy your app to the EC2 instance:
    ```
    scp -r -i ~/.ssh/your-key.pem /path/to/your/app ubuntu@ec2-ip:/home/ubuntu/app
    ```

4. SSH into the EC2 instance:
    ```
    ssh -i ~/.ssh/your-key.pem ubuntu@ec2-ip
    ```

5. Build and run the Docker container:
    ```
    cd /home/ubuntu/app
    sudo docker build -t trade-app .
    sudo docker run -d -p 80:80 --name trade-app trade-app
    ```

6. Open the Swagger UI:
    ```
    http://ec2-ip/docs
    ```

---

## API Documentation

The API documentation is available via the Swagger UI:
    ```
    http://localhost:80/docs (local)
    http://ec2-ip/docs (AWS EC2)
    ```

---

## CI/CD Pipeline

The GitHub Actions workflow automates:
- Running tests on PRs.
- Building the Docker image.
- Deploying the app to AWS EC2 on merge to main.

