# Argo CD Deployment Guide

## Overview

Argo CD is a declarative, GitOps continuous delivery tool for Kubernetes. This guide will help you deploy Argo CD on your Kubernetes cluster and use it to manage your applications.

## Prerequisites

- A running Kubernetes cluster
- `kubectl` command-line tool installed and configured to interact with your cluster
- `helm` command-line tool installed (optional, but recommended for easier installation)

## Installing Argo CD

### Using kubectl

1. **Create the Argo CD namespace**:

   ```bash
   kubectl create namespace argocd
   ```

2. **Install Argo CD components**:

   ```bash
   kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
   ```

## Accessing the Argo CD API Server

### Port Forwarding

To access the Argo CD API server, use port forwarding:

```bash
kubectl port-forward svc/argocd-server -n argocd 8080:443
```

Open your browser and navigate to `https://localhost:8080`.

## Logging into Argo CD

### Get the Initial Admin Password

The initial password for the `admin` account is auto-generated and stored in a Kubernetes secret. To retrieve it, run:

```bash
kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d
```

### Login via CLI

You can log in to Argo CD using the `argocd` CLI:

1. **Install the Argo CD CLI**:
   Download the appropriate version of the Argo CD CLI from the [releases page](https://github.com/argoproj/argo-cd/releases).

2. **Login to Argo CD**:
   ```bash
   argocd login localhost:8080
   ```

   When prompted, use `admin` as the username and the password retrieved earlier.

### Login via Web UI

1. **Open the Web UI**:
   Navigate to `https://localhost:8080` in your browser.

2. **Login**:
   Use `admin` as the username and the password retrieved earlier.

### Deploying Applications with Argo CD
```
kubectl apply -f argocd/application.yaml
```
1. **Open the Web UI**:
   Navigate to `https://localhost:8080` in your browser and check the status of application.

## Additional Resources

- [Argo CD Official Documentation](https://argo-cd.readthedocs.io/)
- [Argo CD GitHub Repository](https://github.com/argoproj/argo-cd)
- [Helm Official Documentation](https://helm.sh/docs/)

