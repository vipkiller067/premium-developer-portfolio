# Vaibhav Pandey - Premium Developer Portfolio

A complete, production-ready developer portfolio dynamically served with a Python **FastAPI** backend and utilizing an ultra-premium dark-theme UI. This application is architected as a hybrid Single-Page Application (SPA), integrating cleanly separated components into a central entry point.

## 🚀 Features
- **High-Performance Backend**: Powered entirely by FastAPI and Uvicorn.
- **Classic Premium UI**: Pure CSS/Jinja implementation of a deep-dark theme (#020617 / #0f172a / #3b82f6), meticulously organized grid components, and precision hover mechanics.
- **Single-Page Hybrid Nav**: Robust custom JavaScript and CSS offset engine for perfectly butter-smooth scrolling and offset snapping directly behind the frosted glass navigation menu.
- **Recruiter Optimized Layouts**: Clean, readable Education & Experience grids, skill pill-badges, and dedicated Call To Action checkpoints.
- **Native SVGs**: High-resolution, mathematically constrained SVG icons for all platforms (GitHub, LeetCode, LinkedIn, Instagram).

## 📂 Project Structure

```
front/
│
├── main.py                # Core FastAPI Router executing Jinja template bridging
├── requirements.txt       # Python dependencies required to run the portal
├── README.md              # Project Documentation
│
├── static/                # Static mount boundary
│   ├── css/               # Core styles and design system overrides
│   ├── js/                # Client-Side javascript
│   ├── images/            # Assets, profile pics, and favicons
│   ├── Vaibhav_resume.pdf # Downloadable persistent document asset
│
└── templates/             # Server boundaries
    └── index.html         # Master Single-Page Template
```

## 🛠️ Installation & Setup

1. **Clone the repository** (or download the source code files).
2. **Install dependencies**: Ensure you have a working Python environment.
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the server** via Uvicorn in development mode:
   ```bash
   uvicorn main:app --reload
   ```
4. **View your Application**: Head over to [http://127.0.0.1:8000](http://127.0.0.1:8000)

## 📌 Technology Stack
- **Backend**: FastAPI, Python 3
- **Templating Engine**: Jinja2
- **Frontend Architecture**: Native HTML5, Deep Custom CSS, ES6 Javascript
- **Deployment Spec READY**: Optimized for 0ms cold-start and permanent continuous online configurations via platforms like Render.com.
