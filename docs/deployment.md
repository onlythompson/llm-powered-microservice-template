# Deployment Guide

[... previous content remains the same ...]

## Kubernetes Deployment

### Prerequisites

- Kubernetes cluster
- kubectl configured to communicate with your cluster
- Helm (optional, for managing Kubernetes applications)

### Steps

1. Create a Kubernetes secret for your environment variables:
   ```
   kubectl create secret generic llm-microservice-secrets --from-env-file=.env
   ```

2. Apply the Kubernetes manifests:
   ```
   kubectl apply -f k8s/
   ```

   This assumes you have Kubernetes manifest files (Deployment, Service, etc.) in a `k8s/` directory.

3. Verify the deployment:
   ```
   kubectl get pods
   kubectl get services
   ```

4. (Optional) If using Helm:
   ```
   helm install llm-microservice ./helm-charts/llm-microservice
   ```

## Scaling

### Horizontal Pod Autoscaler (HPA)

To automatically scale your deployment based on CPU usage:

1. Create an HPA:
   ```
   kubectl autoscale deployment llm-microservice --cpu-percent=70 --min=2 --max=10
   ```

2. Verify the HPA:
   ```
   kubectl get hpa
   ```

## Monitoring

1. Deploy Prometheus for monitoring:
   ```
   helm install prometheus stable/prometheus
   ```

2. Deploy Grafana for visualization:
   ```
   helm install grafana stable/grafana
   ```

3. Import the provided Grafana dashboard for LLM-specific metrics.

## Troubleshooting

- Check pod logs:
  ```
  kubectl logs <pod-name>
  ```

- Exec into a pod:
  ```
  kubectl exec -it <pod-name> -- /bin/bash
  ```

- Check events:
  ```
  kubectl get events --sort-by=.metadata.creationTimestamp
  ```

Remember to always test your deployment in a staging environment before applying changes to production.