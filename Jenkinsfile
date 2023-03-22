pipeline {
  agent any
  stages {
    stage('Watch Github') {
      steps {
        git(url: 'https://github.com/tajexume/Character-Builder', branch: 'main')
      }
    }

    stage('Run Unit Tests') {
      steps {
        sh 'pytest test.py'
      }
    }

  }
}