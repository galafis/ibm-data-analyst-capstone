#!/usr/bin/env python3
import pandas as pd
import pyodbc

class SQLAnalyzer:
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.connection = None

    def connect(self):
        self.connection = pyodbc.connect(self.connection_string)

    def execute_query(self, query):
        return pd.read_sql(query, self.connection)
