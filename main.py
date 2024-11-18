from fastapi import FastAPI, UploadFile, File, HTTPException
import pandas as pd
import io

app = FastAPI()

# Endpoint para ler o arquivo CSV
@app.post("/ler_csv")
async def ler_csv(file: UploadFile = File(...)):
    try:
        # Ler o arquivo CSV enviado
        contents = await file.read()
        df = pd.read_csv(io.StringIO(contents.decode("utf-8")))

        # Retornar as primeiras 5 linhas do CSV como exemplo
        return df.head().to_dict(orient="records")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao ler o arquivo CSV: {str(e)}")
