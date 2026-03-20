from enum import Enum

class UserType(str, Enum):
    CONSTRUTORA = "CONSTRUTORA"
    CORRETOR = "CORRETOR"

class PropertyType(str, Enum):
    APARTAMENTO = "APARTAMENTO"
    CASA = "CASA"
    COBERTURA = "COBERTURA"
    SOBRADO = "SOBRADO"
    LOFT = "LOFT"
    TERRENO = "TERRENO"
    COMERCIAL = "COMERCIAL"

class TransactionType(str, Enum):
    VENDA = "VENDA"
    ALUGUEL = "ALUGUEL"
    TEMPORADA = "TEMPORADA"

class ProposalStatus(str, Enum):
    PENDENTE = "PENDENTE"
    EM_NEGOCIACAO = "EM_NEGOCIACAO"
    ACEITA = "ACEITA"
    RECUSADA = "RECUSADA"

class PaymentType(str, Enum):
    A_VISTA = "A_VISTA"
    FINANCIAMENTO = "FINANCIAMENTO"
    PERMUTA = "PERMUTA"
    OUTRO = "OUTRO"

class EnterpriseStatus(str, Enum):
    LANCAMENTO = "LANCAMENTO"
    EM_CONSTRUCAO = "EM_CONSTRUCAO"
    PRONTO = "PRONTO"

class UnitStatus(str, Enum):
    DISPONIVEL = "DISPONIVEL"
    RESERVADO = "RESERVADO"
    VENDIDO = "VENDIDO"