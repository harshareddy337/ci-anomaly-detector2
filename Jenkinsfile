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
                // Stop any running container with the same name
                bat '''
                docker ps -q --filter "name=ci-anomaly-detector2-container" > tmp.txt
                for /f %%i in (tmp.txt) do docker stop %%i
                del tmp.txt
                '''

                // Run a fresh container
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
