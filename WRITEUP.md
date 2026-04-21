# Write-up Template

### Analyze, choose, and justify the appropriate resource option for deploying the app.

Azure App chosen due to the Cost, scalability, and availability
**Cost**
App Service supports:
Free (F1) tier
Low-cost Basic tiers
No OS or infrastructure management costs.
Pay only for the application hosting plan.

**Scalability**
Built-in horizontal and vertical scaling
Scaling can be configured via:
Azure Portal
Autoscale rules

**Availability**
High availability is built in:
Managed infrastructure
Automated restarts
Integrated logging and monitoring
No OS patching required by the developer.
No application changes required.

**Workflow and Dev experience**
Integrated GitHub Actions deployment
Environment variables managed via Azure Portal
Built-in:
HTTPS
Logging (Log Stream)
Restart / redeploy controls

Final decisiont for deployment based on:
Flask web app with standard dependencies
No OS-level customization required
Uses Azure-native services:
Azure SQL Database
Azure Blob Storage
Microsoft Entra ID (MSAL)
Lower cost, lower maintenance, faster deployment

### Assess app changes that would change your decision.
App-Level Changes

Requirement for:

Persistent background workers (Celery, custom daemons)
Non-HTTP services
Custom OS packages or drivers


Multi-process or stateful workloads that exceed App Service constraints

Infrastructure Needs

Fine-grained control over:

OS kernel
Network stack
Security tooling


Deployment of non-web services alongside Flask

*Detail how the app and any other needs would have to change for you to change your decision in the last section.* 
If switching to a VM-based deployment, the following changes would be required:

Provision and secure a Linux VM
Manually install:

Python
Virtual environment
Dependencies
Gunicorn + NGINX


Configure:

Reverse proxy
Firewall rules
HTTPS certificates


Set up monitoring, backups, and OS patching

These changes would significantly increase operational complexity for little benefit in this project.
