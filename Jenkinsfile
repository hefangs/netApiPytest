pipeline {
    agent any
    stages {
        stage('testcases') {   
            steps {
                withDockerContainer('python') {
                    sh 'python -V'
                    sh 'which python'
                    sh 'pwd'
                    sh 'ls'
                    // 创建虚拟环境
                    sh 'python -m venv venv'
                    // 激活虚拟环境（Linux/Unix）
                    sh '''
                        . venv/bin/activate
                        which python
                        pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
                        pip install -r requirements.txt
                        pytest testcases
                    '''
                }
            }
        }
    }
}