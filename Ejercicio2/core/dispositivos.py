"""Clases de dispositivos del catálogo"""

#from dataclasses import dataclass, field, InitVar
from core.excepciones import StockInvalidoError

#@dataclass
class DispositivoEcologico:
    
    """ Clase base 
    
    modelo: str
    precio: float
    stock: InitVar[int] = 0
    _stock: int = field(default=0, repr=False, init=False)
    """
    
    def __init__(self, modelo: str, precio: float, stock: int = 0) -> None:
        self.modelo = modelo
        self.precio = precio
        self._stock = 0
        self.stock = stock
    
    @property
    def stock(self) -> int:
        """Setter que no acepta negativos
        """
        return self._stock
    
    @stock.setter
    def stock(self, valor: int) -> None:
        if not isinstance(valor, int):
            raise StockInvalidoError(valor)
        if valor < 0:
            raise StockInvalidoError(valor)
        self._stock = valor
    
    def ficha_tecnica(self) -> str:
        """Ficha técnica, para subclases"""
        return (
            f"Modelo: {self.modelo}\n"
            f"Precio: ${self.precio:.2f}\n"
            f"Stock: {self.stock} unidades"
        )
    
    
    """def __post_init__(self, stock:int) -> None:
        Valida stock - Pruebo solución InitVar por problema atributo privado de stock
        self.stock = self._stock
        
    @property
    def stock(self) -> int:
        Getter
        
        return self._stock
    
    @stock.setter
    def stock(self, valor: int) -> None:
        if not isinstance(valor, int):
            raise StockInvalidoError(valor)
        if valor < 0:
            raise StockInvalidoError(valor)
        self._stock = valor
                
        
    def ficha_tecnica(self) -> str:
        Ficha técnica genérica
        return (
            f"Modelo: {self.modelo}\n"
            f"Precio:${self.precio:.2f}\n"
            f"Stock: {self.stock} unidades"
        )
        
@dataclass"""
class PanelSolar(DispositivoEcologico):
    """ Hereda de la clase base y agrega atributos"""
    def __init__(
        self,
        modelo: str,
        precio: float,
        stock: int = 0,
        potencia_w: float = 0.0, 
        eficiencia: float = 0.0,
        ) -> None:
        
        super().__init__(modelo, precio, stock)
        self.potencia_w = potencia_w
        self.eficiencia = eficiencia
    
def ficha_tecnica(self) -> str:
    """ Incluye atributos del panel"""
    
    base = super().ficha_tecnica()
    return(
        f"{base}\n"
        f"Potencia: {self.potencia_W} W\n"
        f"Eficiencia: {self.eficiencia}%"
    )
    