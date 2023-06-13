from fastapi import FastAPI
import uvicorn
app = FastAPI()


@app.get("/add")
async def add(operand_1: float, operand_2: float):
    return operand_1+operand_2


@app.get("/sub")
async def sub(operand_1: float, operand_2: float):
    return operand_1-operand_2


@app.get("/mul")
async def mul(operand_1: float, operand_2: float):
    return operand_1*operand_2


@app.get("/div")
async def div(operand_1: float, operand_2: float):
    try:
        return operand_1/operand_2

    except ZeroDivisionError:
        print("Exception caught")








