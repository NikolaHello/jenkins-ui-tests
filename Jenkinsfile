pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Debug') {
            steps {
                powershell '& "C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" --version'
            }
        }

        stage('Setup') {
            steps {
                powershell '& "C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m pip install --upgrade pip'
                powershell '& "C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                powershell '& "C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m pytest tests/ -v --tb=short'
            }
        }
    }
}