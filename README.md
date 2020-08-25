# MLOPS - ML Models in production

Deploying ML models at scale in kubernetes cluster

## Includes

1. Simple Flask application which serves http request<br />
2. GET method for Health check<br />
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

In the flask app (`main.py`), add a POST method to get prediction from a real ML model.<br /> 
Change the kubernetese yaml configuration files to A/B test the model versions and to play with additional nodes and pods as well<br />
Test the latency and load balancer with JMeter

