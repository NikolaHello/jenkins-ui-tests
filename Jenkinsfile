pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Tests') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'jenkins-login',
                        usernameVariable: 'JENKINS_USER',
                        passwordVariable: 'JENKINS_PASSWORD'
                    )
                ]) {
                    bat 'python -m pytest tests -v'
                }
            }
        }
    }
}