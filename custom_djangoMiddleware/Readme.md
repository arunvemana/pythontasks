# Error logging using DjangoMiddleware

## Project Details:
**ProjectName**: `ExceptionaLogPro`

**Endpoint**: "http://localhost:8000/" --> give complete info on endpoints
**App1**: `StoreException` ->
* **Endpoint**: **GET** `http://127.0.0.1:8000/GenerateException/`
* **Response**: Give u the random Exception name with random Status_code

**App2**: `GetException` ->
* **Endpoint**: **GET** `http://127.0.0.1:8000/FilterException/`
* **Response**: Give u the all the value from the database.
* **Endpoint**: **POST** `http://127.0.0.1:8000/FilterException/`
* **body**: Form-data -> `id`:<id value> to delete the particular record
* **Response**: success message for deletion of record.

> Find the postman collection for more details
> 