# simple blockchain

## Read blockchain:

1. After changing Python source code,
   rebuild Docker image `docker build -t <yentestblockchain> .`
2. Deploy k8s
   ```kubectl apply -f deployment.yaml
   kubectl apply -f service.yaml
   ```
3. Obtain new k8s pods name: `kubectl get pods`
4. View pod's logs: `kubectl logs <name of pod>`
5. Forward port: `kubectl port-forward service/<blockchain-service> 8080:80`
6. Look up the blockchain in browser: `http://127.0.0.1:8080/mine`

## Add block:

1. `curl -X POST -H "Content-Type: application/json" -d '{"sender": "sender_address", "recipient": "recipient_address", "amount": 5}' http://localhost:8080/transactions/new
`
