pipeline {
    agent any
    stages {
        stage('pytest testcases') {   
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
                        pytest testcases || true
                    '''
                }
            }
        stage('Generate Allure Report') {
            steps {
                withDockerContainer('frankescobar/allure-docker-service') {
                    sh 'allure --version'
                    sh 'allure generate ./temp -o ./allure-report'
                }
            }
        }
//         stage('Send Allure Report via Email') {
//             steps {
//                 mail to: 'he529564582@163.com',
//                      subject: "Jenkins Job - Allure Report-${env.BUILD_NUMBER}",
//                      body: "Please find attached the Allure report for build ${env.BUILD_NUMBER}.",
//                      attachments: 'allure-report/index.html',
//                      mimeType: 'text/html'
//                 }
//             }
        }
    }
}
