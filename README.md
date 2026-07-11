# AWS Weather Pipeline

## 1. Project Overview

AWS Weather Pipeline is a serverless data collection system that retrieves real-time weather information from the OpenWeather API and stores the data in AWS cloud services for further analysis.

The main objective of this project is to automate weather data collection using AWS Lambda and store structured weather records in Amazon DynamoDB. The collected data can be transferred to Amazon S3 and analyzed using Snowflake.

---

## 2. Architecture Diagram
          OpenWeather API
                 |
                 ↓
           AWS Lambda
                 |
                 ↓
    DynamoDB (table_weather)
                 |
                 ↓
      DynamoDB Streams
                 |
                 ↓
            Amazon S3
                 |
                 ↓
          Snowflake Analytics
          
          

---

## 3. Detailed Description

This project implements a serverless weather data pipeline using AWS services.

The workflow:

1. AWS Lambda is triggered to collect weather data.
2. Lambda sends a request to the OpenWeather API.
3. Weather information is received and processed.
4. The processed data is stored in DynamoDB table `table_weather`.
5. DynamoDB Streams capture database changes.
6. Data can be stored in Amazon S3 for analytics.
7. Snowflake is used for further data analysis.

The collected weather information includes:

- City
- Country
- Temperature
- Humidity
- Pressure
- Weather condition
- Weather description
- Wind speed
- Timestamp

---

## 4. Tech Stack

### Programming Language
- Python 3.12

### Cloud Services
- AWS Lambda
- Amazon DynamoDB
- Amazon S3
- Amazon EventBridge
- DynamoDB Streams

### External API
- OpenWeather API

### Data Analytics
- Snowflake

### Development Tools
- Git
- GitHub

---

## 5. Setup and Installation

### Prerequisites

- AWS Account
- Python 3.12
- Git
- OpenWeather API Key

### Clone Repository

```bash
git clone https://github.com/rijinpv123456789-prog/aws-weather-pipeline.git



