pipeline{
		agent any
		options{
			ansiColor('xterm')
			buildDiscarder(logRotator(numToKeepStr:'10')
			disableConcurrentBuilds()
			timeout(time: 30, unit: 'MINUTES')
			timestamps()
		}
		
		environment{
			CFN_TEMPLATES_REPO = 'marinehadd/DevOps'
			CFN_TEMPLATES_PATH = 'DevOps'
			CFN_TEMPLATES_REPO_BRANCH = 'master'
			CFN_TEMPLATES_LOCATION = 'DevOps/cloudformation-infra-lb.yaml'				
			STACK_NAME = "Infra Setup"	
		}
		
		stages{
			stage('Checkout CFN templates'){
				steps{
					script{
						ansiColor('xterm'){
							checkoutRepository(repository: CFN_TEMPLATES_REPO, branch: CFN_TEMPLATES_REPO_BRANCH)
							checkoutRepository(repository: TEMPLATES_PARAMETERS_REPO, branch: TEMPLATES_PARAMETERS_REPO_BRANCH)
					}
				}
			}
		} //End of checkout stage
			
			stage('Deploy CFN resources'){
				steps{
					script{
						ansiColor('xterm'){
							runCloudFormationStack(STACK_NAME,
													CFN_TEMPLATES_LOCATION)
					}
				}
			}
		}
	} // end of stack deployment
}
						
			
										
