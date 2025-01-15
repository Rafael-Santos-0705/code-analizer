import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.docs import get_swagger_ui_html
from pyctuator.pyctuator import Pyctuator, Endpoints
from datetime import datetime
from utils import Policy, Environment
from routes import router_code_analizer, router_health

app = FastAPI(
    title= "Code Analyzer",
    description="Agente para sugestões de otimização de código Python",
    docs_url="/docs",
    redoc_url=None,
)

app.include_router(router_code_analizer)
app.include_router(router_health)
APPLICATION_URL = Environment.get("APPLICATION_URL")
allow_origins = Policy.origins(APPLICATION_URL)

app.add_middleware(
    CORSMiddleware,
    allow_origins=allow_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if APPLICATION_URL:
    Pyctuator(
        app,
        f"Monitoring {app.title} Service",
        app_url=APPLICATION_URL,
        pyctuator_endpoint_url=f"{APPLICATION_URL}",
        registration_url=None,
        metadata=dict(
            statup=datetime.now().date()
        ),
        disabled_endpoints=[
            Endpoints.ENV,
            Endpoints.THREAD_DUMP,
            Endpoints.LOGFILE
        ]
    )


