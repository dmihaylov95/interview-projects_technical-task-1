# interview-projects_technical-task-1

## Part 1

## Part 2 - AWS VPC Lister Lambda (Python)

This AWS Lambda function lists all VPCs and Subnets in your AWS account and saves them into a DynamoDB table named `NetworkResources`.

---

### Prerequisites

- AWS CLI configured
- AWS SAM CLI installed
- Python 3.9+

---

### Deployment with AWS SAM

1. **Install dependencies locally:**

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
