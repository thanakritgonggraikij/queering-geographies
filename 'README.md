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
- 