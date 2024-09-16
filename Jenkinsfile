pipeline {
    agent any
    stages {
        stage('Check') {   
            steps {
                withDockerContainer('python') {
                    sh 'python -v'
                    sh 'pip -v'
                }
            }
        }
    }
}
