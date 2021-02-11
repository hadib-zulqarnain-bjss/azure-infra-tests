```
pytest --no-summary \
       --tls-versions="TLS1_0,TLS1_1,TLS1_2,None" \
       --network-access="Deny,Allow,None" \
       --allowed-locations="uksouth,ukwest,UK South,UK West,westeurope,eastus,westus" \
       tests/azure-infra-tests
```