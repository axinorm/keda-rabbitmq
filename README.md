# RabbitMQ with Keda

## Build rabbitmq-receiver

```sh
cd receive
docker build . -t rabbitmq-receiver:latest
```

## Build rabbitmq-sender

```sh
cd send
docker build . -t rabbitmq-sender:latest
```

## Deploy in Kubernetes

You can use [Kind](https://kind.sigs.k8s.io/docs/user/local-registry/) with local registry to test this example.

```sh
kubectl create -f receive/deployment_rabbitmq_receiver.yaml
kubectl create -f send/job_rabbitmq_sender.yaml
```