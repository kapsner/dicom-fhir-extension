# dicom-fhir-extension

This repo contains some classes and methods used for feasibility tests with respect to extending the [ImagingStudy](https://build.fhir.org/imagingstudy.html) FHIR resource.

The code from this repo is utilized in the [`dicom-fhir-converter`](https://github.com/kapsner/dicom-fhir-converter).

Currently added fields are:

| Modality | Name | DICOM Tag | FHIR Type |
| -------- | ---- | --------- | --------- |
| MR | Scanning Sequence | 0018,0020 | Coding |
| MR | Scanning Variant | 0018,0021 | Codeable Concept |
| MR | Echo Time | 0018,0081 | Decimal |


## Getting Started

```bash
git clone https://github.com/kapsner/dicom-fhir-converter
git clone https://github.com/kapsner/dicom-fhir-extension
cd dicom-fhir-converter
```

```python
from dicom2fhir import dicom2fhir
import json

root_path = "/path/to/dcm_imgaing_study/"

results = dicom2fhir.process_dicom_2_fhir(root_path)

jsonfile = "example_imagingStudy.json"


with open(jsonfile, "w+") as outfile:
    outfile.write(_res.json())
```
