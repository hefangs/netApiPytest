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
                 subject: "构建成功: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                 body: """
                        <!DOCTYPE html>
                        <html>
                        <head>
                            <meta charset="UTF-8">
                            <title>构建成功 - ${env.JOB_NAME} #${env.BUILD_NUMBER}</title>
                        </head>
                        <body>
                            <p>项目名称 ： ${env.JOB_NAME}</p>
                            <p>构建编号 ： 第${env.BUILD_NUMBER}次构建</p>
                            <p>构建状态： 成功</p>
                            <p>构建URL： <a href="${env.BUILD_URL}">${env.BUILD_URL}</a></p>
                        </body>
                        </html>
                        """,
                 mimeType: 'text/html'
        }
    }
}