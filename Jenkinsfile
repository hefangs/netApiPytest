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

        // stage('Send Allure Report via Email') {
        //     steps {
        //         withDockerContainer('openjdk:8-jdk-alpine') {
        //             sh '''
        //                 echo "Subject: Allure Report" > email.txt
        //                 echo "Please find the Allure report attached." >> email.txt
        //                 echo "" >> email.txt
        //                 tar -czf allure-report.tar.gz ./allure-report
        //                 apk add --no-cache bash
        //                 apk add --no-cache ssmtp
        //                 cat email.txt | ssmtp -v he529564582@163.com -s smtp.163.com -p 465 -U your-email@163.com -P hf15000840699 -f your-email@163.com
        //                 ssmtp -v he529564582@163.com -s smtp.163.com -p 465 -U your-email@163.com -P hf15000840699 -f your-email@163.com < email.txt -A allure-report.tar.gz
        //             '''
        //         }
        //     }
        // }
    }
}
