pipeline {
    agent any
    stages {
        stage('Check Python and Pip') {   // 检查 Python 和 Pip 是否存在
            steps {
                sh 'python --version || python3 --version'  // 检查 Python 版本
                sh 'pip --version || pip3 --version'        // 检查 Pip 版本
            }
        }
    }
}
