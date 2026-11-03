"""Clase de excepcion"""


class StockInvalidoError(Exception):
    """ Se lanza con un stock negativo"""
    
    def __init__(self, valor_recibido: int) -> None:
        
        self.valor_recibido = valor_recibido
        
        mensaje = (
            f"Stock inválido: {valor_recibido}."
            f"  El stock debe ser un número entero"
        )
        
        super().__init__(mensaje)
    
    
