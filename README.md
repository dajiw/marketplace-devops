
# Marketplace Microservices DevOps Infrastructure

Полноценная инфраструктура для развертывания микросервисного приложения (Marketplace) с использованием концепций **Infrastructure as Code (IaC)**, **GitOps**, **CI/CD** и **Observability**.

---

## Технологический стек

* **Virtualization & OS:** Vagrant (Ubuntu 22.04 LTS)
* **Containerization:** Docker, Docker Hub
* **Orchestration:** Kubernetes (Minikube)
* **Packaging & Delivery:** Helm (v3)
* **Infrastructure as Code (IaC):** Terraform
* **CI/CD:** GitHub Actions
* **Observability & Monitoring:** Prometheus, Grafana

---

## Архитектура системы

```
                                +-------------------+
                                |   GitHub Actions  |
                                |      (CI/CD)      |
                                +---------+---------+
                                          |
                                          v (Push Images)
                                +-------------------+
                                |    Docker Hub     |
                                +---------+---------+
                                          |
   +--------------------------------------|---------------------------------------+
   | Vagrant VM (Ubuntu)                  v (Pull Images)                         |
   |  +------------------------------------------------------------------------+  |
   |  | Kubernetes Cluster (Minikube)                                          |  |
   |  |                                                                        |  |
   |  |  [ Terraform ] ──> Manages Namespaces & Releases                       |  |
   |  |                                                                        |  |
   |  |  +---------------------------+    +---------------------------------+  |  |
   |  |  | Namespace: marketplace-tf |    | Namespace: monitoring           |  |  |
   |  |  |                           |    |                                 |  |  |
   |  |  |  * Catalog Service        |    |  * Prometheus                   |  |  |
   |  |  |  * Order Service          |    |  * Grafana                      |  |  |
   |  |  |  * Ingress Controller     |    |  * Node Exporter                |  |  |
   |  |  +---------------------------+    +---------------------------------+  |  |
   |  +------------------------------------------------------------------------+  |
   +------------------------------------------------------------------------------+
```
---

## Структура репозитория

marketplace-devops/
├── .github/workflows/    # CI/CD пайплайны GitHub Actions
├── helm/                 # Helm Chart приложения
│   └── marketplace/
│       ├── Chart.yaml
│       ├── values.yaml
│       └── templates/
├── terraform/            # IaC конфигурация управления Kubernetes и Helm
│   └── main.tf
├── k8s/                  # Статические YAML-манифесты (legacy/reference)
├── Vagrantfile           # Описание окружения виртуальной машины
└── README.md



