# -*- coding: utf-8 -*-
"""
Configuração de Relatórios Automatizados

Este módulo contém configurações para geração de relatórios automatizados
para análise de dados no projeto IBM Data Analyst Capstone.
"""

import os
from datetime import datetime, timedelta
from typing import Dict, List, Optional


class ReportConfig:
    """Configurações para geração de relatórios."""
    
    # Configurações gerais
    REPORT_OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'reports')
    TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), '..', 'templates')
    
    # Formatos de saída suportados
    SUPPORTED_FORMATS = ['html', 'pdf', 'excel', 'csv']
    DEFAULT_FORMAT = 'html'
    
    # Configurações de agendamento
    SCHEDULE_CONFIG = {
        'daily': {'hour': 6, 'minute': 0},
        'weekly': {'day': 'monday', 'hour': 8, 'minute': 0},
        'monthly': {'day': 1, 'hour': 9, 'minute': 0}
    }
    
    # Configurações de email
    EMAIL_CONFIG = {
        'enabled': False,
        'smtp_server': os.getenv('SMTP_SERVER', 'localhost'),
        'smtp_port': int(os.getenv('SMTP_PORT', '587')),
        'username': os.getenv('EMAIL_USERNAME', ''),
        'password': os.getenv('EMAIL_PASSWORD', ''),
        'from_address': os.getenv('EMAIL_FROM', 'noreply@company.com'),
        'use_tls': True
    }
    
    # Lista de destinatários padrão
    DEFAULT_RECIPIENTS = [
        'data-team@company.com',
        'analytics@company.com'
    ]


class ReportTemplates:
    """Templates disponíveis para relatórios."""
    
    DASHBOARD_TEMPLATE = {
        'name': 'Dashboard Executivo',
        'file': 'executive_dashboard.html',
        'description': 'Visão geral dos KPIs principais',
        'charts': ['line', 'bar', 'pie'],
        'frequency': 'daily'
    }
    
    SALES_TEMPLATE = {
        'name': 'Relatório de Vendas',
        'file': 'sales_report.html',
        'description': 'Análise detalhada das vendas',
        'charts': ['bar', 'trend', 'heatmap'],
        'frequency': 'weekly'
    }
    
    PERFORMANCE_TEMPLATE = {
        'name': 'Relatório de Performance',
        'file': 'performance_report.html',
        'description': 'Métricas de performance e benchmarks',
        'charts': ['gauge', 'bar', 'line'],
        'frequency': 'monthly'
    }
    
    CUSTOM_TEMPLATE = {
        'name': 'Relatório Customizado',
        'file': 'custom_report.html',
        'description': 'Template personalizável',
        'charts': ['any'],
        'frequency': 'on_demand'
    }


class DataSources:
    """Configuração das fontes de dados."""
    
    # Conexões de banco de dados
    DATABASE_CONNECTIONS = {
        'primary': {
            'type': 'postgresql',
            'host': os.getenv('DB_HOST', 'localhost'),
            'port': int(os.getenv('DB_PORT', '5432')),
            'database': os.getenv('DB_NAME', 'analytics'),
            'schema': 'public'
        },
        'warehouse': {
            'type': 'snowflake',
            'account': os.getenv('SNOWFLAKE_ACCOUNT', ''),
            'warehouse': os.getenv('SNOWFLAKE_WAREHOUSE', ''),
            'database': os.getenv('SNOWFLAKE_DATABASE', ''),
            'schema': os.getenv('SNOWFLAKE_SCHEMA', 'PUBLIC')
        }
    }
    
    # APIs externas
    API_ENDPOINTS = {
        'sales_api': {
            'base_url': os.getenv('SALES_API_URL', ''),
            'auth_token': os.getenv('SALES_API_TOKEN', ''),
            'timeout': 30
        },
        'marketing_api': {
            'base_url': os.getenv('MARKETING_API_URL', ''),
            'auth_token': os.getenv('MARKETING_API_TOKEN', ''),
            'timeout': 30
        }
    }
    
    # Arquivos de dados
    FILE_SOURCES = {
        'csv_files': os.path.join(os.path.dirname(__file__), '..', 'data', 'csv'),
        'excel_files': os.path.join(os.path.dirname(__file__), '..', 'data', 'excel'),
        'json_files': os.path.join(os.path.dirname(__file__), '..', 'data', 'json')
    }


class ChartConfig:
    """Configurações para gráficos e visualizações."""
    
    # Configurações de estilo
    STYLE_CONFIG = {
        'theme': 'professional',
        'color_palette': ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'],
        'font_family': 'Arial, sans-serif',
        'font_size': 12,
        'figure_size': (10, 6),
        'dpi': 300
    }
    
    # Tipos de gráfico disponíveis
    CHART_TYPES = {
        'line': 'Gráfico de Linha',
        'bar': 'Gráfico de Barras',
        'pie': 'Gráfico de Pizza',
        'scatter': 'Gráfico de Dispersão',
        'heatmap': 'Mapa de Calor',
        'histogram': 'Histograma',
        'boxplot': 'Box Plot',
        'gauge': 'Medidor',
        'trend': 'Análise de Tendência'
    }
    
    # Configurações específicas por tipo
    CHART_DEFAULTS = {
        'line': {'show_markers': True, 'line_width': 2},
        'bar': {'show_values': True, 'orientation': 'vertical'},
        'pie': {'show_percentages': True, 'explode_max': True},
        'heatmap': {'show_annotations': True, 'colormap': 'Blues'}
    }


class AlertConfig:
    """Configurações para alertas e notificações."""
    
    # Tipos de alerta
    ALERT_TYPES = {
        'threshold': 'Limite Ultrapassado',
        'anomaly': 'Anomalia Detectada',
        'data_quality': 'Problema na Qualidade dos Dados',
        'system_error': 'Erro no Sistema'
    }
    
    # Configurações de limites
    THRESHOLDS = {
        'revenue_drop': -0.10,  # 10% de queda na receita
        'data_freshness': 24,   # Dados com mais de 24 horas
        'error_rate': 0.05,     # Taxa de erro acima de 5%
        'response_time': 5.0    # Tempo de resposta acima de 5s
    }
    
    # Canais de notificação
    NOTIFICATION_CHANNELS = {
        'email': True,
        'slack': False,
        'sms': False,
        'webhook': False
    }


class SecurityConfig:
    """Configurações de segurança para relatórios."""
    
    # Configurações de acesso
    ACCESS_CONTROL = {
        'require_authentication': True,
        'session_timeout': 3600,  # 1 hora
        'max_failed_attempts': 3,
        'lockout_duration': 1800  # 30 minutos
    }
    
    # Configurações de criptografia
    ENCRYPTION = {
        'encrypt_sensitive_data': True,
        'encryption_algorithm': 'AES-256',
        'key_rotation_days': 90
    }
    
    # Configurações de auditoria
    AUDIT = {
        'log_access': True,
        'log_changes': True,
        'retention_days': 365
    }


# Função auxiliar para validar configurações
def validate_config() -> Dict[str, bool]:
    """Valida as configurações de relatório.
    
    Returns:
        Dict[str, bool]: Status da validação para cada seção
    """
    validation_results = {}
    
    # Validar diretórios
    validation_results['output_dir'] = os.path.exists(ReportConfig.REPORT_OUTPUT_DIR)
    validation_results['template_dir'] = os.path.exists(ReportConfig.TEMPLATE_DIR)
    
    # Validar configurações de email
    email_config = ReportConfig.EMAIL_CONFIG
    validation_results['email_config'] = all([
        email_config.get('smtp_server'),
        email_config.get('from_address')
    ]) if email_config.get('enabled') else True
    
    # Validar conexões de banco
    db_configs = DataSources.DATABASE_CONNECTIONS
    validation_results['database_config'] = all([
        config.get('host') and config.get('database')
        for config in db_configs.values()
    ])
    
    return validation_results


# Função para criar diretórios necessários
def setup_directories():
    """Cria os diretórios necessários para relatórios."""
    directories = [
        ReportConfig.REPORT_OUTPUT_DIR,
        ReportConfig.TEMPLATE_DIR,
        DataSources.FILE_SOURCES['csv_files'],
        DataSources.FILE_SOURCES['excel_files'],
        DataSources.FILE_SOURCES['json_files']
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
    
    print("Diretórios de relatório configurados com sucesso!")


if __name__ == '__main__':
    # Executar validações e setup quando o arquivo for executado diretamente
    print("Configurando sistema de relatórios...")
    setup_directories()
    
    validation = validate_config()
    print("\nStatus das validações:")
    for key, status in validation.items():
        print(f"  {key}: {'✓' if status else '✗'}")
    
    if all(validation.values()):
        print("\n✅ Todas as configurações foram validadas com sucesso!")
    else:
        print("\n⚠️  Algumas configurações precisam ser ajustadas.")
