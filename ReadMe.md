This project cleans and segments OCR generated from New Zealand Hansard from the year 1901. The original volumes were digitized by the Google Books project and stored in the Hathi Trust in pdf format. Microsft Azure Document Intelligence was used for text recognition, and Microsoft Co-Pilot was heavily used for cleaning and segmentation of the Azure .json output.

The final content seems reliable, but some pages seem to suffer from the low quality of the original page image, with slightly garbled results (possibly a result of the solution for the two column layout not working properly). Page numbers for the source PDFs are retained for cross-checking.

An additional step to use the OpenAI API for additional formatting and cleaning is only partially implemented after initial testing suggested it will be difficult to optimise and test.

Log files and processing artefacts (individual pages and a master file) have been retained for transparency and debugging.

Known issues:
- Lines in some columns are not transcribed. This could probably be improved by tuning the range settings in local_process.ipynb but it is tuned quite finely already.
- Tabular-like information (lists or columns of data) can result in the order of text on the page being mangled. This appears to be isolated to indiviudal pages. This could potentially be improved using different settings in Azure Document intelligence but doing so might require additional cleaning of digitization metadata.
- There are occasional remnants of digitization metadata (white spaces, exclamation marks, brackets etc). 

AAfter this baseline processing, the output is copied to [AIINFRA source preparation](https://github.com/AI-as-Infrastructure/aiinfra-source-preparation) for processing alongside AU and UK sources.