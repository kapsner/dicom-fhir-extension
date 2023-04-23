# dicom-fhir-extension

This repo contains some classes and methods used for feasibility tests with respect to extending the [ImagingStudy](https://build.fhir.org/imagingstudy.html) FHIR resource.

The code from this repo is utilized in the [`dicom-fhir-converter`](https://github.com/kapsner/dicom-fhir-converter).

Currently added fields are:

| Modality | Name | DICOM Tag | FHIR Type |
| -------- | ---- | --------- | --------- |
| MR | Scanning Sequence | 0018,0020 | Coding |
| MR | Scanning Variant | 0018,0021 | Codeable Concept |
| MR | Echo Time | 0018,0081 | Decimal |
