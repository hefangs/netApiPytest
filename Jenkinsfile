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
                        pytest testcases || true
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
                withDockerContainer('namshi/smtp') {
                    sh '''
                        echo "Subject: Jenkins Job - Allure Report-${env.BUILD_NUMBER}" > email.txt
                        echo "To: he529564582@163.com" >> email.txt
                        echo "From: he529564582@163.com" >> email.txt
                        echo "MIME-Version: 1.0" >> email.txt
                        echo "Content-Type: multipart/mixed; boundary=\\"boundary-text\\"" >> email.txt
                        echo "" >> email.txt
                        echo "--boundary-text" >> email.txt
                        echo "Content-Type: text/plain" >> email.txt
                        echo "" >> email.txt
                        echo "Please find attached the Allure report for build ${env.BUILD_NUMBER}." >> email.txt
                        echo "--boundary-text" >> email.txt
                        echo "Content-Type: text/html; name=\\"index.html\\"" >> email.txt
                        echo "Content-Disposition: attachment; filename=\\"index.html\\"" >> email.txt
                        echo "" >> email.txt
                        cat ./allure-report/index.html >> email.txt
                        echo "--boundary-text--" >> email.txt

                        cat email.txt | sendmail -t
                    '''
                }
            }
        }

    } 
}
