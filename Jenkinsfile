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
        
        stage('Send Allure Report via Email') {
            steps {
                // 禁用默认的 ENTRYPOINT
                withDockerContainer(image: 'namshi/smtp', args: '--entrypoint=\'\'') { 
                    sh '''
                        # 创建邮件内容
                        cat <<EOF > email.txt
                        Subject: Jenkins Job - Allure Report-\${env.BUILD_NUMBER}
                        To: he529564582@163.com
                        From: he529564582@163.com
                        MIME-Version: 1.0
                        Content-Type: multipart/mixed; boundary="boundary-text"

                        --boundary-text
                        Content-Type: text/plain

                        Please find attached the Allure report for build \${env.BUILD_NUMBER}.
                        --boundary-text
                        Content-Type: text/html; name="index.html"
                        Content-Disposition: attachment; filename="index.html"

                        --boundary-text--
                        EOF

                        # 将 index.html 文件内容追加到 email.txt
                        cat ./allure-report/index.html >> email.txt

                        # 发送邮件
                        cat email.txt | exim -C -
                    '''
                }
            }
        }

    } 
}
