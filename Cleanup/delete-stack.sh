#!/bin/sh
for x in instancev2 instancev1 sgvpc-securitygroup sgpvpc;
do aws cloudformation delete-stack --stack-name $x; 
sleep 30; 
done
