pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/Fardaad-Khan/travel-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t travel-app-backend .'
            }
        }

        stage('Run Container') {
            steps {
                sh '''
                docker stop travel-app-backend || true
                docker rm travel-app-backend || true
                docker run -d -p 5000:5000 --name travel-app-backend travel-app-backend
                '''
            }
        }
    }

    post {
        success {
            echo '✅ Build & Deployment Successful!'
        }
        failure {
            echo '❌ Build Failed!'
        }
    }
}
