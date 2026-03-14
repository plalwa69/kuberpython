import time
import sys

number = 10

if len(sys.argv) > 1:
    number = int(sys.argv[1])

if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# Keep container running
time.sleep(3600)




// docker login
// docker build -t username/imagename .
//docker push username/imagename
// kubectl apply -f deployment.yaml
// kubectl get pods 
//kubectl log <pods>
