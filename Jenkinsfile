pipeline {
  agent any
  stages {
    stage('Watch Github') {
      steps {
        git(url: 'https://github.com/tajexume/Character-Builder', branch: 'main')
      }
    }

    stage('Print Working Directory') {
      steps {
        sh 'pwd'
      }
    }

  }
}