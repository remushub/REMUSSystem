properties([
	pipelineTriggers([pollSCM('* * * * *')])
	])

node {
	
	def app
	
	stage('Clone Repository') {
		checkout scm
	}
	
	stage('Build image') {
		app = docker.build("remushub/aspnet-test", "-f ./dockerfiles/Remus.Test/Dockerfile .")
	}
	
	stage('Test') {
		app.inside {
			sh 'dotnet test /app' 
		}
	}
	
	stage('Approval') {
		timeout(time: 1, unit: 'HOURS') {
			input 'Done?'
		}
	}
}