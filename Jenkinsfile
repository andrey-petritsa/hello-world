#!/usr/bin/env groovy

pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Update dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run webserver') {
             steps {
                 sh 'sudo nohup python main.py > log.txt 2>&1 &'
             }
        }
    }
  }