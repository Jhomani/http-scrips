#!/usr/bin/bash

invoices='https://back-impuestos.blockchainconsultora.com'; 
istime='https://back-itsmine.blockchainconsultora.com';
container='https://dback.ltfastl.com';
signals='https://dbseniales.blockchainconsultora.com';
local='http://localhost:3010';

token=$(cat token);
filter=$(node filter.js);

#curl -X GET -H "Authorization: Bearer ${token}" \
# $host_local/pagos-net/ffa93bbb-9c1d-4cd2-bca7-bb50da7e025d/Tarjeta \

#curl -X POST -H "Content-Type: application/json" \
# -H "Authorization: Bearer ${token}" \
# $host_local/subscription/129d75fd-c10e-4422-b802-23b2cb9bb0db \
# -d @body2.json;

#curl -X POST -H "Content-Type: application/json" \
# -H "Authorization: Bearer ${token}" \
# $container/signup \
# -d @newuser.json;

#curl -X POST -H "Content-Type: application/json" \
# -H "Authorization: Bearer ${token}" \
# $local/payment-deatails/cascade \
# -d @paymentDetail.json;


#curl -X POST -H "Content-Type: application/json" \
# -H "Authorization: Bearer ${token}" \
# $local/payments/purchase \
# -d @body4.json;

#curl -X PATCH -H "Content-Type: application/json" \
# -H "Authorization: Bearer ${token}" \
# $host_local/users/694d7f59-31fd-432a-9c26-5bebe9230f9d \
# -d @body2.json;

#curl -X POST  -H "Authorization: Bearer ${token}" \
#	-F "image=@/home/jhomani/Pictures/great.png" \
#	-F "promotionId=10a97010-44c2-46a8-b301-cdabc53bf226" \
#	$host_local/file-storages;

#curl -X DELETE -H "Content-Type: application/json" \
# -H "Authorization: Bearer ${token}" \
# $signals/tracking-rooms\
# -d @body.json;

# curl -X DELETE -H "Content-Type: application/json" \
# -H "Authorization: Bearer ${token}" \
# $host_local/file-storages/98efc231-573b-404d-8799-7d3289553771 \
