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

       stage('Send Allure Report via Email') {
            steps {
                script {
                    // 使用 docker-mailserver 镜像
                    withDockerContainer('mailserver/docker-mailserver:latest') {
                        withCredentials([usernamePassword(credentialsId: '2c6be544-a0eb-493e-89a4-6fe5443c1eae',
                                                            usernameVariable: 'SMTP_USER',
                                                            passwordVariable: 'SMTP_PASS')]) {
                            sh '''
                                # 发送邮件
                                echo "Subject: Allure Report\nPlease find the attached Allure report." | \
                                mailx -s "Allure Report" -a allure-report.tar.gz -r "$SMTP_USER" -S smtp="smtp://smtp.163.com:587" -S smtp-auth=login -S smtp-auth-user="$SMTP_USER" -S smtp-auth-password="$SMTP_PASS" he529564582@163.com
                            '''
                        }   
                    }
                }
            }
        }
    }
}