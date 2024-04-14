#!/bin/bash

# Obtener la versión actual del chart
CURRENT_VERSION=$(grep "version:" ./k8s/helm/Chart.yaml | awk '{print $2}')

# Incrementar la versión (puedes adaptar este paso según tu estrategia de versionado)
NEW_VERSION=$(echo $CURRENT_VERSION | awk -F. '{$NF = $NF + 1;} 1' | sed 's/ /./g')

# Actualizar la versión en el archivo Chart.yaml
sed -i "s/version: $CURRENT_VERSION/version: $NEW_VERSION/g" ./k8s/helm/Chart.yaml

echo "Updated version from $CURRENT_VERSION to $NEW_VERSION"

echo $NEW_VERSION

