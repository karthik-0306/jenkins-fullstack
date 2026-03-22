pipeline {
    agent any
    environment {
        // Task 5.3: Tagging format requirements [cite: 115]
        DOCKER_HUB_USER = '2023bcs0159karthik' 
        REG_ROLL = '2023bcs0159' 
    }
    stages {
        stage('Checkout') {
            steps {
                // Task 5.1: Checkout from GitHub [cite: 111]
                checkout scm
            }
        }
        stage('Build Frontend & Backend') {
            steps {
                script {
                    // Task 5.2: Build Docker images [cite: 112]
                    // Task 5.3: Apply specific tagging format [cite: 115]
                    sh "docker build -t ${DOCKER_HUB_USER}/${REG_ROLL}_frontend ./frontend"
                    sh "docker build -t ${DOCKER_HUB_USER}/${REG_ROLL}_backend ./backend"
                }
            }
        }
        stage('Push to Docker Hub') {
            steps {
                // Task 5.4: Push to Docker Hub [cite: 116]
                withCredentials([string(credentialsId: 'docker-hub-token', variable: 'DOCKER_HUB_TOKEN')]) {
                    sh "echo \$DOCKER_HUB_TOKEN | docker login -u ${DOCKER_HUB_USER} --password-stdin"
                    sh "docker push ${DOCKER_HUB_USER}/${REG_ROLL}_frontend"
                    sh "docker push ${DOCKER_HUB_USER}/${REG_ROLL}_backend"
                }
            }
        }
    }
}