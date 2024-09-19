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
                 subject: "${env.JOB_NAME} - 第${env.BUILD_NUMBER}次构建成功",
                 body: """
                            <!DOCTYPE html>    
                            <html>    
                            <head>    
                            <meta charset="UTF-8">    
                            <title>${env.JOB_NAME} - 第${env.BUILD_NUMBER}次构建日志</title>    
                            </head>    
                                
                            <body leftmargin="8" marginwidth="0" topmargin="8" marginheight="4"    
                                offset="0">    
                                <table width="95%" cellpadding="0" cellspacing="0"  style="font-size: 11pt; font-family: Tahoma, Arial, Helvetica, sans-serif">    
                                    <tr>    
                                        本邮件由系统自动发出，无需回复！<br/>            
                                        大家好，以下为 ${env.JOB_NAME} 项目构建信息</br> 
                                        <td><font color="#CC0000">构建结果 - 成功</font></td>   
                                    </tr>    
                                    <tr>    
                                        <td><br />    
                                        <b><font color="#0B610B">构建信息</font></b>    
                                        <hr size="2" width="100%" align="center" /></td>    
                                    </tr>    
                                    <tr>    
                                        <td>    
                                            <ul>    
                                                <li>项目名称: ${env.JOB_NAME}</li>    
                                                <li>构建编号: 第${env.BUILD_NUMBER}次构建</li>    
                                                <li>触发原因: ${env.CAUSE}</li>    
                                                <li>构建状态: 成功</li>    
                                                <li>构建日志: <a href="${env.BUILD_URL}console">${env.BUILD_URL}console</a></li>    
                                                <li>构建URL: <a href="${env.BUILD_URL}">${env.BUILD_URL}</a></li>    
                                                <li>测试报告: <a href="${env.JOB_URL}allure-report">${env.JOB_URL}allure-report</a></li>    
                                            </ul>    

                                <h4><font color="#0B610B">失败用例</font></h4>
                                <hr size="2" width="100%" />
                                ${FAILED_TESTS}<br/>

                                <h4><font color="#0B610B">最近提交(#${env.GIT_REVISION})</font></h4>
                                <hr size="2" width="100%" />
                                <ul>
                                ${CHANGES_SINCE_LAST_SUCCESS, reverse=true, format="%c", changesFormat="<li>%d [%a] %m</li>"}
                                </ul>
                                详细提交: <a href="${env.JOB_URL}changes">${env.JOB_URL}changes</a><br/>

                                        </td>    
                                    </tr>    
                                </table>    
                            </body>    
                            </html>
                        """
        }
    }
}
