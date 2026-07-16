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
                // Используем абсолютный путь к cmd.exe и python.exe
                bat 'C:\\Windows\\System32\\cmd.exe /c C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python313\\python.exe -m pip install --upgrade pip'
                bat 'C:\\Windows\\System32\\cmd.exe /c C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python313\\python.exe -m pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                bat 'C:\\Windows\\System32\\cmd.exe /c C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python313\\python.exe -m pytest tests/ -v --tb=short'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'screenshots/*.png', allowEmptyArchive: true
        }
    }
}