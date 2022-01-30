istime='https://back-impuestos.blockchainconsultora.com';
signals='https://dbseniales.blockchainconsultora.com';
container='https://back.ltfastl.com';
local='http://localhost:3010';

curl -X POST -H "Content-Type: application/json" \
 $local/users/login \
 -d @auth.json | \
 egrep -o '\"[a-zA-Z0-9=\.\_\-]{60,400}\"' | \
 sed 's/\"//g' > token;          

echo 'this is your token';
cat token;
