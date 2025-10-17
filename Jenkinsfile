pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/Fardaad-Khan/travel-app.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t travel-app-backend .'
            }
        }

        stage('Run Container') {
            steps {
                bat '''
                docker stop travel-app-backend || true
                docker rm travel-app-backend || true
                docker run -d -p 5000:5000 --name travel-app-backend travel-app-backend
                '''
            }
        }
    }

    post {
        success { echo '✅ Build & Deployment Successful!' }
        failure { echo '❌ Build Failed!' }
    }
}
