pipeline {
    agent any
    stages {
        stage('demo') {   
            steps {
                withDockerContainer('python') {
                    sh 'python -V'
                    sh 'which python'
                    sh 'pwd'
                    sh 'ls'
                    // 创建虚拟环境
                    sh 'python -m venv venv'
                    // 激活虚拟环境（Linux/Unix）
                    sh '. venv/bin/activate'
                    // 验证虚拟环境是否已激活
                    sh 'which python'
                    // 设置 pip 镜像源为清华大学
                    sh 'pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple'
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
