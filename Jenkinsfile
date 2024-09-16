pipeline {
    agent any
    stages {
        stage('Install Python') {   
            steps {
                withDockerContainer('python') {
                    sh 'python -V'
                    sh 'pwd'
                    sh 'ls'
                    // 创建虚拟环境
                    sh 'python -m venv venv'
                    // 激活虚拟环境（Linux/Unix）
                    sh '. venv/bin/activate'
                    // 验证虚拟环境是否已激活
                    sh 'which python'
                    // Install Dependencies
                    sh 'pip install -r requirements.txt'
                }
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
