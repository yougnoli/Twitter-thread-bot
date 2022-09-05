# Twitter-thread-bot

This is a beginner and learning project to build a reliable data storage architecture and program execution for writing Twitter threads.

## Tools
- Azure Data Factory
- tSQL
- Python
- Azure Function

## Prerequisites
- Azure Account
- beginner tSQL
- intermediate Python
- Twitter API

## Problem Encountered
Need to create a program that can automate the posting of a thread on Twitter. The program searches for the tweet from an Azure SQL Database and will be posted based on the previously set publication date. The program, inserted on an Azure Function, will run at a certain preset time. The user only has to worry about uploading tweets to a csv: the program will take care of publishing daily.

## Data Storage Architecture
- file .txt that contains the information to be stored in a sql azure database. It is located in a Blob Storage.
- the file has 2 columns: id and json. The json column accepts a json, which contains all the information of the daily tweet to be posted.
- schema of the json
  - id
  - json
  - insertion date
  - publication date
  - module
  - page
  - topic
  - first tweet
  - long tweet
- through Azure Data Factory the file is read and only the json column loaded on the Azure SQL Database
- the table in Azure SQL consists of 2 fields: id and json. There are calculated fields that unpack the json

## Python Program
- log in on Twitter
- capture first tweet and long tweet of a given day from the Azure SQL Database and divide it into n tweets (which must be each other's reply in order to be a thread)
- publish on Twitter

## Azure Function
- load the program into an Azure Function timer trigger
