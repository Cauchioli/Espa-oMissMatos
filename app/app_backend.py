import http.server
import json
import os
from datetime import datetime


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CACHE_FILE = os.path.join(BASE_DIR, "instagram_cache.json")


class MetricsHandler(http.server.BaseHTTPRequestHandler):
    def send_cors_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS, DELETE")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_cors_headers()
        self.end_headers()

    def do_GET(self):
        if self.path == "/api/metrics":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_cors_headers()
            self.end_headers()
            
            data = {"profile": {}, "posts": [], "insights_7d": {}}
            if os.path.exists(CACHE_FILE):
                try:
                    with open(CACHE_FILE, "r", encoding="utf-8") as f:
                        data = json.load(f)
                except Exception as e:
                    print("Error reading cache file:", e)
            
            self.wfile.write(json.dumps(data).encode("utf-8"))
        elif self.path.startswith("/api/crm/leads"):
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_cors_headers()
            self.end_headers()
            
            crm_file = os.path.join(BASE_DIR, "crm_database.json")
            data = {"leads": []}
            if os.path.exists(crm_file):
                try:
                    with open(crm_file, "r", encoding="utf-8") as f:
                        data = json.load(f)
                except Exception as e:
                    print("Error reading CRM file:", e)
            self.wfile.write(json.dumps(data).encode("utf-8"))
        elif self.path == "/api/ideas":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_cors_headers()
            self.end_headers()
            
            ideas_file = os.path.join(BASE_DIR, "ideas_database.json")
            data = []
            if os.path.exists(ideas_file):
                try:
                    with open(ideas_file, "r", encoding="utf-8") as f:
                        data = json.load(f)
                except Exception as e:
                    print("Error reading ideas file:", e)
            self.wfile.write(json.dumps(data).encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        if self.path == "/api/metrics":
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            
            try:
                new_data = json.loads(post_data.decode("utf-8"))
            except Exception as e:
                self.send_response(400)
                self.send_cors_headers()
                self.end_headers()
                self.wfile.write(b"Invalid JSON")
                return

            # Read existing
            cache = {"profile": {}, "posts": [], "insights_7d": {}, "insights_30d": {}, "audience": {}, "daily_insights": []}
            if os.path.exists(CACHE_FILE):
                try:
                    with open(CACHE_FILE, "r", encoding="utf-8") as f:
                        cache = json.load(f)
                except Exception as e:
                    print("Error reading cache file:", e)

            # Update all keys dynamically
            for key, val in new_data.items():
                if key == "posts":
                    # Update posts (merge by id)
                    existing_posts = {p["id"]: p for p in cache.get("posts", [])}
                    for np in val:
                        pid = np["id"]
                        if pid in existing_posts:
                            existing_posts[pid].update(np)
                        else:
                            existing_posts[pid] = np
                    cache["posts"] = list(existing_posts.values())
                elif key == "daily_insights":
                    # Merge daily_insights by date
                    existing_days = {d["date"]: d for d in cache.get("daily_insights", [])}
                    for nd in val:
                        dkey = nd["date"]
                        if dkey in existing_days:
                            existing_days[dkey].update(nd)
                        else:
                            existing_days[dkey] = nd
                    cache["daily_insights"] = sorted(existing_days.values(), key=lambda x: x["date"], reverse=True)
                elif isinstance(val, dict):
                    if key not in cache or not isinstance(cache[key], dict):
                        cache[key] = {}
                    cache[key].update(val)
                else:
                    cache[key] = val

            # Always update last_saved with current time of the backend save
            cache["last_saved"] = datetime.now().isoformat()

            # Save cache
            try:
                with open(CACHE_FILE, "w", encoding="utf-8") as f:
                    json.dump(cache, f, indent=2, ensure_ascii=False)
            except Exception as e:
                print("Error writing cache file:", e)
                self.send_response(500)
                self.send_cors_headers()
                self.end_headers()
                self.wfile.write(b"Error saving data")
                return

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_cors_headers()
            self.end_headers()
            self.wfile.write(json.dumps({"status": "success"}).encode("utf-8"))
        elif self.path == "/api/crm/leads":
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            try:
                new_lead = json.loads(post_data.decode("utf-8"))
            except Exception as e:
                self.send_response(400)
                self.send_cors_headers()
                self.end_headers()
                self.wfile.write(b"Invalid JSON")
                return
            
            crm_file = os.path.join(BASE_DIR, "crm_database.json")
            data = {"leads": []}
            if os.path.exists(crm_file):
                try:
                    with open(crm_file, "r", encoding="utf-8") as f:
                        data = json.load(f)
                except Exception as e:
                    print("Error reading CRM file:", e)
            
            leads = data.setdefault("leads", [])
            
            # If no ID, generate one and set creation date
            lead_id = new_lead.get("id")
            if not lead_id:
                import uuid
                new_lead["id"] = "lead-" + str(uuid.uuid4())[:8]
                new_lead["date_created"] = datetime.now().isoformat()
            
            # Merge logic
            found = False
            for i, p in enumerate(leads):
                if p["id"] == new_lead["id"]:
                    leads[i].update(new_lead)
                    found = True
                    break
            if not found:
                leads.append(new_lead)
                
            try:
                with open(crm_file, "w", encoding="utf-8") as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)
            except Exception as e:
                print("Error writing CRM file:", e)
                self.send_response(500)
                self.send_cors_headers()
                self.end_headers()
                self.wfile.write(b"Error saving data")
                return
            
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_cors_headers()
            self.end_headers()
            self.wfile.write(json.dumps(new_lead).encode("utf-8"))

        elif self.path == "/api/webhook/instagram-lead":
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            try:
                payload = json.loads(post_data.decode("utf-8"))
            except Exception as e:
                self.send_response(400)
                self.send_cors_headers()
                self.end_headers()
                self.wfile.write(b"Invalid JSON")
                return
                
            import uuid
            new_lead = {
                "id": "lead-" + str(uuid.uuid4())[:8],
                "name": payload.get("name", "Instagram Lead"),
                "instagram": payload.get("instagram", "@stranger"),
                "phone": payload.get("phone", ""),
                "value_charged": 0.0,
                "value_paid": 0.0,
                "value_expenses": 0.0,
                "stage": "new",
                "proposal_details": "Capturado via Instagram Webhook / Link Request",
                "date_created": datetime.now().isoformat()
            }
            
            crm_file = os.path.join(BASE_DIR, "crm_database.json")
            data = {"leads": []}
            if os.path.exists(crm_file):
                try:
                    with open(crm_file, "r", encoding="utf-8") as f:
                        data = json.load(f)
                except Exception as e:
                    print("Error reading CRM file:", e)
            
            data.setdefault("leads", []).append(new_lead)
            try:
                with open(crm_file, "w", encoding="utf-8") as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)
            except Exception as e:
                print("Error writing CRM file:", e)
                self.send_response(500)
                self.send_cors_headers()
                self.end_headers()
                self.wfile.write(b"Error saving data")
                return
                
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_cors_headers()
            self.end_headers()
            self.wfile.write(json.dumps(new_lead).encode("utf-8"))
        elif self.path == "/api/ideas":
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            try:
                new_ideas = json.loads(post_data.decode("utf-8"))
            except Exception as e:
                self.send_response(400)
                self.send_cors_headers()
                self.end_headers()
                self.wfile.write(b"Invalid JSON")
                return
            
            ideas_file = os.path.join(BASE_DIR, "ideas_database.json")
            try:
                with open(ideas_file, "w", encoding="utf-8") as f:
                    json.dump(new_ideas, f, indent=2, ensure_ascii=False)
            except Exception as e:
                print("Error writing ideas file:", e)
                self.send_response(500)
                self.send_cors_headers()
                self.end_headers()
                self.wfile.write(b"Error saving data")
                return
            
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_cors_headers()
            self.end_headers()
            self.wfile.write(json.dumps({"status": "success"}).encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()

    def do_DELETE(self):
        if self.path.startswith("/api/crm/leads"):
            import urllib.parse
            parsed = urllib.parse.urlparse(self.path)
            params = urllib.parse.parse_qs(parsed.query)
            lead_id = params.get("id", [None])[0]
            if not lead_id:
                parts = parsed.path.split("/")
                if len(parts) > 4:
                    lead_id = parts[4]
            
            if not lead_id:
                self.send_response(400)
                self.send_cors_headers()
                self.end_headers()
                self.wfile.write(b"Missing ID")
                return
                
            crm_file = os.path.join(BASE_DIR, "crm_database.json")
            data = {"leads": []}
            if os.path.exists(crm_file):
                try:
                    with open(crm_file, "r", encoding="utf-8") as f:
                        data = json.load(f)
                except Exception as e:
                    print("Error reading CRM file:", e)
            
            leads = data.get("leads", [])
            initial_len = len(leads)
            data["leads"] = [p for p in leads if p["id"] != lead_id]
            
            if len(data["leads"]) == initial_len:
                self.send_response(404)
                self.send_cors_headers()
                self.end_headers()
                self.wfile.write(b"Lead not found")
                return
                
            try:
                with open(crm_file, "w", encoding="utf-8") as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)
            except Exception as e:
                print("Error writing CRM file:", e)
                self.send_response(500)
                self.send_cors_headers()
                self.end_headers()
                self.wfile.write(b"Error saving data")
                return
                
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_cors_headers()
            self.end_headers()
            self.wfile.write(json.dumps({"status": "success"}).encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()

def run():
    server_class = http.server.HTTPServer
    if hasattr(http.server, "ThreadingHTTPServer"):
        server_class = http.server.ThreadingHTTPServer
        
    with server_class(("", 5000), MetricsHandler) as httpd:
        print("Server backend running at http://localhost:5000")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server...")

if __name__ == "__main__":
    run()
