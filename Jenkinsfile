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
                bat 'python --version'
                bat 'pip --version'
                bat 'dir'
            }
        }

        stage('Install') {
            steps {
                bat 'pip install pytest selenium webdriver-manager python-dotenv allure-pytest'
            }
        }

        stage('Test') {
            steps {
                bat 'pytest tests/ -v'
            }
        }
    }
}