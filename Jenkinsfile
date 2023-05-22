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
    }

    triggers {
        pollSCM('*/2 * * * *')     }
}
