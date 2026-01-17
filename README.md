# K8s Docker Project

This project demonstrates the use of Docker and Kubernetes to deploy a simple web application with a backend and frontend.


- **backend/**: Contains the backend application code and its Dockerfile.
- **frontend/**: Contains the frontend application code and its Dockerfile.
- **k8s/**: Contains Kubernetes configuration files for deploying the backend and frontend services.

## Getting Started

### Prerequisites
- Docker
- Kubernetes (kubectl)

### Build and Run the Application
1. Navigate to the backend directory:
   ```bash
   cd backend
   ```
2. Build the Docker image:
   ```bash
   docker build -t backend-image .
   ```
3. Navigate to the frontend directory:
   ```bash
   cd ../frontend
   ```
4. Build the Docker image:
   ```bash
   docker build -t frontend-image .
   ```

### Deploying to Kubernetes
1. Apply the backend deployment:
   ```bash
   kubectl apply -f ../k8s/backend-deployment.yaml
   ```
2. Apply the backend service:
   ```bash
   kubectl apply -f ../k8s/backend-service.yaml
   ```
3. Apply the frontend deployment:
   ```bash
   kubectl apply -f ../k8s/frontend-deployment.yaml
   ```
4. Apply the frontend service:
   ```bash
   kubectl apply -f ../k8s/frontend-service.yaml
   ```

## Accessing the Application
- After deploying, you can access the application through the services defined in the Kubernetes configuration.

