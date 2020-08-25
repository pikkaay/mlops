# MLOPS - ML Models in production

Deploying ML models at scale in kubernetes cluster

## Includes

1. Simple Flask application which serve http request<br />
2. Health check GET method to get status of the Flask app<br />
3. Dockerfile to build docker image<br />
4. Configuration yaml files for kubernetes deployments<br />

## Usage
Working directory ./mlops/src/
```bash
docker build ti appname:latest .
docker run -d -p 5000:5000 appname:latest
```

Test the API using curl
```bash
curl localhost:5000/hcheck 
```
This will output json result with app status

Use the yaml configurations inside to deploy the app to a kubernetes cluster

Apply the deployments with kustomization.yaml using this command

```bash
kubectl apply --kustomize=./kubernetes-yaml-configs/ --record=true
```

Get the status of deployments using this command
```bash
kubectl get deployment -n mlops
```

Get the external ip address using this command
```bash
kubectl get service -n mlops
```

Output will look like this
```bash
NAME        TYPE           CLUSTER-IP    EXTERNAL-IP     PORT(S)          AGE
flask-app   LoadBalancer   xx.xx.xx.xx   xx.xx.xx.xx     5000:xxxx/TCP    20s
```
