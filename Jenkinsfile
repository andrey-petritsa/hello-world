#!/usr/bin/env groovy

pipeline {
    agent any
    stages {
        stage('Upgrade project') {
            steps {
                checkout scm
            }
        }
        stage('Start web server') {
            steps {
                echo 'Run web server'
            }
        }
    }
}