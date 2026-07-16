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
                bat 'echo %PATH%'
                bat 'where python'
                bat 'where pip'
            }
        }

        stage('Run UI tests') {
            steps {
                bat 'pytest'
            }
        }
    }
}