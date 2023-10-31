from fastapi import APIRouter
from typing import Union

numeric = Union[int, float]

router = APIRouter()

@router.get('/')
def index():
    return {'status':  'OK'}

@router.get('/maths')
def sum_two_numbers(a : numeric, b : numeric) -> dict:
    return {f'{a} + {b} = ': a+b}