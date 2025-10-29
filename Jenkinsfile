pipeline {
    agent any

    stages {

        stage('Build Docker Image') {
            steps {
                echo "Building Docker Image..."
                bat "docker build -t harikayadav/currencyconverter:v1 ."
            }
        }

        stage('Docker Login') {
            steps {
                echo "Logging in to Docker Hub..."
                bat 'docker login -u harikayadav -p 22251a1245'
            }
        }

        stage('Push Docker Image to Docker Hub') {
            steps {
                echo "Pushing Docker Image to Docker Hub..."
                bat "docker tag harikayadav/currencyconverter:v1 harikayadav/currencyconverter:latest"
                bat "docker push harikayadav/currencyconverter:latest"
            }
        }

        stage('Deploy to Kubernetes') {
            steps { // ✅ Add this block
                echo 'Deploying to Kubernetes...'
                withEnv(["KUBECONFIG=C:\\ProgramData\\Jenkins\\.kube\\config"]) {
                    bat 'kubectl apply -f deployment.yaml --validate=false'
                }
            }
        }

    }

    post {
        success {
            echo '✅ Deployment Successful!'
        }
        failure {
            echo '❌ Deployment Failed!'
        }
    }
}

