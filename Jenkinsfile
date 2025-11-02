pipeline {
    agent any

    environment {
        IMAGE_NAME = "ci-anomaly-detector2"
        CONTAINER_NAME = "ci-anomaly-detector2-container"
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/harshareddy337/ci-anomaly-detector2.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t ci-anomaly-detector2 .'
            }
        }

        stage('Run Docker Container') {
    steps {
        // Stop and remove old container (by name, directly)
        bat '''
        docker stop ci-anomaly-detector2-container || echo "No existing container to stop"
        docker rm ci-anomaly-detector2-container || echo "No existing container to remove"
        '''

        // Run fresh container
        bat 'docker run -d -p 5000:5000 --name ci-anomaly-detector2-container ci-anomaly-detector2'
    }
}

    }

    post {
        success {
            echo "✅ Build & Deployment successful! Visit http://localhost:5000"
        }
        failure {
            echo "❌ Pipeline failed!"
        }
    }
}
