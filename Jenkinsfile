pipeline {
    agent any

    environment {
        KUBE_USER = 'harikayadav'   // Your Kubernetes username
        KUBE_CONFIG = 'C:\\Users\\Harika\\.kube\\config' // Path to kubeconfig
    }

    stages {
        stage('Checkout SCM') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Building the application...'

                // Use Maven wrapper if available, else ensure Maven is installed on Jenkins
                bat '.\\mvnw clean package || mvn clean package'
            }
        }

        stage('Test') {
            steps {
                echo 'Testing the application...'
                // Add test commands if any
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                echo 'Deploying to Kubernetes...'
                
                // Set KUBECONFIG path for kubectl
                withEnv(["KUBECONFIG=${env.KUBE_CONFIG}"]) {
                    bat "kubectl apply -f deployment.yaml --validate=false"
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished!'
        }
        failure {
            echo 'Pipeline failed. Check the logs!'
        }
        success {
            echo 'Pipeline succeeded!'
        }
    }
}
