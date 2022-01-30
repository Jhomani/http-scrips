invoices='https://back-impuestos.blockchainconsultora.com'; 
istime='https://back-itsmine.blockchainconsultora.com';
container='https://dback.ltfastl.com';
signals='https://dbseniales.blockchainconsultora.com';
local='http://localhost:3010';

token=$(cat token);
filter=$(node filter.js);

curl -X GET -H "Content-Type: application/json" \
 -H "Authorization: Bearer ${token}" \
 $signals/symbols/verified