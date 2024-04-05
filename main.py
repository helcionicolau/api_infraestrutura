from fastapi import FastAPI
from views.index import index_router


app = FastAPI(
    docs_url="/api/v2/docs",
    redoc_url="/api/v2/redocs",
    title="API MAXALERTS",
    description="BASE DE DADOS PRINCIPAL",
    version="2.0",
    openapi_url="/api/v2/openapi.json",
    swagger_ui_parameters={"syntaxHighlight.theme": "monokai"}
)

app.include_router(index_router, prefix='/api')

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)