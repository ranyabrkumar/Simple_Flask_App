pipeline {
    agent { label 'agent1' }

    environment {
        VENV = 'venv'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/ranyabrkumar/Simple_Flask_App.git'
            }
        }
        stage('Build') {
            steps {
                sh 'python3 -m venv $VENV'
                sh './venv/bin/pip install -r requirements.txt'
            }
        }
        
        stage('Deploy') {
            // when {
            //     branch 'main'
            // }
            steps {
                sh 'echo "Deploying to staging..."'
                sh './venv/bin/python app.py &'
                  sh 'sleep 5' // Wait for the app to start
                
            }
        }
        stage('Test') {
            steps {
                sh 'ls -l test/'
                sh 'nohup ./venv/bin/pytest test/test-app.py &' || true
            }
        }
    }
    post {
        success {
            mail to: 'ranyabrkumar@gmail.com',
                 subject: "SUCCESS: Jenkins Build #${env.BUILD_NUMBER}",
                 body: "Build succeeded!"
        }
        failure {
            mail to: 'ranyabrkumar@gmail.com',
                 subject: "FAILURE: Jenkins Build #${env.BUILD_NUMBER}",
                 body: "Build failed!"
        }
    }
}
