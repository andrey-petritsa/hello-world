#!/usr/bin/env groovy

pipeline {
    agent any
    stages {
        stage('Upgrade project') {
            steps {
                cd ./green
                git pull
                git checkout origin/main
            }
        }
        stage('Start web server') {
            steps {
                echo 'Run web server'
            }
        }
    }
}