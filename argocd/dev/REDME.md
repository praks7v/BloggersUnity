# Deploy Application on Minikube Cluster

## Overview

Minikube is a tool that makes it easy to run a single-node Kubernetes cluster locally. This guide will help you install Minikube on your machine and get started with Kubernetes.

## Installing Minikube
Follow the Minikube official documentation for [Minikube Installation](https://minikube.sigs.k8s.io/docs/start/).

## Prerequisites

- A compatible operating system (Windows, macOS, Linux)
- Virtualization software (like VirtualBox, VMware, Hyper-V, or KVM)
- `kubectl` command-line tool installed

## Getting Started
Clone the project to any directory where you do development work.
```
git clone https://github.com/praks7v/BloggersUnity.git
cd BloggersUnity
```

### Starting Minikube

1. **Start Minikube**:
   ```bash
   minikube start
   ```

2. **Verify Minikube Status**:
   ```bash
   minikube status
   ```

3. **Enable Ingress Addon**

Minikube comes with an Ingress addon which you need to enable:
```
minikube addons enable ingress
```
4. **Activate Minikube docker environment**
```
eval $(minikube docker-env)
```
5. **Add an entry to your `/etc/hosts` file to map `bloggersunity.com` to the Minikube IP**
```
echo "$(minikube ip) bloggersunity.com" | sudo tee -a /etc/hosts
```

6. **Build Docker image**
```
docker compose build . -f docker/docker-compose.yaml
```

7. **Apply Kubernetes configurations**

```
kubectl apply -f argocd/dev/bloggersunity-ingress.yaml
kubectl apply -f argocd/dev/deployment.yaml
```
8. **Check the status of Deployments**
```
kubectl get all
```
9. **Access the applicaton on web**
```
http://bloggersunity.com
```


### Managing Minikube

- **Stop Minikube**:
  ```bash
  minikube stop
  ```

- **Delete Minikube Cluster**:
  ```bash
  minikube delete
  ```

## Troubleshooting

### Common Issues
- **See the logs of Pods**:
  ```
  kubectl logs <pod-name-or-id>
  kubectl describe <pod-name-or-id>
  ```
- **Virtualization Not Enabled**:
  Ensure virtualization is enabled in your BIOS settings.
  
- **Insufficient Resources**:
  Allocate more resources (CPU, memory) to Minikube in your virtualization software.

- **Network Issues**:
  Restart your network or check firewall settings if Minikube cannot connect to the internet.

### Logs and Diagnostics

- **View Minikube Logs**:
  ```bash
  minikube logs
  ```

## Additional Resources

- [Minikube Documentation](https://minikube.sigs.k8s.io/docs/)
- [Kubernetes Documentation](https://kubernetes.io/docs/home/)
- [kubectl Documentation](https://kubernetes.io/docs/reference/kubectl/overview/)
