pipeline{
    agent any 
    tools {
        maven "MAVEN3"
        jdk "oraclejdk8"
    }
    stages {
        stage('Fetch code') {
            steps {
                git branch: 'master', url: 'https://github.com/Pythontp/toucan_analytics.git'
            }
        }
    }  
}