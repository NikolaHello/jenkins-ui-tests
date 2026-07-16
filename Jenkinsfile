pipeline {
    agent any
    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run UI tests') {
            steps {
                bat 'pytest -v'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: '**/*.log', allowEmptyArchive: true
        }
        success {
            echo 'Tests passed'
        }
        failure {
            echo 'Tests failed'
        }
    }
}