#!/usr/bin/python3
""" Flask Application """
from models import storage
from api.v1.views import app_views
from os import environ
from flask import Flask, render_template, make_response, jsonify
from flask_cors import CORS
from flasgger import Swagger
from flasgger.utils import swag_from


def pascal_triangle(n):
    pascal = []
    if n <= 0:
        return pascal
    n = 5
    for row in range(1,n+1):
        i = []
        for col in range(1,row+1):
            if col == 1:
                i += [1]
            else:
                try:
                    i += [ pascal[row-2][col-1]+pascal[row-2][col-2] ]
                except:
                    i += [1]
        pascal += [i]
    return pascal

if __name__ == "__main__":
    pascal_triangle(0)
