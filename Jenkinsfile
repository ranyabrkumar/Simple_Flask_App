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
                sh 'python3 -m venv ${VENV}'
                sh './${VENV}/bin/pip install -r requirements.txt'
            }
        }
        
        stage('Deploy') {
            steps {
                sh 'echo "Deploying to staging..."'
                sh "nohup ./${VENV}/bin/python app.py > app.log 2>&1 &"
                sh 'sleep 5' // Wait for the app to start
            }
        }
        stage('Test') {
            steps {
                sh 'ls -l test/'
                sh "./${VENV}/bin/pytest test/test_app.py"
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
