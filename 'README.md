1. **RUN** "*text-parser.py*" on PDFs to extract text blocks
2. **RUN** "*text-parser-clean.py*" to get rid of bounding boxes and stuff, only texts, page number, and source.
3. TO TRAIN
   1. **START** *Label Studio* (**label-studio start**) to label data to be used for training - import the output from step 2
   2. **Export** from *Label Studio* a JSON file, put into the "spacy-training" folder with the name "*fugue_LS_training_data_SAMPLE.json*"
   3. **Follow & RUN** the "*convert_to_docbin.py*" script to convert to docBin format, and creating "*dev.spacy*" and "*train.spacy*"
      1. **Follow** command instructions in "*convert_to_docbin.py*" script
         1. GO TO CORRECT DIRECTORY ---- *cd C:\Users\13065\Documents\GitHub\queering-geographies\spacy-training*
         2. START TRAINING ---- ***python -m spacy train config.cfg --output ./output --paths.train ./train.spacy --paths.dev ./dev.spacy***
4. Then ... you can run "*spacy-parser.py*" on any _CLEAN output


<!-- TODO -->
TASKS
- Make "config.py" and "index.py" to batch automate this process.


OCR WITH GCS cloud command
# #! ######################################### STEP 0 ##############################################

# Prediction Endpoint:
#   https://us-documentai.googleapis.com/v1/projects/250300843094/locations/us/processors/a8c7e841a98abf38:process


LIST Files 
``` bash
gry_spc@cloudshell:~ (project-09437c36-1230-414f-9fc)$ gcloud storage ls gs://fugue-magazines/2011
```


Build a CURL Command to communicate with the API
``` bash
gry_spc@cloudshell:~ (project-09437c36-1230-414f-9fc)$ curl -X POST "https://us-documentai.googleapis.com/v1/projects/250300843094/locations/us/processors/a8c7e841a98abf38:process" -H "Authorization: Bearer $(gcloud auth print-access-token)" -H "Content-Type: application/json" -d "{\"rawDocument\":{\"content\":\"$(base64 -w 0 gs://fugue-magazines/2011/fugues_apr-2011.pdf)\",\"mimeType\":\"application/pdf\"}}"
```

NOTE: base64 command can't read directly from a GCS..
So we have to format the PDF in base64 format first
``` bash
gry_spc@cloudshell:~ (project-09437c36-1230-414f-9fc)$ echo "{\"rawDocument\":{\"content\":\"$(gcloud storage cat gs://fugue-magazines/2011/fugues_apr-2011.pdf | base64 -w 0)\",\"mimeType\":\"application/pdf\"}}" > request.json
```

``` bash
cat request.json l jq.
``` 


IF PDF is too big (which it is) we have to split it into 2 parts using "pdftk"
``` bash
gry_spc@cloudshell:~ (project-09437c36-1230-414f-9fc)$ sudo apt-get update && sudo apt-get install pdftk
```

``` bash
gry_spc@cloudshell:~ (project-09437c36-1230-414f-9fc)$ pdftk file.pdf cat 1-100 output part1.pdf
```

--------------------------------------------------------------------


Google Cloud SDK
**