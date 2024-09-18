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
                // 将 allure-report 目录压缩为 tar 文件
                sh 'tar -cvf allure-report.tar ./allure-report'
                
                // 使用 jess/mutt 发送邮件
                withDockerContainer('jess/mutt') {
                    // 创建 .muttrc 配置文件
                    sh '''
                        echo 'set smtp_url = "smtp://he529564582@163.com:hf15000840699@smtp.163.com:587/"' > /root/.muttrc
                        echo "请查收附件中的 Allure 测试报告，构建编号 #${env.BUILD_NUMBER}。" | mutt \
                        -s "Allure 测试报告 - 构建 #${env.BUILD_NUMBER}" \
                        -a allure-report.tar \
                        -- he529564582@163.com
                    '''
                }
            }
        }
    }
}