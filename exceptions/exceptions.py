
class SumsNeighborsException(Exception):
    
    def __init__(self, *args):
        super().__init__("La suma de de vecinos da como resultado un valor igual que cero.\
                         Un posible motivo puede ser que no se cuenta con obervaciones replicadas")

class NotFoundParameterExtraException(Exception):
    
    def __init__(self, _nameParameter, _nameFunction, *args):
        super().__init__("Imposible de efectuar la operación "+str(_nameFunction)+
                         ", no se encontró el parametro "+_nameParameter)
        
class NotMeasurementDuplicadasException(Exception):
    
    def __init__(self, _nameFunction, *args):
        super().__init__("No se pudo efectuar la operación "+_nameFunction+". No existen observaciones duplicadas.")
        
class EstadigrafoFisherCalFOException(Exception):
    
    def __init__(self, *args):
        super().__init__("Imposible determinar el Estadígrafo de Fisher Calculado por una de las siguientes posibles razones:\n- No se cuenta con con observaciones replicadas.\n\n")
        
class RelationFOFTException(Exception):
    
    def __init__(self, *args):
        super().__init__("Imposible determinar la relación entre el Estadígrafo de Fisher Calculado y el Estadígrafo de Fisher Tabulado por una de las siguientes posibles razones:\n- No se cuenta con con observaciones replicadas.\n\n")

class VariableNotFoundDataFrame(Exception):
    
    def __init__(self, _nameVar,*args):
        super().__init__("No se encontro una columna con nombre "+_nameVar+" en la tabla de datos")