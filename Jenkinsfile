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

    stage('error') {
      steps {
        sh 'python3 pytest service_unit_tests.py --junitxml=results.txt'
      }
    }

  }
}