pipeline {pipeline {
    agent any

    environment {
        // Path to your kubeconfig for kubectl
        KUBECONFIG = "C:\\Users\\harikayadav\\.kube\\config"
    }

    stages {

        stage('Build') {
            steps {
                echo 'Building the application...'
                // Example: if using Maven
                bat 'mvn clean package'
            }
        }

        stage('Test') {
            steps {
                echo 'Running unit tests...'
                // Example: run test command
                bat 'mvn test'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                echo 'Deploying to Kubernetes...'
                // Make sure deployment.yaml is in workspace
                bat 'kubectl apply -f deployment.yaml --validate=false'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check the logs!'
        }
    }
}


