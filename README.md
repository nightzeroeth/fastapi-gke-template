# fastapi-gke

gcloud artifacts repositories create helloworld-gke \
--project=helloworld-gke \
--repository-format=docker \
--location=us-west1 \
--description="helloworld-gke"

gcloud config set project helloworld-gke

gcloud builds submit --tag us-west1-docker.pkg.dev/helloworld-gke/helloworld-gke/helloworld-gke .

kubectl apply -f deployment.yaml

kubectl apply -f service.yaml

kubectl expose deployment helloworld-gke --type LoadBalancer --port 80 --target-port 8080

kubectl get deployments

kubectl get pods

kubectl get services

kubectl logs <pod_name>
