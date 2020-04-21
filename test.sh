a=$(date +%F_%H-%M-%S)
Curl -u rsekaran:11893a5cb5780c5fecb4e61f9df5dccfce -XPOST https://jenkins-ci.iherb.net/createItem?name=IherbAutomation1 --data-binary @mylocalconfig.xml -H "Content-Type:text/xml"
sleep 5
Curl -u rsekaran:11893a5cb5780c5fecb4e61f9df5dccfce -XPOST https://jenkins-ci.iherb.net/job/IherbAutomation1/buildWithParameters
sleep 1
echo Curl -u rsekaran:11893a5cb5780c5fecb4e61f9df5dccfce -XPOST https://jenkins-ci.iherb.net/job/IherbAutomation1/buildNumber
