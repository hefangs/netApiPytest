pipeline {
    agent any
    stages {
        stage('Clean Workspace') {
            steps {
                script {
                    // 清理工作目录
                    sh 'rm -rf *'
                }
            }
        }
        stage('Test Testcases') {
            agent {
                docker { image 'python' }
            }
            steps('python') {
                sh 'pwd'
                sh 'ls'
                // 创建虚拟环境
                sh '''
                    python -m venv venv
                    . venv/bin/activate
                    which python
                    pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
                    pip install -r requirements.txt
                    rm -rf logs/*
                    pytest testcases/test_playlist/test_playlist.py::TestPlayList::test_user_playlist  || true
                    pwd
                    ls -al
                '''
            }
        }
        stage('Generate Allure Report') {
            agent {
                docker { image 'frankescobar/allure-docker-service' }
            }
            steps('Allure') {
                sh 'allure --version'
                sh 'allure generate ./temp -o ./allure-report --clean'
            }
        } 
    }


    post {
        success{
            mail to: 'he529564582@163.com',
                subject: "构建成功: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: """
                        <!DOCTYPE html>
                        <html>
                            <head>
                                <meta charset="UTF-8">
                                <title>构建成功 - ${env.JOB_NAME} #${env.BUILD_NUMBER}</title>
                            </head>
                            <body>
                                <table width="95%" cellpadding="0" cellspacing="0"  style="font-size: 11pt; font-family: Tahoma, Arial, Helvetica, sans-serif">    
                                    <tr>    
                                        本邮件由系统自动发出，无需回复！<br/>            
                                        大家好，以下为 ${env.JOB_NAME } 项目构建信息</br> 
                                        <td><font color="#CC0000">构建结果 - ${currentBuild.result}</font></td>   
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
                                                <li>构建编号: 第 ${BUILD_NUMBER} 次构建</li>            
                                                <li>构建URL: <a href="${BUILD_URL}">${BUILD_URL}</a></li>
                                                <li>测试报告:<a href="${BUILD_URL}execution/node/23/ws/allure-report/index.html">${BUILD_URL}allure</a></li>
                                                <li>构建日志:<a href="${BUILD_URL}console">${BUILD_URL}console</a></li>
                                                <li>最近提交: <a href="${BUILD_URL}changes">${BUILD_URL}changes</a</li>  
                                            </ul>    
                                        </td>    
                                    </tr>    
                                </table>  
                            </body>
                        </html>
                        """,
                mimeType: 'text/html'
        }
        
        failure {
            mail to: 'he529564582@163.com',
                subject: "构建失败: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: """
                        <!DOCTYPE html>
                        <html>
                            <head>
                                <meta charset="UTF-8">
                                <title>构建失败 - ${env.JOB_NAME} #${env.BUILD_NUMBER}</title>
                            </head>
                            <body>
                                <table width="95%" cellpadding="0" cellspacing="0"  style="font-size: 11pt; font-family: Tahoma, Arial, Helvetica, sans-serif">    
                                    <tr>    
                                        本邮件由系统自动发出，无需回复！<br/>            
                                        大家好，以下为 ${env.JOB_NAME } 项目构建信息</br> 
                                        <td><font color="#CC0000">构建结果 -  ${currentBuild.result}</font></td> 
                                    </tr>    
                                    <tr>    
                                        <td><br />    
                                        <b><font color="#B40404">构建信息</font></b>    
                                        <hr size="2" width="100%" align="center" /></td>    
                                    </tr>    
                                    <tr>    
                                        <td>    
                                            <ul>    
                                                <li>项目名称: ${env.JOB_NAME}</li>    
                                                <li>构建编号: 第 ${env.BUILD_NUMBER} 次构建</li>            
                                                <li>构建URL: <a href="${env.BUILD_URL}">${env.BUILD_URL}</a></li>
                                                <li>构建日志： <a href="${env.BUILD_URL}console">${env.BUILD_URL}console</a></li>
                                                <li>最近提交: <a href="${env.BUILD_URL}changes">${env.BUILD_URL}changes</a></li>  
                                            </ul>    
                                        </td>    
                                    </tr>    
                                </table>  
                            </body>
                        </html>
                    """,
                mimeType: 'text/html'
        }
    }
}