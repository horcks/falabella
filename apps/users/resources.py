from import_export import resources
from apps.users.models import *

from import_export.fields import Field

# Register your models here.
          

class UserExportResource(resources.ModelResource):
	class Meta: 
		model = Extended_User
		fields = (
			'id',
			'user',
			'user__username',
			'document_number',
			'phone1',
			'phone2',
			'address',
			'document_type__name',
			'date_birth',
			'description_address',
			'gender__name',
			)
		