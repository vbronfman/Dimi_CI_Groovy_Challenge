#!groovy
// Jenkinsfile (Scripted Pipeline)
node { // node/agent

def commit_id

stage('Prepare') {
    
    echo 'Stage Prepare  ' // echo stage name
    checkout scm // is this any one better than next one? - ERROR: ‘checkout scm’ is only available when using “Multibranch Pipeline” or “Pipeline script from SCM”
    
    
    // checkout changelog: false, poll: false, 
            // scm: [$class: 'GitSCM', branches: [[name: '*/main']], 
                  // doGenerateSubmoduleConfigurations: false, 
                  // extensions: [], 
                  // submoduleCfg: [], 
                  // userRemoteConfigs: [[url: 'https://github.com/vbronfman/Dimi_CI_Groovy_Challenge.git']]]
   
    //sh "git rev-parse --short HEAD > .git/commit-id"  //hangs up entire build 
    //commit_id = readFile('.git/commit-id').trim()
    echo "Commit ID = $commit_id"
    def branch = env.BRANCH_NAME
    echo "branch $branch"
    
  }

////////////////////////////////////////////////
stage ('Merge'){   //add branch names as variable
  echo 'Stage Merge:  merge master into feature'

 //  sh 'git tag -a tagName -m "Your tag comment"'
 /*
 How do we merge the master branch into the feature branch? Easy:

git checkout feature
git merge master
====
You can either git merge master or git rebase master.
*/

/* Should I try this out insted? 
  parallel firstBranch: {
        // do something
    }, secondBranch: {
        // do something else
    },
    failFast: true|false
*/

sh 'printenv'

 if (env.BRANCH_NAME == 'master') {
   echo 'branch - master'
   sh 'git checkout feature'
 
   //sh 'git merge master'
   def statusCode = sh 'git merge master', returnStatus:true
   if (statusCode !=0 ){
      //if merge failed 
      error("Build failed because of this and that..") // fail job if merge failed;//Actively fail current pipeline job
   }
   else {
        sh 'git commit -am "Merged master branch to feature'

        test() //custom test to run
        if (isThereChangeInMaster()){
           sh "git push origin master"
        }

   }
 }
}

// This limits build concurrency to 1 per branch
//  properties([disableConcurrentBuilds()])
  stage('Build') {
    echo 'Building...'
    //sh 'python --version'
    //sh 'docker-compose -d -f ./composetest/up'
     setBuildStatus ("Some context ", 'Checking out completed', 'SUCCESS')

  }

}
def test() {
    echo "Start"
    //prints the hash of the current git commit and waits ~3 min
    echo "prints the hash of the current git commit and waits ~3 min"
    sleep(3)
    echo "Stop"

    //return 0
}

def isThereChangeInMaster(){
  //def cmd = ['/bin/sh',  'git',  'status', '-uno' | grep "Your branch is up to date with 'origin/main'" ']
   //some regex here? 
   /*
   cmd.execute().with{
   def output = new StringWriter()
   def error = new StringWriter()
   //wait for process ended and catch stderr and stdout.
   it.waitForProcessOutput(output, error)
   //check there is no error
   println "error=$error"
   println "output=$output"
   println "code=${it.exitValue()}"
 }
 */
  //seems way simpler 
  def check = "Your branch is up to date with 'origin/main'"
  def result = sh ' git status -uno | grep ${check} ' // | awk -F \'"\' {\'print $2\'}'

  //if (sh 'git diff origin/master'){ //main  git status -uno
  if ($result){ //main  git status -uno
   // 
    return 0
  }
  else {
    return 1
  }
  
}

 