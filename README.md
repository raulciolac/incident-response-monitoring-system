# Incident Response Monitoring System

## Overview
This project simulates a DevOps monitoring system with alerting and automated incident response.

## Features
- Application metrics exposed via Prometheus
- Alert detection (high error rate)
- Kubernetes deployment
- Auto-healing script (restart pods automatically)

## Tech Stack
- Python
- Docker
- Kubernetes
- Prometheus

## Project Structure
- app/ → application code
- docker/ → Dockerfile
- k8s/ → Kubernetes configs
- monitoring/ → Prometheus + alerts
- scripts/ → automation scripts

## Use Case
Detect application failures and automatically recover the system using DevOps practices.

## Future Improvements
- Grafana dashboards
- Alertmanager integration
- CI/CD pipeline
