pipeline {
    agent any
    stages {
        stage('Install Python') {   
            steps {
                withDockerContainer('python') {
                    sh 'python -version'
                }
            }
        }
        stage('Create Venv') {   
            steps {
                sh 'pwd'
                sh 'ls'
            }
        }
        stage('Install Dependencies') {   
            steps {
                sh 'pwd'
                sh 'ls'
                // sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {   
            steps {
                sh 'pwd'
                sh 'ls'
                // sh 'pytest testcases'
            }
        }
    }
}
