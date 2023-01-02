from typing import Optional
from django.db import models
from django.contrib.auth.models import User
from pydantic import BaseModel, Field, constr, conint, create_model


class Post(models.Model):
    build_status = models.IntegerField()
    is_active = models.BooleanField()
    start_month = models.DateTimeField()
    construction_type = models.IntegerField()
    date_diff = models.IntegerField()
    description = models.CharField(max_length=200)
    date_in = models.DateTimeField()
    property_type = models.IntegerField()
    end_week = models.IntegerField()
    typology_type = models.IntegerField()
    _id = models.BigIntegerField()
    coordinates = models.CharField(max_length=200)
    boundary_id = models.IntegerField()
    id_uda = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    listing_type = models.IntegerField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title + "\n" + self.description


class PropertyModel(BaseModel):
    build_status: conint(strict=True) = Field(...)
    is_active: bool = Field(...)
    start_month: constr(strict=True) = Field(...)
    construction_type: constr(strict=True) = Field(...)
    date_diff: conint(strict=True) = Field(...)
    description: constr(strict=True) = Field(...)
    date_in: constr(strict=True) = Field(...)
    property_type: conint(strict=True) = Field(...)
    end_week: conint(strict=True) = Field(...)
    typology_type: conint(strict=True) = Field(...)
    id: conint(strict=True) = Field(...)
    coordinates: constr(strict=True) = Field(...)
    boundary_id: conint(strict=True) = Field(...)
    id_uda: constr(strict=True) = Field(...)
    title: constr(strict=True) = Field(...)
    listing_type: conint(strict=True) = Field(...)
    date: constr(strict=True) = Field(...)

    class config:
        schema_extra = {
            "example": {
                "build_status": 0,
                "is_active": False,
                "start_month": 19213,
                "construction_type": "0",
                "date_diff": 0,
                "description": "VICÁLVARO CASCO HISTÓRICO la vivienda consta de 62 metros útiles distribuídos en salóncomedor cocina amueblada y con electrodomésticos dos dormitorios  un baño y dos terrazas.  Junto metro Vicálvaro y  San Cipriano. Cerca de la Renfe (Vicálvaro-Puerta Arganda) autobuses: 4 109 E3 N7.  En Inmuga Homes resolvemos cualquier duda o consulta fiscal y jurídica que pudiera surgir.   Buscamos FINANCIACIÓN. Tramitamos la inscripción de compraventas herencias cancelaciones de hipoteca levantamiento de embargos C. E. E…. y cualquier trámite relacionado con la transacción de su inmueble. Contáctenos para ampliar información.",
                "date_in": "2021-06-04T00:00:00.000Z",
                "property_type": 0,
                "end_week": 15184,
                "typology_type": 0,
                "id__": "5665884",
                "coordinates": "40.40039999999999764668245916254818439484,-3.60155000000000002913225216616410762072",
                "boundary_id": "71410",
                "id_uda": "54-93946671",
                "title": "Alquiler de Piso en Casco Histórico de Vicálvaro, Vicálvaro, Madrid — idealista",
                "listing_type": 1,
                "date": "2021-06-04T00:00:00.000Z"
            }
        }


class UpdatePropertyModel(BaseModel):
    build_status: Optional[conint(strict=True)]
    is_active: Optional[bool]
    start_month: Optional[constr(strict=True)]
    construction_type: Optional[constr(strict=True)]
    date_diff: Optional[conint(strict=True)]
    description: Optional[constr(strict=True)]
    date_in: Optional[constr(strict=True)]
    property_type: Optional[conint(strict=True)]
    end_week: Optional[conint(strict=True)]
    typology_type: Optional[conint(strict=True)]
    id: Optional[conint(strict=True)]
    coordinates: Optional[constr(strict=True)]
    boundary_id: Optional[conint(strict=True)]
    id_uda: Optional[constr(strict=True)]
    title: Optional[constr(strict=True)]
    listing_type: Optional[conint(strict=True)]
    date: Optional[constr(strict=True)]

    class config:
        schema_extra = {
            "example": {
                "build_status": 0,
                "is_active": False,
                "start_month": 19213,
                "construction_type": "0",
                "date_diff": 0,
                "description": "VICÁLVARO CASCO HISTÓRICO la vivienda consta de 62 metros útiles distribuídos en salóncomedor cocina amueblada y con electrodomésticos dos dormitorios  un baño y dos terrazas.  Junto metro Vicálvaro y  San Cipriano. Cerca de la Renfe (Vicálvaro-Puerta Arganda) autobuses: 4 109 E3 N7.  En Inmuga Homes resolvemos cualquier duda o consulta fiscal y jurídica que pudiera surgir.   Buscamos FINANCIACIÓN. Tramitamos la inscripción de compraventas herencias cancelaciones de hipoteca levantamiento de embargos C. E. E…. y cualquier trámite relacionado con la transacción de su inmueble. Contáctenos para ampliar información.",
                "date_in": "2021-06-04T00:00:00.000Z",
                "property_type": 0,
                "end_week": 15184,
                "typology_type": 0,
                "id": "5665884",
                "coordinates": "40.40039999999999764668245916254818439484,-3.60155000000000002913225216616410762072",
                "boundary_id": "71410",
                "id_uda": "54-93946671",
                "title": "Alquiler de Piso en Casco Histórico de Vicálvaro, Vicálvaro, Madrid — idealista",
                "listing_type": 1,
                "date": "2021-06-04T00:00:00.000Z"
            }
        }

    @classmethod
    def as_optional(cls):
        annonations = cls.__fields__
        fields = {
            attribute: (Optional[data_type.type_], None)
            for attribute, data_type in annonations.items()
        }
        OptionalModel = create_model(f"Optional{cls.__name__}", **fields)
        return OptionalModel


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
