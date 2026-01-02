# Scalable Web Application on AWS

## Overview
This project demonstrates the deployment of a highly available and scalable web application on AWS using EC2, Application Load Balancer, Auto Scaling Groups, and CloudWatch monitoring

The application automatically scales EC2 instances based on CPU utilization and distributes traffic evenly across instances.




## Architecture
- EC2 instances running Apache HTTP Server
- Application Load Balancer for traffic distribution
- Auto Scaling Group with Launch Template
- CloudWatch metrics and scaling policies
- IAM roles and security groups for controlled access




## Key Features
- Load-balanced web traffic using ALB
- Automatic instance scaling based on CPU utilization
- Health checks to ensure high availability
- Monitoring with CloudWatch metrics




## Auto Scaling Configuration
- Minimum instances: 1
- Desired instances: 2
- Maximum instances: 3
- Scaling policy: Target tracking based on 50% average CPU utilization




## AWS Services Used
- Amazon EC2
- Application Load Balancer
- Auto Scaling Group
- Amazon CloudWatch
- IAM
- Amazon VPC




## Screenshots
All screenshots demonstrating the infrastructure and monitoring are available in the `screenshots` directory.




