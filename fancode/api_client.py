from playwright.sync_api import sync_playwright

class APIClient:
    BASE_URL = "https://jsonplaceholder.typicode.com/"

    def __init__(self):
        self.playwright = sync_playwright().start()
        self.context = self.playwright.request.new_context()
    
    def get_users(self):
        response = self.context.get(f'{APIClient.BASE_URL}users')
        # response.raise_for_status()
        return response.json()
    
    def get_todos(self):
        response = self.context.get(f'{APIClient.BASE_URL}todos')
        # response.raise_for_status()
        return response.json()
    
    def close(self):
        self.context.dispose()
        self.playwright.stop()