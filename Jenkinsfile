pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                // Clone main branch from your GitHub repo
                git branch: 'main', url: 'https://github.com/Fardaad-Khan/travel-app.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                // Install all Python dependencies
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Build Docker Image') {
            steps {
                // Build a new Docker image for the Flask app
                sh 'docker build -t travel-app-backend .'
            }
        }

        stage('Run Container') {
            steps {
                // Stop and recreate container for deployment
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
