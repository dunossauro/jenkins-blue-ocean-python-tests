pipeline {
  agent {
    dockerfile true
  }
  stages {
    stage('Testes de unidade') {
      steps {
        try {
          sh '''
pipenv install &&
pipenv run nose2 --plugin nose2.plugins.junitxml --junit-xml'''
        }
       finally {
       junit(allowEmptyResults: true, testResults: 'nose2-junit.xml', keepLongStdio: true)
      }
    }
    }
  }
}
