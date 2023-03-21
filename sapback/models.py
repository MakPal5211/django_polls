from django.db import models


class MaterialGeneral(models.Model):
    createdon = models.DateField(verbose_name='Created On', max_length=8)
    createdat = models.TimeField(verbose_name='Created At', max_length=6)
    createdby = models.CharField(verbose_name='Name of person responsible for creating object', max_length=12)
    lastchangedate = models.TimeField(verbose_name='Date of last change', max_length=6)
    lastchangedby = models.CharField(verbose_name='Name of person who changed the object', max_length=12)
    maintenacestatus = models.CharField(verbose_name='Maintenance Status', max_length=15)
    materialnumber = models.CharField(verbose_name='Material Number', max_length=40)
    materialdelind = models.CharField(verbose_name='Material Deletion at the client level', max_length=1)
    materialtype = models.CharField(verbose_name='Material Type', max_length=4)
    baseuom = models.CharField(verbose_name='Base Unit of Measure', max_length=3)
    oldmaterialnumber = models.CharField(verbose_name='Old Material Number', max_length=40)
    crossplantmaterialstatus = models.CharField(verbose_name='X-Plant Material Status', max_length=2)
    crossplantmaterialstatusvalidfrom = models.DateField(verbose_name='Material Status Valid From', max_length=8)
    materialgroup = models.CharField(verbose_name='Material Group', max_length=9)
    producthierarchy = models.CharField(verbose_name='Product Hierarchy', max_length=18)
    crossplantgeneralitemcategorygroup = models.CharField(verbose_name='General Item Category Group', max_length=4)
    grossweight = models.DecimalField(verbose_name='Gross Weight', max_digits=13, decimal_places=3)
    netweight = models.DecimalField(verbose_name='Net Weight', max_digits=13, decimal_places=3)
    volume = models.DecimalField(verbose_name='Volume', max_digits=13, decimal_places=3)
    weightunit = models.CharField(verbose_name='Weight Unit', max_length=3)
    volumeunit = models.CharField(verbose_name='Volume Unit', max_length=3)
    sizedimensions = models.CharField(verbose_name='Size/dimensions', max_length=32)
    eanupc = models.CharField(verbose_name='EAN/UPC', max_length=18)
    eancategory = models.CharField(verbose_name='EAN Category', max_length=2)
    crossplantbasicdatatext = models.TextField(verbose_name='Basic Data Text')


