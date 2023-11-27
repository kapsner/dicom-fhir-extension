#!/usr/bin/env python

__author__ = "Lorenz A. Kapsner"

from fhir.resources import R4B as fr
import typing
from pydantic import Field


# https://github.com/nazrulworld/fhir.resources/blob/02b04257dfe2f956fb2c7825624da50f8a464afd/fhir/resources/imagingstudy.py


class ImagingStudyErlangen(fr.imagingstudy.ImagingStudy):

    bodySite__ext: typing.List[fr.fhirtypes.CodeableReferenceType] = Field(
        None,
        alias="bodySite",
        title="All of the distinct values for series' body site.",
        description=("All of the distinct values for series.bodySite."),
        # if property is element of this resource.
        element_property=True,
    )
    laterality__ext: typing.List[fr.fhirtypes.CodeableConceptType] = Field(
        None,
        alias="laterality",
        title="All of the distinct values for series' laterality.",
        description=("All of the distinct values for series.laterality."),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ImagingStudy`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "meta",
            "implicitRules",
            "language",
            "text",
            "contained",
            "extension",
            "modifierExtension",
            "identifier",
            "status",
            "modality",
            "subject",
            "encounter",
            "started",
            "basedOn",
            "referrer",
            "endpoint",
            "numberOfSeries",
            "numberOfInstances",
            "procedureCode",
            "location",
            "reasonCode",
            "note",
            "description",
            "series"
            # "laterality", # kann man so nicht definieren, sonst kommt keine valide FHIR Ressource raus 
                            # --> eigene StructureDefinition und dann als extension in der ImagingStudy definieren
            # "bodySite",
        ]


class ImagingStudySeriesErlangen(fr.imagingstudy.ImagingStudySeries):
    # general image
    imageType: fr.fhirtypes.CodingType = Field(
        None,
        alias="imageType",
        title="Image Type",
        description="Echo Time",
        # if property is element of this resource.
        element_property=True,
    )

    # MR-specific
    scanningSequence__ext: fr.fhirtypes.CodingType = Field(
        None,
        alias="scanningSequence",
        title="All of the distinct values for series' scanning sequence",
        description=("Description of the type of data taken."),
        # if property is element of this resource.
        element_property=True,
    )
    scanningVariant__ext: fr.fhirtypes.CodeableConceptType = Field(
        None,
        alias="scanningVariant",
        title="All of the distinct values for series' scanning variant",
        description=("Variant of the Scanning Sequence."),
        # if property is element of this resource.
        element_property=True,
    )
    echoTime__ext: fr.fhirtypes.Decimal = Field(
        None,
        alias="echoTime",
        title="Echo Time",
        description="Echo Time",
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``ImagingStudySeries`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "uid",
            "number",
            "modality",
            "description",
            "numberOfInstances",
            "endpoint",
            "bodySite",
            "laterality",
            "specimen",
            "started",
            "performer",
            "instance"
            # "scanningSequence", # siehe oben!
            # "scanningVariant",
            # "echoTime",
        ]