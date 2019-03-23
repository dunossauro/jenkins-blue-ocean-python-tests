pipeline {
  agent {
    dockerfile true
  }
  stages {
    stage('Testes de unidade') {
      steps {
        sh '''
pipenv install &&
pipenv run nose2 --plugin nose2.plugins.junitxml --junit-xml'''
        junit(testResults: 'nose2-junit.xml', keepLongStdio: true)
      }
    }
  }
}
