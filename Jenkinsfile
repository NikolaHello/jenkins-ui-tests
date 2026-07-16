pipeline {
    agent any

    environment {
        JENKINS_URL = "http://localhost:8080"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup') {
            steps {
                bat 'C:\\Windows\\System32\\cmd.exe /c C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python313\\python.exe -m pip install --upgrade pip'
                bat 'C:\\Windows\\System32\\cmd.exe /c C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python313\\python.exe -m pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {

                withCredentials([
                    usernamePassword(
                        credentialsId: 'jenkins-login',
                        usernameVariable: 'JENKINS_USER',
                        passwordVariable: 'JENKINS_PASSWORD'
                    )
                ]) {
                bat 'C:\\Windows\\System32\\cmd.exe /c C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python313\\python.exe -m pytest tests/ -v --tb=short'
            }
        }
    }
}