groovy
      pipeline {
            agent any

            environment {
                  VENV = 'venv'
            }

            stages {
                  stage('Build') {
                        steps {
                              sh 'python3 -m venv $VENV'
                              sh './venv/bin/pip install -r requirements.txt'
                        }
                  }
                  stage('Test') {
                        steps {
                              
                              sh './venv/bin/pytest tests/'
                        }
                  }
                  stage('Deploy') {
                        when {
                              branch 'main'
                        }
                        steps {
                              sh 'echo "Deploying to staging..."'
                              // Add deployment commands here
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
