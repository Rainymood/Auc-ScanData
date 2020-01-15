# Auc-ScanData.lua

This project converts Auctioneer scan data into a valid JSON file for parsing. 

## Setup

If you don't have lua, first install it. 

```bash
brew install lua
```

Then install luarocks to manage your dependencies. 

```bash
brew install luarocks
```

Use luarocks to install dkjson

```bash
luarocks install dkjson
```

## Your first `.lua` script

Getting started is as easy as this

```bash
echo 'print("Hello World!")' > hello.lua 
lua hello.lua
```

## Conversion `.lua` to `.json`

To convert the `.lua` to `.json` we slightly modify the original `.lua` file with the following changes.

```lua
local json = require("dkjson")

...

local AucScanDataJson = json.encode(AucScanData, {indent=true})
print(AucScanDataJson)
```

We use some bash magic to do so

```bash
sed '1s;^;local json = require("dkjson");' Auc-ScanData.lua > ConvertScript.lua
echo "local AucScanDataJson = json.encode(AucScanData, {indent=true})" >> ConvertScript.lua
echo "print(AucScanDataJson)" >> ConvertScript.lua
```

Then we can run it with 

```bash
lua ConvertScript.lua > Auc-ScanData.json
```

## Resources

* [lua-users.org](http://lua-users.org/wiki/JsonModules)
* [luarocks](https://github.com/luarocks/luarocks/wiki/Using-LuaRocks)

## Questions that I've Googled

* "import variable lua from another file"
* "lua variables import other file"
* "require returns boolean"
* "save lua to file"
* "shell prepend file" 
* "prepend text to file python"