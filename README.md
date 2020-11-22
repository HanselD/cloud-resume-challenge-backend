# Cloud Resume Challenge Backend

## Overview

This project was a result of a challenge introduced by AWS Serverless Hero, Forrest Brazeal. The challenge was to use the AWS cloud to host your resume online. See details [here](https://cloudresumechallenge.dev/).

This repo contains the backend services needed for the visitor count function. It is deployed using the [Serverless Framework](https://www.serverless.com/framework/docs/providers/aws/guide/intro/). It deploys an API Gateway which invokes a Lambda function. The Lambda function increments by 1 and retrieves the number of visitors to the website from DynamoDB. A GitHub Actions pipeline tracks changes in the repo, runs tests and deploys the stack. 

For frontend code, visit [Cloud Resume Frontend](https://github.com/HanselD/cloud-resume-challenge-frontend).

## Architecture

![Architecture](/Cloud-Resume-Backend.png)

### Details

API Gateway is the entry point for the website. A POST method allows the website to invoke the Lambda function. The Lambda updates the single item in the DynamoDB table and returns it's value. The value is then passed back to the client.