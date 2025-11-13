terraform {
  required_version = ">= 1.6.0"
}

# Minimal IaC just for Checkov demo (no cloud provider configured here)
resource "null_resource" "demo" {
  triggers = {
    owner = "platform-engineering"
  }
}
