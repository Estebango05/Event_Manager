# Documentación de Despliegue

## 1. Prerrequisitos
- Azure CLI instalado y autenticado (`az login`).  
- Permisos para crear Resource Groups, ACR y ACI.  
- Docker instalado para builds locales.  

---

## 2. Resource Group
```bash
az group create --name event-manager-az --location southcentralus
```

---

## 3. Registrar Container Registry Provider
```bash
az provider register --namespace Microsoft.ContainerRegistry
```

---

## 4. Azure Container Registry (ACR)
```bash
az acr create --resource-group event-manager-az --name eventmanageracrregistry --sku Standard --location southcentralus --admin-enabled true
az acr credential show --name eventmanageracrregistry --resource-group event-manager-az --query "username" -o tsv
az acr credential show --name eventmanageracrregistry --resource-group event-manager-az --query "passwords[0].value" -o tsv
```

---

## 5. Desplegar PostgreSQL en ACI
```bash
az container delete -g event-manager-az -n my-postgres-aci --yes
az container create --resource-group event-manager-az --name my-postgres-aci --image postgres:15 --dns-name-label mypgdns --ports 5432 --cpu 1 --memory 1.5 --os-type Linux --environment-variables POSTGRES_USER=admin POSTGRES_PASSWORD='uno.2.tres' POSTGRES_DB=eventManagerDB
```

> URL de conexión: `postgresql://admin:uno.2.tres@mypgdns.southcentralus.azurecontainer.io:5432/eventManagerDB`

---

## 6. Construir & Publicar Backend
```bash
az acr login --name eventmanageracrregistry
docker build -t eventmanageracrregistry.azurecr.io/event-manager-be:latest ./backend
docker push eventmanageracrregistry.azurecr.io/event-manager-be:latest
```

---

## 7. Desplegar Backend en ACI
```bash
az container create --resource-group event-manager-az --name event-manager-be-aci --image eventmanageracrregistry.azurecr.io/event-manager-be:latest --os-type Linux --dns-name-label eventmanagerbeapi --ports 8000 --cpu 1 --memory 1.5 --registry-login-server eventmanageracrregistry.azurecr.io --registry-username <ACR_USER> --registry-password <ACR_PASS> --environment-variables DATABASE_URL="postgresql://admin:uno.2.tres@mypgdns.southcentralus.azurecontainer.io:5432/eventManagerDB"
```

> Endpoint API: `http://eventmanagerbeapi.southcentralus.azurecontainer.io:8000`

---

## 8. Construir & Publicar Frontend
```bash
docker build -t eventmanageracrregistry.azurecr.io/event-manager-fe:latest frontend/Event-Manager-Interface
docker push eventmanageracrregistry.azurecr.io/event-manager-fe:latest
```

---

## 9. Desplegar Frontend en ACI
```bash
az container create --resource-group event-manager-az --name event-manager-fe-aci --image eventmanageracrregistry.azurecr.io/event-manager-fe:latest --os-type Linux --dns-name-label eventmanagerfeui --ports 80 --cpu 1 --memory 1.5 --registry-login-server eventmanageracrregistry.azurecr.io --registry-username <ACR_USER> --registry-password <ACR_PASS> --environment-variables REACT_APP_API_URL="http://eventmanagerbeapi.southcentralus.azurecontainer.io:8000"
```

> URL Frontend: `http://eventmanagerfeui.southcentralus.azurecontainer.io`

---

## 10. Verificación
- **Estado contenedores**:  
  ```bash
  az container show -g event-manager-az -n <ACI_NAME> --query "instanceView.state" -o tsv
  ```
- **Logs**:  
  ```bash
  az container logs -g event-manager-az -n <ACI_NAME>
  ```

