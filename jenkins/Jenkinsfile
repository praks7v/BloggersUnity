pipeline {
    agent any
    
    environment {
        SCANNER_HOME= tool 'sonar-scanner'
    }

    stages {
        stage('Git Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/praks7v/BloggersUnity.git'
            }
        }
        
        stage('OWASP Scan') {
            steps {
                dependencyCheck additionalArguments: '--scan ./' , odcInstallation: 'DC'
                    dependencyCheckPublisher pattern: '**/dependency-check-report.xml'
            }
        }
        
        stage('Trivy Scan') {
            steps {
                sh "trivy fs ."
            }
        }
        
        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('sonar') {
                    sh "$SCANNER_HOME/bin/sonar-scanner -Dsonar.projectName=BologgersUnity -Dsonar.projectKey=BologgersUnity"
    
                }
            }
        }
        
        stage('Build Image') {
            steps {
                sh "make image"
            }
        }
        
        stage('Docker Push') {
            steps {
                script {
                    withDockerRegistry(url: 'http://localhost:5000'){
                        sh "make push"
                    }
                }
            }
        }
        
        stage('Docker Deploy') {
            steps {
                script {
                    withDockerRegistry(url: 'http://localhost:5000') {
                        sh "docker images"
                        sh "docker run -d --rm -it -p 8000:8000 localhost:5000/bloggersunity-web:latest"
                    }
                }
            }
        }
    }
}
