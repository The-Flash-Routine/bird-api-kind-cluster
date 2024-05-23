## Bird Weather API
This app displays basic information about birds and weather.

### Pre Read

- To test this app on Kubernetes cluster we will be using KIND CLI to create a local Kubernetes cluster
- Nginx's Ingress Controller will be used for Ingress
- App uses a test database
- App uses opensource weather API i.e. api.weather.gov

### Steps to deploy app
1. Build image
```
docker build . -t bird:v1
```

2. Create Kubernetes cluster
```
kind create cluster --name sayari
```

3. Load locally built docker image in KIND's kubernetes cluster. Optionally, we can also publish image to an image registry such as dockerhub and then pull from there.
```
kind load docker-image bird:v1 --name sayari
```

4. Deploy Nginx's Ingress Controller
```
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.10.1/deploy/static/provider/cloud/deploy.yaml
```

5.  Wait for Ingress Controller pods to be ready
``` 
kubectl get pods -n ingress-nginx
```

6. As KIND's cluster is local, so we won't be getting External IP for Service Type LoadBalanacer, so we use port forwarding to reach Ingress Controller. If we were on any cloud such as GCP, we won't need this step. 
```
kubectl port-forward -n ingress-nginx service/ingress-nginx-controller 8080:80
```

7. Create a namespace to deploy the Bird Weather API
``` 
kubectl create ns birds
```

8. Deploy package using helm for first time
```
helm install birds helm/birds -n birds
```

9. For later revisions use 
```
helm upgrade birds helm/birds -n birds
```

10. Now the API should be accessible from local machine. Example:
```
curl --request GET 'http://127.0.0.1:8080/IN'
```


10. Teardown. Delete KIND's Kubernetes cluster
```
kind delete cluster --name sayari
```



