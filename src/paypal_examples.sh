#!/bin/bash

curl -v https://api.sandbox.paypal.com/v1/oauth2/token \
  -H "Accept: application/json" \
  -H "Accept-Language: en_US" \
  -u "Ad4GARBAggxw3gWtJ2Hp7jb8fL4njBwzcyPaIMiBLdpwsVBLcvDyOR5lJBkR:EOCx4RAfEaYAGtLE28BOml0zwYdk-rvt6_01coHI7Cf44rwaE_DM73_mj9js" \
  -d "grant_type=client_credentials"