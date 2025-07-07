# CI/CD Pipeline with Jenkins for Python Web Application

This guide walks you through setting up a CI/CD pipeline using Jenkins for a Python web application.

## 1. Setup

- **Install Jenkins**:  
   - [Jenkins Installation Guide](https://www.jenkins.io/doc/book/installing/)
      ```bash
      sudo wget -O /etc/apt/keyrings/jenkins-keyring.asc \
      https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key
      echo "deb [signed-by=/etc/apt/keyrings/jenkins-keyring.asc]" \
      https://pkg.jenkins.io/debian-stable binary/ | sudo tee \
      /etc/apt/sources.list.d/jenkins.list > /dev/null
      sudo apt-get update
      sudo apt-get install jenkins
      ```
    - **Jenkins -agent node configuration: **
   - create new EC2 instance with Java.
   - copy the agent jar and execute the agent start up command in background
   ```bash
        curl -sO http://44.251.219.26:8080/jnlpJars/agent.jar
        java -jar agent.jar -url http://44.251.219.26:8080/ -secret e6b7dea27f44d625632e8f79a090bd02b24c858a7d1fb3779c64eda61fc9063f -name agent1 -webSocket -workDir "/home/ubuntu/Jenkins_agent" &
    ```
![Jenkins_installation](https://github.com/user-attachments/assets/0b19a1e8-6592-4352-b0be-bb46cf11b57e)
![Agent_node](https://github.com/user-attachments/assets/59544f84-bfbf-40e4-aeec-19adfeb10a96)


## 2. Source Code

- **Fork the Repository**:  
    - Example repo: [Sample Python Flask App](https://github.com/ranyabrkumar/Simple_Flask_App.git)
- **Clone the Repository**:  
    - SSH into your Jenkins server and run:  
        ```bash
        git clone https://github.com/ranyabrkumar/Simple_Flask_App.git
        ```

## 3. Jenkins Pipeline

- **Create a Jenkinsfile** in the root of your repository with the following stages:

    ```
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
    ```
![jenkins_job](https://github.com/user-attachments/assets/c1c92396-2fd2-4702-8258-6afcbd17ebf3)

## 4. Triggers

- **Configure Build Triggers**:  
    - In Jenkins, set the pipeline to trigger on changes to the `main` branch (Used "GitHub hook trigger for GITScm polling").
    - Added a web hook in GitHub http://<jenkins_server>/github-webhook/
    - Add a change in branch it will trigger the jenkins job.
      ![GH_WebHook_config](https://github.com/user-attachments/assets/18e3b95c-dc19-49d2-a367-e9998b8d3c20)

## 5. Notifications

- **Email Notifications**:  
    - Configure Jenkins with SMTP settings.
        STMP SERVER: smtp.gmail.com
        SMTP Port : 587
        SMTP User Name : <gmail user name>
        STMP Password : generated a pass key from google account
![SMTP_CONFIG](https://github.com/user-attachments/assets/62977950-78d5-45e8-8fbf-a8f46b992da0)

    - The `post` section in the Jenkinsfile sends emails on build success or failure.
![email_notofication](https://github.com/user-attachments/assets/22dcc077-4855-4e43-8d98-4482e61846cb)

---


