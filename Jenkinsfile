pipeline {
    agent any

    stages {
        stage('Clone GitHub Repo') {
            steps {
               git branch: 'master', url: 'https://github.com/Pythontp/toucan_analytics.git'
            }
        }

        stage('Run Django Server') {
            steps {
                sh '/usr/bin/python3 manage.py runserver 0.0.0.0:8000'
            }
        }
        stage('Run Migrations') {
            steps {
                sh 'python3 manage.py migrate'
            }
        }
        stage('SonarQube analysis') {
//    def scannerHome = tool 'SonarScanner 4.0';
        steps{
        withSonarQubeEnv('sonarqube-8.9') { 
        // If you have configured more than one global server connection, you can specify its name
//      sh "${scannerHome}/bin/sonar-scanner"
        sh "mvn sonar:sonar"
    }

    triggers {
        pollSCM('*/2 * * * *')     }
}
}
    }
}
