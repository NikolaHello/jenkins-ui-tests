pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup') {
            steps {
                // Ваш путь к Python
                bat 'C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python313\\python.exe -m pip install --upgrade pip'
                bat 'C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python313\\python.exe -m pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                bat 'C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python313\\python.exe -m pytest tests/ -v --tb=short'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'screenshots/*.png', allowEmptyArchive: true
        }
    }
}