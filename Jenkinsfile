pipeline {
    agent any

    stages {
        stage('stage 1') {
            steps {
                sh 'pwd'
                sh 'ls -al'
                // 该步骤通常不应该在您的脚本中使用。请参考帮助查看详情。
                withDockerContainer('node') {
                    sh 'node -v'
                }
            }
        }          
    }
}
