terraform {
  required_version = ">= 1.0.0"
  required_providers {
    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = "~> 2.25.0"
    }
    helm = {
      source  = "hashicorp/helm"
      version = "~> 2.12.0"
    }
  }
}

# Провайдер для связи с нашим локальным Minikube
provider "kubernetes" {
  config_path = "~/.kube/config"
}

provider "helm" {
  kubernetes {
    config_path = "~/.kube/config"
  }
}

# 1. Создаем отдельный Namespace через Terraform
resource "kubernetes_namespace" "marketplace_tf" {
  metadata {
    name = "marketplace-tf"
  }
}

# 2. Автоматически деплоим наш Helm Chart в этот Namespace
resource "helm_release" "marketplace" {
  name      = "marketplace-tf-release"
  chart     = "../helm/marketplace" # Путь к нашему локальному Helm-чарту
  namespace = kubernetes_namespace.marketplace_tf.metadata[0].name

  values = [
    file("../helm/marketplace/values.yaml")
  ]
}