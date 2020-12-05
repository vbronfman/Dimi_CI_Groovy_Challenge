#!/usr/bin/env groovy
// Jenkinsfile (Scripted Pipeline)

def commitHash

def test( ) { //prints the hash of the current git commit and waits ~3 min It is expected to always pass 
    echo "Start test "
    
    echo "prints the hash of the current git commit and waits ~3 min"
    /*
     git_commit = sh (
        script: 'git rev-parse HEAD',
        returnStdout: true
    ).trim()
    */
    
    echo "Starts build_test.sh..."
    tested= sh (
       script: './build_test.sh', // bogus test script
       returnStdout: true
    ).trim()
    echo 'After start build_test.sh: $tested'
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
  def result = sh ' git status -uno | grep ${check} ' // | awk -F \'"\' {\'print $2\'}' //doesn't work

  //if (sh 'git diff origin/master'){ //main  git status -uno
  if ($result){ //main  git status -uno
   // 
    return 0
  }
  else {
    return 1
  }
}

node ('master'){ // node/agent
def commit_id
def scmVars 
def branch

stage('Prepare') {
    
    echo 'Stage Prepare : checkout scm ' // echo stage name
   scmVars =  checkout scm // is this any one better than next one? - ERROR: ‘checkout scm’ is only available when using “Multibranch Pipeline” or “Pipeline script from SCM”
   commitHash = scmVars.GIT_COMMIT
    
    // checkout changelog: false, poll: false, 
            // scm: [$class: 'GitSCM', branches: [[name: '*/main']], 
                  // doGenerateSubmoduleConfigurations: false, 
                  // extensions: [], 
                  // submoduleCfg: [], 
                  // userRemoteConfigs: [[url: 'https://github.com/vbronfman/Dimi_CI_Groovy_Challenge.git']]]
   
    //sh "git rev-parse --short HEAD > .git/commit-id"  //hangs up entire build 
    //commit_id = readFile('.git/commit-id').trim()
    echo "Commit ID = $commitHash"
    branch = scmVars.GIT_BRANCH
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
"...You can either git merge master or git rebase master." //??
*/

/* Should I try this out insted? 
  parallel firstBranch: {
        // do something
    }, secondBranch: {
        // do something else
    },
    failFast: true|false
*/

def cmd = ['git',  'status', '-uno', '|', 'grep', "Your branch is up to date with 'origin/main'"]
def process = cmd.execute()
def stdOut = process.inputStream.text
def stdErr = process.errorStream.text

echo "Output of '  'git',  'status', '-uno', '|', 'grep', Your branch is up to date with 'origin/main' " + stdOut + stdErr

//def printout = "printenv".execute().text // +
echo "scmVars.GIT_BRANCH =" + scmVars.GIT_BRANCH

//if ($branch == 'master') 
{
   echo 'branch - master'
   //sh 'git checkout feature'
   //'git checkout feature'.execute().text
   def proc = "git checkout feature".execute()
   def b = new StringBuffer()
   proc.consumeProcessErrorStream(b)

  println proc.text   
  println b.toString() //error message if any

   //sh 'git merge master'
   //def statusCode = sh 'git merge master', returnStatus:true
   proc = 'git merge master'
   proc.consumeProcessErrorStream(b)
   println proc.text
   println b.toString()

   def statusCode = 0 //default
   if (statusCode !=0 ){ 
      //if merge failed 
      error("Build failed because of this and that..") // fail job if merge failed;//Actively fail current pipeline job
    }
      //sh 'git commit -am "Merged master branch to feature'
       git_merge_commit = sh (
       script: 'git commit -am "Merged master branch to feature',
       returnStdout: true
       ).trim()

   println ("Merge result " + git_merge_commit)

        test() //custom test to run

        if (isThereChangeInMaster()){ // if master has been changed during the run, runs again (again, merge from master, and again, fake "test") - should be function/method here
           sh "git push origin master"

        }

  
}
}



} 