>> ### IF YOU ENJOY OUR REPOS, REACH OUT VIA EMAIL OR SOCIAL MEDIA FOR CUSTOMIZED SOLUTIONS 

>> ### DON'T FORGET TO RATE THIS REPO IF YOU FIND IT USEFUL!!!

<br/>

# AWS Lambda Function - Python Simple Flask API CloudFormation
This repo contains a project ready for deployment on AWS with the following features*:
 - A Python Flask simple API (/LambdaFunction)
 - Serverless AWS Infratsructure on CloudFormation IaC (/Infra)
 - Dedicated dependencies layer directory (/DependenciesLayer)

This project based is on the infrastructure provided by our product SCA: An API builder that generates a full CRUD API with swagger definitions to map any relational database with a complete and secure AWS infrastructure. We're able to provide your project with several infrastrucutures with all the features contained within this project and other customizable resources such as: Cognito for Authentication/Authorization, WAF (Web Application Firewalls), ElastiCache (Redis or Memcached) for low latency applications and full logging capabilities powered by Cloudwatch or Centralized Logs features (S3 + Glue + Athena).
For more information, visit our page and send us an inquiry: [SevenTechnologies](https://seventechnologies.cloud/)

## Requirements
[SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html), [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) and [AWS Account](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-creating.html).

</br>

## Deployment
* unzip DependenciesLayer/python.zip and make sure the directories structure looks like:
 
![Dependencies Layer Folder Structure](https://user-images.githubusercontent.com/106110465/181619678-54685dc8-6f5a-4db8-98f2-b7513f19be31.JPG)
* replace the parameters values after "--parameter-overrides", in the deployment command bellow. 
* sam deploy --profile {AWS_PROFILE} --template-file {TEMPLATE_NAME} --stack-name {STACK_NAME} --region {AWS_REGION} --capabilities CAPABILITY_NAMED_IAM --confirm-changeset --parameter-overrides CompanyName={COMPANYNAME} Owner={OWNER} ProjectType={PROJECTTYPE} EnvironmentName={ENVIRONMENTNAME} VpcCidr={VPCCIDR} PublicSubnet1CIDR={PUBLICSUBNET1CIDR} PublicSubnet2CIDR={PUBLICSUBNET2CIDR} PrivateSubnet1CIDR={PRIVATESUBNET1CIDR} PrivateSubnet2CIDR={PRIVATESUBNET2CIDR} PublicRouteDestinationCIDRBlock={PUBLICROUTEDESTINATIONCIDRBLOCK} PrivateRoute1DestinationCIDRBlock={PRIVATEROUTE1DESTINATIONCIDRBLOCK} PrivateRoute2DestinationCIDRBlock={PRIVATEROUTE2DESTINATIONCIDRBLOCK} MemorySize={MEMORYSIZE} TimeOut={TIMEOUT} LambdaWarmUpEventsState={LAMBDAWARMUPEVENTSSTATE}

* eg.:
* sam deploy --profile default --template-file template.yaml --stack-name test --region us-east-1 --capabilities CAPABILITY_NAMED_IAM --confirm-changeset --parameter-overrides ProjectName=TestProject CompanyName=TestCompany Owner=TestOwner ProjectType=TestType EnvironmentName=DEV VpcCIDR=10.192.0.0/16 PublicSubnet1CIDR=10.192.10.0/24 PublicSubnet2CIDR=10.192.11.0/24 PrivateSubnet1CIDR=10.192.20.0/24 PrivateSubnet2CIDR=10.192.21.0/24 PublicRouteDestinationCidrBlock=0.0.0.0/0 PrivateRoute1DestinationCidrBlock=0.0.0.0/0 PrivateRoute2DestinationCidrBlock=0.0.0.0/0 MemorySize=128 Timeout=29 LambdaWarmUpEventsState=DISABLED


