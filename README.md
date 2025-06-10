# interview-projects_technical-task-1

## Part 1 - Scalable Web Site

This repository contains a Dockerized single-page HTML website served via Nginx, designed for easy deployment and scalability in both on-premises and cloud environments.

---

### Tooling Used

- **Docker**: Containerizes the web server and the static website for consistent, portable deployments.
- **Nginx**: Lightweight, high-performance HTTP server to serve the static HTML content.
- **Docker Compose (optional)**: For local multi-container orchestration (if needed).
- **Kubernetes (optional)**: For production scaling and high availability.

---

### Scaling and High Availability Documentation

#### 1. **Container Scaling**

- **Docker Containers** can be scaled horizontally by running multiple container instances of the Nginx web server hosting the static website.
- On platforms like **Docker Swarm** or **Kubernetes**, you can easily define replicas (e.g., 3+ replicas) of the web server pod/service.

#### 2. **Load Balancing**

- Use a **Load Balancer** (e.g., AWS ELB, Nginx or HAProxy reverse proxy) in front of multiple container instances.
- The Load Balancer distributes incoming HTTP requests evenly to the healthy container instances, providing fault tolerance.

#### 3. **Service Discovery & Orchestration**

- Use container orchestrators with **Kubernetes** for:
  - Automatic service discovery.
  - Automated container health checks and restart on failure.
  - Rolling updates with zero downtime.
  - Autoscaling based on metrics (CPU, requests, etc.).

#### 4. **Persistent Storage & Configuration**

- Static content is baked into the Docker image, ensuring consistency across instances.
- For dynamic or frequently changing content, use shared volumes or cloud storage solutions.

#### 5. **Monitoring & Logging**

- Integrate with centralized logging (e.g., ELK stack) and monitoring tools (Prometheus, Grafana) for visibility and alerting.

---

### How to Run the Application

#### Prerequisites

- Docker installed (https://docs.docker.com/get-docker/)
- (Optional) Docker Compose for multi-container setups.

#### Build and Run Locally

1. **Clone the repository**

```bash
git clone https://github.com/username/repo.git
cd repo
docker build -t containerized-nginx-single-page-website .
docker run -d -p 8080:80 --name containerized-nginx-single-page-website
```

## Part 2 - AWS VPC Lister Lambda (Python)

This AWS Lambda function lists all VPCs and Subnets in your AWS account and saves them into a DynamoDB table named `NetworkResources`.

---

### Prerequisites

- AWS CLI configured
- AWS SAM CLI installed
- Python 3.9+

---

### Deployment with AWS SAM

1. **Install dependencies locally:**

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
