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
            echo 'Build succeeded! Sending success email...'
            // 发送成功邮件
            withDockerContainer('jess/mutt') {
                sh '''
                    tar -cvf allure-report.tar ./allure-report
                    echo "构建成功！请查收附件中的 Allure 测试报告，构建编号 #${env.BUILD_NUMBER}。" | mutt \
                    -s "Allure 测试报告 - 构建 #${env.BUILD_NUMBER} 成功" \
                    -a allure-report.tar \
                    -- he529564582@163.com
                '''
            }
        }
        failure {
            echo 'Build failed! Sending failure email...'
            // 发送失败邮件
            withDockerContainer('jess/mutt') {
                sh '''
                    echo "构建失败，请尽快查看构建日志，构建编号 #${env.BUILD_NUMBER}。" | mutt \
                    -s "Allure 测试报告 - 构建 #${env.BUILD_NUMBER} 失败" \
                    -- he529564582@163.com
                '''
            }
        }
        always {
            echo 'Build completed. Cleaning up...'
            // 无论构建是否成功，都会执行
        }
    }
}