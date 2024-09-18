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
                withCredentials([usernamePassword(credentialsId: '814aa18c-a7e2-4b58-a7c4-43bf63423be8', usernameVariable: 'SMTP_USERNAME', passwordVariable: 'SMTP_PASSWORD')]) {
                    withDockerContainer('mailhog/mhsendmail') {
                        withEnv([
                            "SMTP_HOST=smtp.163.com",
                            "SMTP_PORT=465",
                            "FROM_ADDRESS=he529564582@163.com",
                            "TO_ADDRESS=he529564582@163.com",
                            "SUBJECT=Allure Report"
                        ]) {
                            sh '''
                                # 压缩Allure报告
                                tar -czf allure-report.tar.gz -C ./allure-report .
                                # 发送邮件
                                mhsendmail -subject="${SUBJECT}" -from="${FROM_ADDRESS}" -to="${TO_ADDRESS}" -auth-plain="${SMTP_USERNAME}:${SMTP_PASSWORD}" -host="${SMTP_HOST}" -port="${SMTP_PORT}" -starttls=false -insecure-skip-verify=true -attach="allure-report.tar.gz" <<EOF
                                Please find attached the Allure report.
                                EOF
                            '''
                        }
                    }
                }
            }
        }
    }
}
