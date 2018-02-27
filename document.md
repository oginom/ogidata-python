
# APIs 
<!-- ################################# -->
## api/createtable(name,cols)

### POST
- name : String
- cols : JSON{Array(ColInfo)}

### RESPONSE

<!-- ################################# -->
## api/gettables()

### GET

### RESPONSE

- DICT{table_title : table_id}

<!-- ################################# -->
## api/gettableid(title)

### GET

- title : String

### RESPONSE

- table_id : INT

<!-- ################################# -->
## api/uploadimage(file)

### POSTFILE

- file : IMG(image/png, image/jpeg)

### RESPONSE

(success)

- DICT{result:"success", img_id:img_id}

<!-- ################################# -->
## api/insertdata(insert,data)

### POST
- title : String
- data : JSON{Dict{name : val}}

### RESPONSE

<!-- ################################# -->
## (ErrorMessage)

### RESPONSE
- DICT{"ErrorMessage" : errmsg}

<!-- ################################# -->
# Types

	ColInfo : Dict{
	  (name_db : String : col%d)
	  name : String
	  type : DataType
	  unit : UnitType
	}

	DataType : Enum{
	  INT,
	  DOUBLE,
	  DECIMAL,
	  STRING,
	  DATETIME,
	  IMG
	}

	UnitType : Enum{
	  NONE,
	  YEN
	}

<!-- ################################# -->
# Inner files

## tableinfo/table%d.json
- %d : tableID

### JSON
- title : String
- columns : Array(ColInfo)

<!-- ################################# -->
# MySQL tables

##  table%d

table for table_id %d

- created_at : DATETIME NOT NULL : CURRENT_TIMESTAMP

	- Auto column

- data_id : INT AUTO_INCREMENT NOT NULL PRIMARY KEY

	- Auto column

- col%d : (Type)

	- Data column

### DataType for SQL

- INT : INT
- DOUBLE : DOUBLE
- STRING : VARCHHAR(64)
- IMG : INT : img_id

## table_title

- created_at : DATETIME NOT NULL : CURRENT_TIMESTAMP

	- Auto column

- table_id : INT AUTO_INCREMENT NOT NULL PRIMARY KEY

- title : VARCHAR(255) UNIQUE NOT NULL

## img_info

- posted_at : DATETIME NOT NULL : CURRENT_TIMESTAMP,

	- Auto Column

- img_id : INT NOT NULL PRIMARY KEY : MAX(img_id) + 1
- mime_type : VARCHAR(255) NOT NULL
- img_filename : VARCHAR(255) UNIQUE NOT NULL : img-%d.(type)
- img_width : INT
- img_height : INT 
