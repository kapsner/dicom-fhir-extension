#!/usr/bin/env python

__author__ = "Lorenz A. Kapsner"

from fhir import resources as fr
import typing
from pydantic import Field


class ImagingStudySeriesErlangen(fr.imagingstudy.ImagingStudySeries):
    # general image

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
            "instance",
            "scanningSequence",
            "scanningVariant",
            "echoTime",
        ]
