"""
PROJECT: COVID19-API
DESCRIPTION: Daily level information on various cases
AUTHOR: Nuttaphat Arunoprayoch
DATE: 9-Feb-2020
RUN SERVER: uvicorn main:app --reload
"""
# Import libraries
import sys
from functools import wraps
from typing import Dict, Any

from fastapi import FastAPI, HTTPException
from starlette.requests import Request
from starlette.responses import RedirectResponse
from starlette.middleware.cors import CORSMiddleware

from routers.v1 import v1
from routers.v2 import v2

# Setup application
app = FastAPI(
    title='COVID-19 API',
    description='Simply FAST API for COVID-19 cases exploration',
    version='2.0.0'
)

# Setup CORS (https://fastapi.tiangolo.com/tutorial/cors/)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


"""
SECTION: Default route
DESCRIPTION: Route to API documentation
"""
# API documentation
@app.get('/', include_in_schema=False)
def read_docs() -> None:
    """ API documentation """
    return RedirectResponse(url='/docs')


"""
SECTION: API v2
DESCRIPTION: New API (v2)
DATE: 14-March-2020
"""
app.include_router(v2, prefix="/v2", tags=["v2"])


"""
SECTION: API v1
REMARK: No further improvement intended unless necessary
"""
app.include_router(v1, prefix="", tags=["v1"])
