pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                sh 'pwd'
                sh 'ls -al'
                withDockerContainer('node') {
                    sh 'node -v'
                }
            }
        }          
    }
}
