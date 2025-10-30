pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                echo "Building Docker Image..."
                bat 'docker build -t harikayadav/currencyconverter:latest .'
            }
        }

        stage('Docker Login') {
            steps {
                echo "Logging into Docker Hub..."
                bat 'docker login -u harikayadav -p 22251a1245'
            }
        }

        stage('Push Docker Image') {
            steps {
                echo "Pushing image to Docker Hub..."
                bat 'docker push harikayadav/currencyconverter:latest'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                echo "Deploying to Kubernetes..."
                bat 'kubectl apply -f deployment.yaml --validate=false'
                bat 'kubectl apply -f service.yaml'
            }
        }
    }

    post {
        success {
            echo "✅ Library Management System successfully deployed!"
        }
        failure {
            echo "❌ Pipeline failed. Check Jenkins logs."
        }
    }
}

