pipeline {
    agent any

    environment {
        KUBE_USER = 'harikayadav'  // Kubernetes user
        KUBE_CONFIG = 'C:\\Users\\harikayadav\\.kube\\config' // Path to kubeconfig
    }

    stages {
        stage('Checkout SCM') {
            steps {
                echo 'Checking out Git repository...'
                git branch: 'main', url: 'https://github.com/Harikayadav12/case.git'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                echo 'Deploying to Kubernetes...'
                withEnv(["KUBECONFIG=${env.KUBE_CONFIG}"]) {
                    // Apply your deployment YAML
                    bat 'kubectl apply -f deployment.yaml'
                    bat 'kubectl get pods'
                }
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
