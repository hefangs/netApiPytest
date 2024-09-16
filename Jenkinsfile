pipeline {
    agent any
    stages {
        stage('Install Python') {   
            steps {
                withDockerContainer('python') {
                    sh 'python -V'
                }
            }
        }
        stage('Create Venv') {   
            steps {
                sh 'pwd'
                sh 'ls'
                sh 'which python'
                // 创建虚拟环境
                sh 'python -m venv venv'
                
                // 激活虚拟环境（Linux/Unix）
                sh '. venv/bin/activate'
                
                // 验证虚拟环境是否已激活
                sh 'which python'
            }
        }
        stage('Install Dependencies') {   
            steps {
                sh 'pwd'
                sh 'ls'
                // 打印当前环境信息
                sh '''
                echo "Checking environment..."
                
                # 打印当前 Python 解释器的路径
                which python

                # 打印 Python 版本
                python -V

                # 打印 pip 版本
                pip -V

                # 检查是否在虚拟环境中
                if [ -z "$VIRTUAL_ENV" ]; then
                    echo "Not in a virtual environment."
                else
                    echo "In a virtual environment: $VIRTUAL_ENV"
                fi
                '''
                        sh 'pip install -r requirements.txt'
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
