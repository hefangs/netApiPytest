pipeline {
    agent any
    stages {
        stage('Install python') {   
            steps {
                withDockerContainer('python') {
                    sh 'python -v'
                }
            }
        }
        stage('Create Venv') {   
            steps {
                sh 'pwd'
                sh 'ls'
            }
        }
    }
}
