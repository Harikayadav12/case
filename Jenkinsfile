pipeline {
    agent any

    environment {
        KUBECONFIG = 'C:\\Users\\Harika\\.kube\\config' // path to kubeconfig on Jenkins agent
    }

    stages {

        stage('Checkout SCM') {
            steps {
                echo 'Checking out Git repository...'
                git branch: 'main', url: 'https://github.com/Harikayadav12/case.git'
            }
        }

        stage('Build') {
            steps {
                echo 'Building the application...'
                // Use Maven Wrapper
                bat '.\\mvnw clean package'
            }
        }

        stage('Test') {
            steps {
                echo 'Running unit tests...'
                bat '.\\mvnw test'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                echo 'Deploying to Kubernetes...'
                // Apply Kubernetes manifests
                bat 'kubectl apply -f deployment.yaml'
            }
        }
    }

    post {
        success {
            echo 'Pipeline finished successfully!'
        }
        failure {
            echo 'Pipeline failed. Check the logs!'
        }
    }
}
