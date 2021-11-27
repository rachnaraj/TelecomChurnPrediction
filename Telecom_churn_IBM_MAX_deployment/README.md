**This is an end-to-end deployment of churn prediction using IBM MAX framework and docker image**
**A big shout-out to Saishruthi Swaminathan and AIEngineering Youtube channel for this wonderful end-to-end project demo**

Using Max-Framework: max-framework has the basic code to get our code run as micro-service
	https://github.com/IBM/MAX-Framework

ibm created a skeleton (template)
	https://github.com/IBM/MAX-Skeleton

Tutorial Video:
	https://www.youtube.com/watch?v=ehS6tmQveA4&t=3998s

## Users with github account can use the max-skeleton with below steps
1. need to login to github and go to MAX Skeleton
2. click on "Use this template" and need to provide one name
3. and then needs cloning with below command
	git clone https://github.com/[repo]

4. # For testing purpose, we are filling temp values in Dockerfile as per SSaishruthi
https://max-cdn.cdn.appdomain.cloud/max-wrapping-demo/1.0.0
assets.tar.gz


5. requirements.txt (update it)


6. In config.py, update the API metadata.
This metadata is used to characterize the API wrapping the model
- API_TITLE
- API_DESC
- API_VERSION
- set MODEL_NAME = 


7. We need to update the model.py file. All the methods

8. run the command on terminal/git bash
	> sha512sum assets/classifier.pkl
copy this value to sha512sums.txt


** The model was in notebook, but with this framework we were successfully able to provide RestAPI to the model

9. Building the docker image
	// docker build -t max .
	# docker image build -t max .
	// -t is 'tag'
	// . to refer the dockerfile under current directory

10. running the docker image
	docker run -it -p 5000:5000 max
	# docker run -d -p 5000:5000 max

11. load url:
	http://0.0.0.0:5000/
	It might be running on http://192.168.99.100:5000/ (default docker IP: > docker-machine ip default)
	// In Toolbox, nothing will be localhost, and will be 192.168.99.100 by default, since it's running a Linux VM in VirtualBox.