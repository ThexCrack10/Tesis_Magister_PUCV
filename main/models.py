from django.db import models

class RubroComercio (models.Model): 
    nombreRubro = models.TextField(default='')
    #FOREING KEY    
        #NO HAY POR AHORA
    #MUESTRA TEXTO ENTENDIBLE
    def __str__ (self):
        return self.nombreRubro 

class Comercio (models.Model): 
    nombreComercio  = models.TextField(default='')
    #FOREING KEY
    rubroId = models.ForeignKey(RubroComercio, on_delete=models.CASCADE)
    #MUESTRA TEXTO ENTENDIBLE
    def __str__ (self):
        return self.nombreComercio

class Sucursal (models.Model): 
    nombreSucursal  = models.TextField(default='')
    direccionSucursal  = models.TextField(default='')
    paisSucursal  = models.TextField(default='')
    #FOREING KEY
    comercioId = models.ForeignKey(Comercio, on_delete=models.CASCADE)
    #MUESTRA TEXTO ENTENDIBLE
    def __str__ (self):
        return "Sucursal %s : de %s " % (self.nombreSucursal, self.paisSucursal)

# ESTE FUNCIONA
class Producto (models.Model): 
    nombreProducto = models.TextField(default='')
    descripcionProducto = models.TextField(default='')  
    tipoProducto = models.TextField(default='')         #SI ES COMIDA, REMEDIO, ETC
    #FOREING KEY
        #NO HAY POR AHORA
    #MUESTRA TEXTO ENTENDIBLE
    def __str__ (self):
        return self.nombreProducto 

class Precio (models.Model): 
    tipoPrecio = models.TextField(default='')           #PUEDE SER PRECIO INTERNET O PRECIO EN TIENDA
    valorPrecio = models.TextField(default='')                 #CANTIDAD, VALOR
    #FOREING KEY
    sucursalId = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    productoId = models.ForeignKey(Producto, on_delete=models.CASCADE)
    #MUESTRA TEXTO ENTENDIBLE
    def __str__ (self):
        return "Precio %s: de %s" % (self.valorPrecio, self.productoId)

class Categoria (models.Model): 
    #IdCategoria = models.IntegerField()
    nombreCategoria = models.TextField(default='')
    descripcionCategoria = models.TextField(default='')
    categoriaPadreFlag = models.BooleanField(default=0)
    #categoriaPadre = models.IntegerField()
    #FOREING KEY
        #NO HAY POR AHORA
    #MUESTRA TEXTO ENTENDIBLE
    def __str__ (self):
        return self.nombreCategoria

class CategoriaProducto (models.Model): 
    #FOREING KEY
    categoriaId = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    productoId = models.ForeignKey(Producto, on_delete=models.CASCADE)
    #MUESTRA TEXTO ENTENDIBLE
    def __str__ (self):
        return "%s de %s" % (self.productoId, self.categoriaId)

class Caracteristica (models.Model): 
    nombreCaracteristica = models.TextField(default='')
    #FOREING KEY
        #NO HAY POR AHORA
    #MUESTRA TEXTO ENTENDIBLE
    def __str__ (self):
        return self.nombreCaracteristica

class CaracteristicaProducto (models.Model):
    valorCaracteristica = models.TextField(default='')
    #FOREING KEY
    caracteristicaId = models.ForeignKey(Caracteristica, on_delete=models.CASCADE)
    productoId = models.ForeignKey(Producto, on_delete=models.CASCADE)
    #MUESTRA TEXTO ENTENDIBLE
    def __str__ (self):
        return "Característica %s: %s de %s" % (self.caracteristicaId, self.valorCaracteristica, self.productoId)
    
class UnidadDeMedida (models.Model): 
    nombreMedida = models.TextField(default='')
    #FOREING KEY
        #NO HAY POR AHORA
    #MUESTRA TEXTO ENTENDIBLE
    def __str__ (self):
        return self.nombreMedida 

class ValorMedida (models.Model): 
    valorUnidadMedida = models.TextField(default='')
    #FOREING KEY
    unidadId = models.ForeignKey(UnidadDeMedida, on_delete=models.CASCADE)
    productoId = models.ForeignKey(Producto, on_delete=models.CASCADE)
    #MUESTRA TEXTO ENTENDIBLE
    def __str__ (self):
        return "%s %s(s) de %s" % (self.valorUnidadMedida, self.unidadId, self.productoId)

class TipoCodigo (models.Model): 
    nombreCodigo = models.TextField(default='')
    #FOREING KEY
        #NO HAY POR AHORA
    def __str__ (self):
        return self.nombreCodigo 

class CodigoProducto (models.Model):    
    valorCodigo = models.TextField(default='')
    #FOREING KEY
    codigoId = models.ForeignKey(TipoCodigo, on_delete=models.CASCADE)
    productoId = models.ForeignKey(Producto, on_delete=models.CASCADE)
    #MUESTRA TEXTO ENTENDIBLE
    def __str__ (self):
        #return "%s Codigo: %s de %s" % (self.valorCodigo, self.productoId)
        return "Codigo %s: %s de %s" % (self.codigoId, self.valorCodigo, self.productoId)