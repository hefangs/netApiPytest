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
                withDockerContainer('alpine:3.12') {
                    script {
                        withCredentials([usernamePassword(credentialsId: '2c6be544-a0eb-493e-89a4-6fe5443c1eae', 
                                                        usernameVariable: 'SMTP_USER', 
                                                        passwordVariable: 'SMTP_PASS')]) {
                            sh '''
                                # 使用清华大学的镜像源
                                echo "http://mirrors.tuna.tsinghua.edu.cn/alpine/v3.12/main" > /etc/apk/repositories
                                echo "http://mirrors.tuna.tsinghua.edu.cn/alpine/v3.12/community" >> /etc/apk/repositories

                                # 创建邮件正文
                                echo "Subject: Allure Report" > email.txt
                                echo "Please find the attached Allure report." >> email.txt

                                # 打包报告
                                tar -czf allure-report.tar.gz ./allure-report

                                # 安装 mutt、SSL证书和 SASL库
                                apk add --no-cache mutt bash ca-certificates cyrus-sasl
                                update-ca-certificates

                                # 配置 mutt
                                echo "set smtp_url=\"smtps://$SMTP_USER@smtp.163.com:465/\"" > ~/.muttrc
                                echo "set smtp_pass=\"$SMTP_PASS\"" >> ~/.muttrc
                                echo "set smtp_authenticators=\"login\"" >> ~/.muttrc
                                echo "set ssl_force_tls=yes" >> ~/.muttrc

                                # 发送带附件的邮件
                                echo "Sending email with attachment..."
                                mutt -s "Allure Report" -a allure-report.tar.gz -- he529564582@163.com < email.txt
                            '''
                        }
                    }
                }
            }
        }
    }
}