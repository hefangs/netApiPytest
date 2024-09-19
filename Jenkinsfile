pipeline {
    agent any
    stages {
        stage('Pytest Testcases') {   
            steps {
                withDockerContainer('python') {
                    sh 'python -V'
                    sh 'which python'
                    sh 'pwd'
                    sh 'ls'
                    // 创建虚拟环境
                    sh '''
                        python -m venv venv
                        . venv/bin/activate
                        which python
                        pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
                        pip install -r requirements.txt
                        pytest testcases/test_search/test_search.py::TestSearch::test_search
                    '''
                }
            }
        } 

        stage('Generate Allure Report') {
            steps {
                withDockerContainer('frankescobar/allure-docker-service') {
                    sh 'allure --version'
                    sh 'allure generate ./temp -o ./allure-report --clean'
                }
            }
        } 
    }
    post {
        success {
            // 构建成功时执行
            mail to: 'he529564582@163.com',
                 subject: "${env.JOB_NAME}-第${env.BUILD_NUMBER}构建成功",
                 body: 
                    """
                        项目名称: ${env.JOB_NAME}
                        构建状态: 成功
                        构建编号: 第${env.BUILD_NUMBER}次构建
                        构建URL: ${env.BUILD_URL}
                        最近提交: ${GIT_REVISION}
                    """
        }
    }
}