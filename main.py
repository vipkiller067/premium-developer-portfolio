from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="Vaibhav Pandey - Developer Portfolio")

# Mount static folder for CSS, JS, Images, and Assets
app.mount("/static", StaticFiles(directory="static"), name="static")

# Mount templates folder
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def home(request: Request):
    """
    Renders the single-page hybrid portfolio.
    All sections (About, Skills, Portfolio, Contact, etc.) are embedded here.
    """
    return templates.TemplateResponse("index.html", {"request": request})
