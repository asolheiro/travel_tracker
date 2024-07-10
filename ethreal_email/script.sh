#!/bin/bash
echo "Creating e-mails using https://ethereal.email/"

python ./ethreal_email/create_email.py > output_raw.txt

cat output_raw.txt  | sed "s/'/\"/g" > output_temp.txt

sed -i 's/False/"FALSE"/g' output_temp.txt
sed -i 's/True/"TRUE"/g' output_temp.txt

python -m json.tool output_temp.txt > ./ethreal_email/output_formatted.json

rm -f output_temp.txt --force
rm -f output_raw.txt --force