
echo "In: $1"
echo "Out: $2"
sed '1s;^;local json = require("dkjson");' $1 > ConvertScript.lua
echo "local AucScanDataJson = json.encode(AucScanData, {indent=true})" >> ConvertScript.lua
echo "print(AucScanDataJson)" >> ConvertScript.lua
echo "Converting $1 to $2..."
lua ConvertScript.lua > $2
rm ConvertScript.lua