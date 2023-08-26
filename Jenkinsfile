#!/usr/bin/env groovy

pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                dir('repo') {
                    checkout scm
                }
            }
        }
    }
}