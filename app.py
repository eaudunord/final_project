import numpy as np
from config import password
from config import username
import psycopg2
# import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify, render_template

from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("Causes").getOrCreate()