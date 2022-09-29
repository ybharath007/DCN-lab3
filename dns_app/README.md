# Bharath Yeddula
# DCN-lab3  

prerequisites :  
create a docker network named lab3  
> docker network create lab3  

1. To run the authoritative server, use below commands under AS directory  
> docker build -t ybharath007/as:latest .  
> docker run --network lab3 --name as -p 53533:53533/udp -it ybharath007/as:latest  

2. to run the fibonacci server, use below commands under FS directory  
> docker build -t ybharath007/fs:latest .  
> docker run --network lab3 --name fs -p 9090:9090 -it ybharath007/fs:latest  

3. to run the user server, use below commands under US directory  
> docker build -t ybharath007/us:latest .  
> docker run --network lab3 --name us -p 8080:8080 -it ybharath007/us:latest  

4. register a dns record by make a PUT request at http://0.0.0.0:9090/register  
pass below arguments as a json object. change ip to ipaddress of fibonacci server and as_ip as ipaddress of dns server  
{  
"hostname" : "fibonacci.com",  
"ip" : "172.18.0.2",  
"as_ip" : "172.18.0.3",  
"as_port" : "53533"  
}  

5. get the fibonacci value by making a GET request to http://0.0.0.0:8080/fibonacci?hostname=fibonacci.com&fs_port=9090&number=15&as_ip=172.18.0.3&as_port=53533  
change the parameters accordingly  
