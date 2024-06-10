# ArgoCD Project

## Overview
This project uses ArgoCD to manage and deploy Kubernetes applications using GitOps. ArgoCD ensures that the desired state of the Kubernetes cluster matches the state defined in the Git repository.

## Prerequisites
- Kubernetes cluster
- kubectl installed and configured
- ArgoCD installed and running in the Kubernetes cluster
- A Git repository containing the Kubernetes manifests

## ArgoCD Installation
If you haven't installed ArgoCD yet, you can follow these steps:

1. **Install ArgoCD**:
    ```bash
    kubectl create namespace argocd
    kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
    ```

2. **Install ArgoCD CLI**:
    Follow the instructions in the [ArgoCD documentation](https://argo-cd.readthedocs.io/en/stable/cli_installation/).

## Accessing ArgoCD
1. **Expose the ArgoCD API Server**:
    ```bash
    kubectl port-forward svc/argocd-server -n argocd 8080:443
    ```

2. **Login to ArgoCD**:
    Retrieve the initial password and log in using the CLI:
    ```bash
    kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d
    argocd login localhost:8080
    ```

## Configuring ArgoCD
1. **Create a new application**:
    ```bash
    argocd app create <app-name> \
        --repo https://github.com/your-repo/your-app.git \
        --path manifests \
        --dest-server https://kubernetes.default.svc \
        --dest-namespace <namespace>
    ```

2. **Synchronize the application**:
    ```bash
    argocd app sync <app-name>
    ```

## Directory Structure
Your Git repository should have a structure similar to this:

```
.
├── manifests
│   ├── deployment.yaml
│   ├── service.yaml
│   └── ...
└── README.md
```

## Kubernetes Manifests
Ensure your Kubernetes manifests are properly configured. For example, a basic `deployment.yaml` might look like:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: my-app
  template:
    metadata:
      labels:
        app: my-app
    spec:
      containers:
      - name: my-app
        image: my-app-image:latest
        ports:
        - containerPort: 80
```

## Managing Applications
You can manage your applications using the ArgoCD CLI or the web UI.

### Using the CLI
- **Get application status**:
    ```bash
    argocd app get <app-name>
    ```

- **Synchronize the application**:
    ```bash
    argocd app sync <app-name>
    ```

- **Delete the application**:
    ```bash
    argocd app delete <app-name>
    ```

### Using the Web UI
- Open `http://localhost:8080` in your browser.
- Log in using the username `admin` and the password retrieved earlier.
- Use the web interface to create, sync, and manage applications.

## Best Practices
- **GitOps Principles**: Treat your Git repository as the source of truth. All changes should be made via Git commits and pull requests.
- **Environment Segregation**: Use separate Git branches or repositories for different environments (e.g., dev, staging, production).
- **Automated Sync**: Configure ArgoCD to automatically sync your applications with the repository state.

## Troubleshooting
- **Check Application Logs**: Use the ArgoCD UI or CLI to view application and sync logs.
- **Ensure Correct Permissions**: Ensure ArgoCD has the necessary permissions to manage resources in the target namespaces.
- **Review Manifests**: Double-check your Kubernetes manifests for any syntax or configuration errors.

## Contributions
Feel free to submit pull requests or open issues if you encounter any problems or have suggestions for improvements.

## License
This project is licensed under the MIT License.

---

Happy deploying with ArgoCD!
```

Feel free to customize this template to better fit your specific project's requirements and workflows.
