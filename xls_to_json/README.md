# Step1
* Install required packages from requirments.txt
# Step2
* Run the `xls_json_file_upload.py` file
* hit the url "https://127.0.0.1:8000/file/" to upload file [Postman]
* To view documentation and In-Browser check HIT "http://127.0.0.1:8000/docs#/default/file_load_file__post" [Browser] 
# Explanation of the code/functionality
* The main logic to convert xls to json was done by `xls_to_json` function with `file data` and `file name` as mandatory fields.
* The uploaded file has to be in `xls` or `xlsx` format if not throw the `400` Error.
* Json was divided on the prefix of `table3` and `table4`, `table3` goes to `strategies` and `table4` goest to `productSegment`
* Later in each `strategies` was divided on the bases of the sheet name `current` and `tierone`

**Here haven't consider the childlevel linkage, Because haven't found related info on relationship in the given excel sheet**
