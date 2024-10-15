# This is an auto-generated Django model module.

# You'll have to do the following manually to clean this up:

#   * Rearrange models' order

#   * Make sure each model has one field with primary_key=True

#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior

#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table

# Feel free to rename the models, but don't rename db_table values or field names.

from django.db import models





class Categoria(models.Model):

    nombre = models.CharField(max_length=45)



    class Meta:

        managed = False

        db_table = 'categoria'





class Cliente(models.Model):

    nit = models.CharField(db_column='NIT', max_length=45)  # Field name made lowercase.

    nombre = models.CharField(db_column='Nombre', max_length=50)  # Field name made lowercase.

    direccion = models.CharField(db_column='Direccion', max_length=50, blank=True, null=True)  # Field name made lowercase.

    telefono = models.CharField(db_column='Telefono', max_length=11, blank=True, null=True)  # Field name made lowercase.



    class Meta:

        managed = False

        db_table = 'cliente'





class Compra(models.Model):

    fecha = models.DateTimeField(blank=True, null=True)

    total = models.FloatField(db_column='Total')  # Field name made lowercase.

    id_proveedor = models.ForeignKey('Proveedor', models.DO_NOTHING, db_column='ID_Proveedor')  # Field name made lowercase.

    usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usuario')



    class Meta:

        managed = False

        db_table = 'compra'





class DetalleCompra(models.Model):

    compra_numero = models.ForeignKey(Compra, models.DO_NOTHING, db_column='compra_numero')

    id_producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='id_Producto')  # Field name made lowercase.

    cantidad = models.IntegerField(db_column='Cantidad')  # Field name made lowercase.

    precio_unitario = models.FloatField(db_column='Precio_unitario')  # Field name made lowercase.

    precio_por_mayor = models.FloatField(db_column='Precio por Mayor')  # Field name made lowercase. Field renamed to remove unsuitable characters.



    class Meta:

        managed = False

        db_table = 'detalle_compra'





class DetalleVenta(models.Model):

    id_factura = models.ForeignKey('Factura', models.DO_NOTHING, db_column='ID_Factura')  # Field name made lowercase.

    id_producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='id_Producto')  # Field name made lowercase.

    cantidad = models.IntegerField(db_column='Cantidad')  # Field name made lowercase.

    precio_unitario = models.FloatField(db_column='Precio_Unitario')  # Field name made lowercase.

    sub_total = models.FloatField(db_column='Sub_Total')  # Field name made lowercase.



    class Meta:

        managed = False

        db_table = 'detalle_venta'





class Empleado(models.Model):

    id_empleado = models.IntegerField(db_column='ID_Empleado', primary_key=True)  # Field name made lowercase.

    nit = models.CharField(max_length=45)

    nombre = models.CharField(db_column='Nombre', max_length=50)  # Field name made lowercase.

    apellido = models.CharField(db_column='Apellido', max_length=50, blank=True, null=True)  # Field name made lowercase.

    usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usuario')



    class Meta:

        managed = False

        db_table = 'empleado'





class Factura(models.Model):

    id_factura = models.AutoField(db_column='ID_Factura', primary_key=True)  # Field name made lowercase. The composite primary key (ID_Factura, cliente_id) found, that is not supported. The first column is selected.

    fecha = models.DateTimeField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.

    descripcion = models.CharField(db_column='Descripcion', max_length=50)  # Field name made lowercase.

    total = models.FloatField(db_column='Total')  # Field name made lowercase.

    usuario_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usuario_Usuario')  # Field name made lowercase.

    cliente = models.ForeignKey(Cliente, models.DO_NOTHING)



    class Meta:

        managed = False

        db_table = 'factura'

        unique_together = (('id_factura', 'cliente'),)





class Producto(models.Model):

    id_producto = models.IntegerField(db_column='ID_Producto', primary_key=True)  # Field name made lowercase.

    codigo_de_barras = models.CharField(max_length=13, blank=True, null=True)

    nombre = models.CharField(db_column='Nombre', max_length=50)  # Field name made lowercase.

    descripcion = models.TextField(db_column='Descripcion')  # Field name made lowercase.

    precio = models.FloatField(db_column='Precio')  # Field name made lowercase.

    existencia = models.IntegerField(db_column='Existencia')  # Field name made lowercase.

    categoria = models.ForeignKey(Categoria, models.DO_NOTHING)

    tipo_producto = models.ForeignKey('TipoProducto', models.DO_NOTHING)



    class Meta:

        managed = False

        db_table = 'producto'





class Proveedor(models.Model):

    id_proveedor = models.AutoField(db_column='ID_Proveedor', primary_key=True)  # Field name made lowercase.

    nit = models.CharField(max_length=45, blank=True, null=True)

    nombre = models.CharField(max_length=45, blank=True, null=True)

    direccion = models.TextField(db_column='Direccion', blank=True, null=True)  # Field name made lowercase.

    telefono = models.CharField(max_length=8, blank=True, null=True)

    categoria = models.CharField(db_column='Categoria', max_length=50)  # Field name made lowercase.



    class Meta:

        managed = False

        db_table = 'proveedor'





class TipoProducto(models.Model):

    nombre = models.CharField(max_length=45)



    class Meta:

        managed = False

        db_table = 'tipo_producto'





class Usuario(models.Model):

    usuario = models.CharField(db_column='Usuario', primary_key=True, max_length=50)  # Field name made lowercase.

    password = models.CharField(db_column='Password', max_length=50)  # Field name made lowercase.



    class Meta:

        managed = False

        db_table = 'usuario'

