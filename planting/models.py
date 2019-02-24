from django.db import models

# Create your models here.

#-----User Model-----#
class User(models.Model):
	name = models.CharField(max_length=300, blank=True, null=True)
	
	class Meta:
		managed = True
		db_table = 'user'
		
	def __str__(self):
		return self.name

#-----Yards Model-----#
class Yards(models.Model):
	plant = models.ForeignKey('Plant', on_delete=models.CASCADE, blank=True, null=True)
	user = models.ForeignKey('User', on_delete=models.CASCADE, blank=True, null=True)
	
	class Meta:
		managed = True
		db_table = 'yard'


#-----Layer Model-----#
class Layer(models.Model):
	value = models.CharField(max_length=300, blank=True, null=True)

	class Meta:
		managed = True
		db_table = 'layer'

	def __str__(self):
		return self.value


#-----EcosystemRelationshipProperty (ERP)-----#
class EcosystemRelationshipProperty(models.Model):
	attribute = models.CharField(max_length = 300)

	class Meta:
		managed = True
		db_table = 'ecosystemRelationshipProperty'

	def __str__(self):
		return self.attribute


#-----EcosystemRelationshipValue (ERV)-----#
class EcosystemRelationshipValue(models.Model):
	value = models.CharField(max_length=50, blank=True, null=True)

	class Meta:
		managed = True
		db_table = "ecosystemRelationshipValue"
		
	def __str__(self):
		return self.value


#-----HumanUseProperty Model-----#
class HumanUseProperty(models.Model):
	attribute = models.CharField(max_length=300, blank=True, null=True)

	class Meta:
		managed = True
		db_table = 'humanUseProperty'
	
	def __str__(self):
		return self.attribute




#-----PlantEcosystemRelationship Model-----#
class PlantEcosystemRelationship(models.Model):
	plant = models.ForeignKey('Plant', on_delete=models.CASCADE, blank=True, null=True)
	ecosystemRelationshipProperty = models.ForeignKey('EcosystemRelationshipProperty', on_delete=models.CASCADE, blank=True, null=True)
	ecosystemRelationshipValue = models.ForeignKey('EcosystemRelationshipValue', on_delete=models.CASCADE, blank=True, null=True)

	class Meta:
		managed = True
		db_table = 'plantEcosystemRelationship'



#-----Plant Human Use---#
class PlantHumanUse (models.Model):
	plant = models.ForeignKey('Plant', on_delete=models.CASCADE, blank=True, null=True)
	human_use_property_id = models.ForeignKey('HumanUseProperty', on_delete=models.CASCADE, blank=True, null=True)

	class Meta:
		managed = True
		db_table = "plantHumanUse"



#-----Plant Model-----#
class Plant(models.Model):
	name = models.CharField(max_length=300, blank=True, null=True)
	layer = models.ForeignKey('Layer', on_delete=models.CASCADE, blank=True, null=True)
	imgURL = models.URLField(blank=True, null=True)

	class Meta:
		managed = True
		db_table = 'plant'
