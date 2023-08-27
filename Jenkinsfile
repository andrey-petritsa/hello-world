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
                sh 'kill -9 $(lsof -t -i:5000)'
                 sh 'JENKINS_NODE_COOKIE=dontKillMe python main.py &'
             }
        }
    }
  }