"""
Configuração do banco de dados para o projeto IBM Data Analyst Capstone
Contém configurações para PostgreSQL, SQL Server e SQLite
"""

import os
from typing import Dict, Any
from dataclasses import dataclass
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine

@dataclass
class DatabaseConfig:
    """
    Classe de configuração para conexões de banco de dados
    """
    host: str
    port: int
    database: str
    username: str
    password: str
    driver: str = 'postgresql'
    
    def get_connection_string(self) -> str:
        """Gera string de conexão baseada no driver"""
        if self.driver == 'postgresql':
            return f"postgresql://{self.username}:{self.password}@{self.host}:{self.port}/{self.database}"
        elif self.driver == 'sqlserver':
            return f"mssql+pyodbc://{self.username}:{self.password}@{self.host}:{self.port}/{self.database}?driver=ODBC+Driver+17+for+SQL+Server"
        elif self.driver == 'sqlite':
            return f"sqlite:///{self.database}"
        else:
            raise ValueError(f"Driver não suportado: {self.driver}")

# Configurações para diferentes ambientes
DATABASE_CONFIGS = {
    'development': DatabaseConfig(
        host=os.getenv('DB_HOST', 'localhost'),
        port=int(os.getenv('DB_PORT', '5432')),
        database=os.getenv('DB_NAME', 'analytics_dev'),
        username=os.getenv('DB_USER', 'analyst'),
        password=os.getenv('DB_PASSWORD', 'dev_password'),
        driver='postgresql'
    ),
    
    'production': DatabaseConfig(
        host=os.getenv('PROD_DB_HOST', 'prod-server.com'),
        port=int(os.getenv('PROD_DB_PORT', '5432')),
        database=os.getenv('PROD_DB_NAME', 'analytics_prod'),
        username=os.getenv('PROD_DB_USER', 'prod_analyst'),
        password=os.getenv('PROD_DB_PASSWORD', 'secure_prod_password'),
        driver='postgresql'
    ),
    
    'test': DatabaseConfig(
        host='localhost',
        port=5433,
        database='analytics_test',
        username='test_user',
        password='test_password',
        driver='postgresql'
    ),
    
    'sqlserver': DatabaseConfig(
        host=os.getenv('SQL_SERVER_HOST', 'localhost'),
        port=int(os.getenv('SQL_SERVER_PORT', '1433')),
        database=os.getenv('SQL_SERVER_DB', 'Analytics'),
        username=os.getenv('SQL_SERVER_USER', 'sa'),
        password=os.getenv('SQL_SERVER_PASSWORD', 'SqlServerPass123'),
        driver='sqlserver'
    ),
    
    'sqlite': DatabaseConfig(
        host='',
        port=0,
        database=os.path.join(os.path.dirname(__file__), '..', 'data', 'analytics.db'),
        username='',
        password='',
        driver='sqlite'
    )
}

# Configuração atual baseada em variável de ambiente
CURRENT_ENV = os.getenv('ENVIRONMENT', 'development')
CURRENT_CONFIG = DATABASE_CONFIGS.get(CURRENT_ENV, DATABASE_CONFIGS['development'])

# Parâmetros de conexão do SQLAlchemy
CONNECTION_PARAMS = {
    'pool_size': 10,
    'max_overflow': 20,
    'pool_timeout': 30,
    'pool_recycle': 3600,
    'echo': os.getenv('SQL_ECHO', 'False').lower() == 'true'
}

def get_engine(config: DatabaseConfig = None) -> Engine:
    """
    Cria engine do SQLAlchemy para conexão com banco de dados
    
    Args:
        config: Configuração do banco (usa CURRENT_CONFIG se não fornecida)
        
    Returns:
        Engine do SQLAlchemy configurada
    """
    if config is None:
        config = CURRENT_CONFIG
    
    connection_string = config.get_connection_string()
    
    if config.driver == 'sqlite':
        # SQLite não suporta pool de conexões
        return create_engine(connection_string, echo=CONNECTION_PARAMS['echo'])
    else:
        return create_engine(connection_string, **CONNECTION_PARAMS)

def test_connection(config: DatabaseConfig = None) -> bool:
    """
    Testa conexão com banco de dados
    
    Args:
        config: Configuração do banco (usa CURRENT_CONFIG se não fornecida)
        
    Returns:
        True se conexão bem-sucedida, False caso contrário
    """
    try:
        engine = get_engine(config)
        with engine.connect() as conn:
            conn.execute("SELECT 1")
        return True
    except Exception as e:
        print(f"Erro na conexão: {e}")
        return False

def get_database_info(config: DatabaseConfig = None) -> Dict[str, Any]:
    """
    Retorna informações sobre o banco de dados
    
    Args:
        config: Configuração do banco (usa CURRENT_CONFIG se não fornecida)
        
    Returns:
        Dicionário com informações do banco
    """
    if config is None:
        config = CURRENT_CONFIG
    
    return {
        'driver': config.driver,
        'host': config.host,
        'port': config.port,
        'database': config.database,
        'username': config.username,
        'connection_string': config.get_connection_string().replace(config.password, '***'),
        'environment': CURRENT_ENV
    }

# Configurações específicas para análise de dados
ANALYTICS_TABLES = {
    'sales_data': 'sales',
    'customer_data': 'customers',
    'product_data': 'products',
    'financial_data': 'financial_records',
    'kpi_data': 'kpi_metrics',
    'reports': 'generated_reports'
}

# Configurações de query otimizada
QUERY_SETTINGS = {
    'default_limit': 10000,
    'max_limit': 100000,
    'timeout_seconds': 300,
    'enable_query_cache': True,
    'cache_duration': 3600  # 1 hora
}

# Configurações de backup e manutenção
MAINTENANCE_CONFIG = {
    'backup_enabled': True,
    'backup_schedule': '0 2 * * *',  # Todo dia às 2h
    'backup_retention_days': 30,
    'auto_vacuum': True,
    'analyze_tables': True,
    'log_slow_queries': True,
    'slow_query_threshold': 5.0  # segundos
}

if __name__ == '__main__':
    # Teste rápido da configuração
    print("=== Configuração do Banco de Dados ===")
    print(f"Ambiente atual: {CURRENT_ENV}")
    print(f"Configuração: {get_database_info()}")
    print(f"Testando conexão... ", end='')
    
    if test_connection():
        print("✅ Sucesso!")
    else:
        print("❌ Falhou!")
        print("Verifique as configurações e variáveis de ambiente.")
