# Speech-Recognition-in-Indian-Languages

Google Doc File : https://docs.google.com/document/d/1rIBITYc4QbGlUJAkcu5B9ATJ7FXy5eBy5bid43J1md4/edit

Google Sheets File :  https://docs.google.com/spreadsheets/d/1ewvoW1cN1ML07BorUNo24gVgyIvL-Ey_7wCqObIah_w/edit?usp=sharing
<br>
Experiments:
1. Gujarati (35h) LAS
1.1 Hindi,Marathi,Telegu,Mandarin(or English) (Adaptation Data + I-Vector) Full Train (No Pretraining used)
2.1 Hindi,Marathi,Telegu,Mandarin(or English) (Adaptation Data + I-Vector) fine tunde Decoder (Pretrained Model = Pt.1)

2. Gujarati (35h) Transformer
2.1 Hindi,Marathi,Telegu,Mandarin(or English) (Adaptation Data + I-Vector) Full Train (No Pretraining used)
2.2 Hindi,Marathi,Telegu,Mandarin(or English) (Adaptation Data + I-Vector) fine tunde Decoder (Pretrained Model = Pt.2)

3. I-Vector Feature Extraction using kaldi for Hindi,Marathi,Telegu,Mandarin(or English) 

4. Sequential Fine Tuning:
4.1 Gujarati(ParentModel) -> Hindi -> Marathi -> Mandarin  (LAS)
4.2 Gujarati(ParentModel) -> Hindi -> Marathi -> Mandarin   (Transformer)
