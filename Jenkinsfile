pipeline {
    agent any

    environment {
        IMAGE_NAME = "ci-anomaly-detector2"
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/harshareddy337/ci-anomaly-detector2.git'

            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${IMAGE_NAME}")
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    sh 'docker ps -q --filter "name=ci-anomaly-detector2" | grep -q . && docker stop ci-anomaly-detector2 || true'
                    sh 'docker run -d -p 5000:5000 --name ci-anomaly-detector2 ci-anomaly-detector2'
                }
            }
        }
    }

    post {
        success {
            echo "✅ Build & Deployment successful!"
        }
        failure {
            echo "❌ Pipeline failed!"
        }
    }
}
