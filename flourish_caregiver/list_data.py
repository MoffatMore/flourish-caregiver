from edc_constants.constants import NOT_APPLICABLE, OTHER, NONE

from edc_list_data import PreloadData

list_data = {
    'flourish_caregiver.chronicconditions': [
        ('Asthma', 'Asthma'),
        ('Hypertension', 'Hypertension'),
        ('Hypercholesterolemia', 'Hypercholesterolemia'),
        ('Heart disease', 'Heart disease'),
        ('Hepatitis B surface Ag positive', 'Hepatitis B surface Ag positive'),
        ('Chronic Hepatitis B carrier', 'Chronic Hepatitis B carrier'),
        ('Hepatitis C', 'Hepatitis C'),
        ('Diabetes', 'Diabetes'),
        (OTHER, 'Other, Specify'),
        (NOT_APPLICABLE, 'Not Applicable')
    ],
    'flourish_caregiver.caregivermedications': [
        (NOT_APPLICABLE, 'Not Applicable'),
        ('Cholesterol medications', 'Cholesterol medications'),
        ('Vitamin D supplement', 'Vitamin D supplement'),
        (NONE, 'None'),
        ('Traditional medications', 'Traditional medications'),
        ('Hypertensive medications', 'Hypertensive medications'),
        ('Prenatal Vitamins', 'Prenatal Vitamins'),
        (OTHER, 'Other, Specify'),
    ],
    'flourish_caregiver.deliverycomplications': [
        ('Uterine rupture', 'Uterine rupture'),
        ('Hemorrhage req. transfusion', 'Hemorrhage req. transfusion'),
        ('Pre-eclampsia/eclampsia', 'Pre-eclampsia/eclampsia'),
        ('Placenta previa', 'Placenta previa'),
        ('Placental abruption', 'Placental abruption'),
        ('Chorioamnioitis or sus. chorioamnionitis',
         'Chorioamnioitis or sus. chorioamnionitis'),
        ('Intrapartum fever', 'Intrapartum fever'),
        ('Other', 'Other'),
        ('None', 'None')
    ],
    'flourish_caregiver.maternaldiagnoseslist': [
        ('Pneumonia', 'Pneumonia'),
        ('Chlamydia', 'Chlamydia'),
        ('Tuberculosis', 'Tuberculosis'),
        ('Depression', 'Depression'),
        ('Pre-eclampsia', 'Pre-eclampsia'),
        ('Gonorrhea', 'Gonorrhea'),
        ('Liver Problems', 'Liver Problems'),
        ('Hepatitis C', 'Hepatitis C'),
        ('Syphillis', 'Syphillis'),
        ('Asthma requiring steroids', 'Asthma requiring steroids'),
        ('Genital Herpes', 'Genital Herpes'),
        ('Gestational Hypertension', 'Gestational Hypertension'),
        (NOT_APPLICABLE, 'Not Applicable'),
        ('Other, specify', 'Other, specify')
    ],
    'flourish_caregiver.phonenumtype': [
        ('cell_phone', 'Cell Phone'),
        ('cell_phone_alt', 'Cell Phone (alternative)'),
        ('telephone', 'Telephone'),
        ('telephone_alt', 'Telephone (alternative)'),
        ('work_contact', 'Work contact number'),
        ('alt_person_cell', 'Alternative contact person cell phone'),
        ('alt_person_tel', 'Alternative contact person telephone'),
        ('resp_person_cell', 'Responsible person cell phone'),
        ('resp_person_tel', 'Responsible person telephone'),
        (NONE, 'None')
    ],
    'flourish_caregiver.priorarv': [
        ('AZT', 'AZT'),
        ('DDI', 'DDI'),
        ('Kaletra (or Aluvia)', 'Kaletra (or Aluvia)'),
        ('Nevirapine', 'Nevirapine'),
        ('3TC', '3TC'),
        ('Atripla', 'Atripla'),
        ('Tenofovir', 'Tenofovir'),
        ('Truvada (Tenofovir, FTC)', 'Truvada (Tenofovir, FTC)'),
        ('ATZ', 'ATZ'),
        ('D4T', 'D4T'),
        ('Raltegravir', 'Raltegravir'),
        ('Efavirenz (or Sustiva)', 'Efavirenz (or Sustiva)'),
        ('Combivir (AZT,3TC)', 'Combivir (AZT, 3TC)'),
        ('Trizivir (AZT, 3TC, Abacavir)', 'Trizivir (AZT, 3TC, Abacavir)'),
        ('Abacavir', 'Abacavir'),
        ('Dolutegravir', 'DTG'),
        ('ART, unknown', 'ART, unknown'),
        (NOT_APPLICABLE, 'Not Applicable'),
        ('Other, specify', 'Other, specify')
    ],
    'flourish_caregiver.wcsdxadult': [
        ('Asymptomatic', 'Asymptomatic'),
        ('Persistent generalized lymphadeno',
         'Persistent generalized lymphadeno'),
        ('Unexplained moderate weight loss',
         'Unexplained moderate weight loss'),
        ('Recurrent resp tract infection', 'Recurrent resp tract infection'),
        ('Herpes zoster', 'Herpes zoster'),
        ('Angular cheilitis', 'Angular cheilitis'),
        ('Recurrent oral ulceration', 'Recurrent oral ulceration'),
        ('Papular pruritic eruptions', 'Papular pruritic eruptions'),
        ('Seborrhoeic dermatitis', 'Seborrhoeic dermatitis'),
        ('Fungal nail infections', 'Fungal nail infections'),
        ('Unexplained* severe weight loss', 'Unexplained* severe weight loss'),
        ('Unexplained persistent fever', 'Unexplained persistent fever'),
        ('Unexplained chronic diarrhoea', 'Unexplained chronic diarrhoea'),
        ('Persistent oral candidiasis', 'Persistent oral candidiasis'),
        ('Oral hairy leukoplakia', 'Oral hairy leukoplakia'),
        ('Pulmonary tuberculosis', 'Pulmonary tuberculosis'),
        ('Severe bacterial infections', 'Severe bacterial infections'),
        ('stomatitis/gingivitis/periodontis',
         'Stomatitis/gingivitis/periodontis'),
        ('anaemia/neutropaenia/thrombocytopa',
         'Anaemia/neutropaenia/thrombocytopa'),
        ('HIV wasting syndrome', 'HIV wasting syndrome'),
        ('Pneumocystis pneumonia', 'Pneumocystis pneumonia'),
        ('Recurrent severe bacterial pneumo',
         'Recurrent severe bacterial pneumo'),
        ('Chronic herpes simplex infection',
         'Chronic herpes simplex infection'),
        ('Oesophageal candidiasis', 'Oesophageal candidiasis'),
        ('Extrapulmonary tuberculosis', 'Extrapulmonary tuberculosis'),
        ('Kaposi\u2019s sarcoma', 'Kaposi\u2019s sarcoma'),
        ('Cytomegalovirus infection', 'Cytomegalovirus infection'),
        ('CNS toxoplasmosis', 'CNS toxoplasmosis'),
        ('HIV encephalopathy', 'HIV encephalopathy'),
        ('Exp cryptococcosis/meningitis', 'Exp cryptococcosis/meningitis'),
        ('Diss non-TB mycobacterial infection',
         'Diss non-TB mycobacterial infection'),
        ('Prog multifocal leukoencephalopathy',
         'Prog multifocal leukoencephalopathy'),
        ('Chronic cryptosporidiosis', 'Chronic cryptosporidiosis'),
        ('Chronic isosporiasis', 'Chronic isosporiasis'),
        ('Disseminated mycosis', 'Disseminated mycosis'),
        ('Recurrent septicaemia', 'Recurrent septicaemia'),
        ('Lymphoma', 'Lymphoma'),
        ('Invasive cervical carcinoma', 'Invasive cervical carcinoma'),
        ('Atypical disseminated leishmaniasis',
         'Atypical disseminated leishmaniasis'),
        ('Sympt nephropathy/cardiomyopathy',
         'Sympt nephropathy/cardiomyopathy'),
        (NOT_APPLICABLE, 'Not Applicable'),
    ],
    'flourish_caregiver.covidsymptoms': [
        ('chest_pain', 'Chest pain'),
        ('chills', 'Chills'),
        ('Cough', 'Cough'),
        ('Diarrhea ', 'Diarrhea '),
        ('Fever', 'Fever > 37.5 Degree Celsius'),
        ('muscle_aches', 'Muscle aches'),
        ('nasal_congestion', 'Nasal Congestion'),
        ('Nausea_or_vomiting  ', 'Nausea/vomiting'),
        ('shortness_of_breath', 'Shortness of breath'),
        ('sore_throat', 'Sore throat'),
    ],

    'flourish_caregiver.covidsymptomsafter14days': [
        ('chest_pain', 'Chest pain'),
        ('chills', 'Chills'),
        ('Cough', 'Cough'),
        ('Diarrhea ', 'Diarrhea '),
        ('Fever', 'Fever > 37.5 Degree Celsius'),
        ('muscle_aches', 'Muscle aches'),
        ('nasal_congestion', 'Nasal Congestion'),
        ('Nausea_or_vomiting  ', 'Nausea/vomiting'),
        ('shortness_of_breath', 'Shortness of breath'),
        ('sore_throat', 'Sore throat'),
    ],

}

preload_data = PreloadData(
    list_data=list_data)
