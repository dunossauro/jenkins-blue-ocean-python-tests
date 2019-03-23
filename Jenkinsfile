pipeline {
  // Run code inside docker using `Dockerfile` in repo
  agent { dockerfile true }
  stages {
    stage('Testes de unidade') { // Run unittests in first stage
      steps {
        sh '''
pipenv install &&
pipenv run nose2 --plugin nose2.plugins.junitxml --junit-xml'''
        junit(testResults: 'nose2-junit.xml', keepLongStdio: true)
      }
    }
  }
}
