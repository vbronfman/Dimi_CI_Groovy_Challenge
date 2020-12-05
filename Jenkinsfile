#!groovy
// Jenkinsfile (Scripted Pipeline)
node { // node/agent

def commit_id

stage('Prepare') {
    
    echo 'Stage Prepare  ' // echo stage name
    checkout scm // is this any one better than next one? - ERROR: ‘checkout scm’ is only available when using “Multibranch Pipeline” or “Pipeline script from SCM”
    
    checkout changelog: false, poll: false, 
            scm: [$class: 'GitSCM', branches: [[name: '*/main']], 
                  doGenerateSubmoduleConfigurations: false, 
                  extensions: [], 
                  submoduleCfg: [], 
                  userRemoteConfigs: [[url: 'https://github.com/vbronfman/Dimi_CI_Groovy_Challenge.git']]]
   
    sh "git rev-parse --short HEAD > .git/commit-id"                        
    commit_id = readFile('.git/commit-id').trim()
    
  }

stage ('Merge'){ //add branch names as variable
 //  sh 'git tag -a tagName -m "Your tag comment"'
   sh 'git merge develop'
   sh 'git commit -am "Merged develop branch to master'
   
   //if failed 
   error("Build failed because of this and that..") // fail job if merge failed
   
   
   sh "git push origin master"
   
   
   error("Build failed because of this and that..") //Actively fail current pipeline job
}


   stage('test') {
     nodejs(nodeJSInstallationName: 'nodejs') {
       sh 'npm install --only=dev'
       sh 'npm test'
     }
   }
   stage('docker build/push') {
     docker.withRegistry('https://index.docker.io/v1/', 'dockerhub') {
       def app = docker.build("wardviaene/docker-nodejs-demo:${commit_id}", '.').push()
     }
   }
//}



  // This limits build concurrency to 1 per branch
//  properties([disableConcurrentBuilds()])
  
   if (env.BRANCH_NAME == 'master') {
            echo 'I only execute on the master branch'
        } else {
            echo 'I execute elsewhere'
        }
    }
    
 
  stage ('Merge'){
      echo 'Merge master into feature'
 }
  
  
  stage('Build') {
    echo 'Building...'
    //sh 'python --version'
    //sh 'docker-compose -d -f ./composetest/up'
  }
  
  stage('Test') {
      withEnv(['DOCKER_HOST=tcp://host.docker.internal:2375', 'PATH+EXTRA=/var/jenkins_home/tools/org.jenkinsci.plugins.docker.commons.tools.DockerTool/dockerjenkins/bin']) {
sh 'build_test.sh'
      //sh 'docker-compose -f ./composetest/docker-compose.yml up -d --build'
      //sh 'docker-compose -f ./composetest/docker-compose.yml exec web python app.test.py'
      }
  }
  
//}
/*
def commit_id
stage('Prepare') {
    echo 'Prepare $GLOBAL_STAGE_NAME name' // echo stage name
    checkout scm // is this any one better than next one? 
    
    checkout changelog: false, poll: false, 
            scm: [$class: 'GitSCM', branches: [[name: '*/main']], 
                  doGenerateSubmoduleConfigurations: false, 
                  extensions: [], 
                  submoduleCfg: [], 
                  userRemoteConfigs: [[url: 'https://github.com/vbronfman/Dimi_CI_Groovy_Challenge.git']]]
   
    sh "git rev-parse --short HEAD > .git/commit-id"                        
    commit_id = readFile('.git/commit-id').trim()
    
  }

stage ('Merge'){ //add branch names as variable
   sh 'git tag -a tagName -m "Your tag comment"'
   sh 'git merge develop'
   sh 'git commit -am "Merged develop branch to master'
   sh "git push origin master"
}
   stage('test') {
     nodejs(nodeJSInstallationName: 'nodejs') {
       sh 'npm install --only=dev'
       sh 'npm test'
     }
   }
   stage('docker build/push') {
     docker.withRegistry('https://index.docker.io/v1/', 'dockerhub') {
       def app = docker.build("wardviaene/docker-nodejs-demo:${commit_id}", '.').push()
     }
   }
}

// Jenkinsfile (Scripted Pipeline)
node { // node/agent

  // This limits build concurrency to 1 per branch
//  properties([disableConcurrentBuilds()])
  
   if (env.BRANCH_NAME == 'master') {
            echo 'I only execute on the master branch'
        } else {
            echo 'I execute elsewhere'
        }
    }
    
 
  stage ('Merge'){
      echo 'Merge master into feature'
 }
  
  
  stage('Build') {
    echo 'Building...'
    //sh 'python --version'
    //sh 'docker-compose -d -f ./composetest/up'
  }
  
  stage('Test') {
      withEnv(['DOCKER_HOST=tcp://host.docker.internal:2375', 'PATH+EXTRA=/var/jenkins_home/tools/org.jenkinsci.plugins.docker.commons.tools.DockerTool/dockerjenkins/bin']) {
sh 'build_test.sh'
      //sh 'docker-compose -f ./composetest/docker-compose.yml up -d --build'
      //sh 'docker-compose -f ./composetest/docker-compose.yml exec web python app.test.py'
      }
  }
  
}
*/
