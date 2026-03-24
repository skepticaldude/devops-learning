
# API Health Monitoring with Cron

## Objective
Set up a **dedicated health endpoint** for a Python API and monitor it automatically using a cron job.

---

## Background

Previously, a Python backend API and Nginx reverse proxy were set up:

- API running on **port 5000**
- Nginx forwarding traffic on **port 80**
- Endpoints included:
  - `/` → basic server status
  - `/time` → current server time

---

## Goal

- Add a **/health endpoint** for dedicated health checks  
- Automate monitoring using cron jobs  
- Log server status every minute

---

## Python API: Complete File

```python
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            response = {
                "status": "ok",
                "message": "server is running"
            }

        elif self.path == "/time":
            import datetime
            response = {
                "current_time": str(datetime.datetime.now())
            }

        elif self.path == "/health":
            response = {
                "status": "healthy"
            }

        else:
            response = {
                "error": "not found"
            }

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(response).encode())

server = HTTPServer(("0.0.0.0", 5000), MyHandler)
print("Server running on port 5000...")
server.serve_forever()
````

---

## Running the API

```bash
python3 ~/api_server.py
```

---

## Testing the Health Endpoint

```bash
curl http://localhost/health
```

Expected output:

```json
{"status": "healthy"}
```

---

## Setting Up Cron Monitoring

### Step 1 — Open cron

```bash
crontab -e
```

### Step 2 — Add monitoring job

```bash
* * * * * echo "[$(date)] $(curl -s -o /dev/null -w "%{http_code}" http://localhost/health)" >> ~/health.log
```

> This logs the HTTP status code from `/health` every minute.

---

## Expected Behavior

* Each minute, a new line is appended to `~/health.log`:

```bash
[Mon Mar 22 09:01:00] 200
[Mon Mar 22 09:02:00] 200
```

* Stop the API to simulate failure:

```bash
CTRL + C
```

* Log entries should now show `502` or `000` for failed checks.

---

## Key Learnings

* Dedicated `/health` endpoint for monitoring
* Cron jobs run independently of the terminal
* Logs provide automated failure detection
* Observed environment limitations (Docker Desktop WSL vs Ubuntu WSL)
* Real-world workflow mirrors professional DevOps setups

---

## Next Steps

* Add alerting (email/slack notifications on failure)
* Deploy API and monitoring on a cloud VM
* Introduce structured logging and metrics collection
* Expand to multiple endpoints and services

```
