from django.db import models

# Create your models here.

#---Plant Model-----#
class Plant(models.Model):
	name = models.CharField(max_length=300, blank=True, null=True)
	layer = models.ForeignKey('Layer', on_delete=models.CASCADE, blank=True, null=True)

	class Meta:
		managed = True
		db_table = 'plant'

class Layer(models.Model):
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'layer'

    def __str__(self):
        return self.value

#Plant Human Uses
class PlantHumanUses (models.Model):
        plant_id = models.ForeignKey('Plant', on_delete=models.CASCADE, blank=True, null=True)
        human_use_property_id = models.ForeignKey('HumanUseProperty', on_delete=models.CASCADE, blank=True, null=True)

         class Meta:
		managed = True
		db_table = 'plantHumanUses'               
