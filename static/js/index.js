let selectedFile;
console.log(window.XLSX);
function UploadDealcsv() {
}

UploadDealcsv.prototype.getCsv = function () {
    document.getElementById('cvs_file').addEventListener("change", (event) => {
    selectedFile = event.target.files[0];
    XLSX.utils.json_to_sheet(data, 'out.xlsx');
    if (selectedFile) {
        let fileReader = new FileReader();
        fileReader.readAsBinaryString(selectedFile);
        fileReader.onload = (event) => {
            let data = event.target.result;
            let workbook = XLSX.read(data, {type: "binary"});
            console.log(workbook);
            workbook.SheetNames.forEach(sheet => {
                let rowObject = XLSX.utils.sheet_to_row_object_array(workbook.Sheets[sheet]);
               console.log(rowObject.type);
                for (let row of rowObject) {
                    console.log(row.type)
                    console.log(row)
                }
            });
        }
    }

})
}


let data = [{
    "name": "jayanth",
    "data": "scd",
    "abc": "sdef"
}]

function new_input(data, class_name, name) {
    const input_tr_date = document.createElement('input')
    input_tr_date.type = 'text'
    input_tr_date.className = class_name
    input_tr_date.value = data
    input_tr_date.name = name
    return input_tr_date;
}

function createARow(clients_id, clients_name, employer_id, employer_name, day_of_work, time_of_work, start_of_work, end_of_work) {
    const new_input_group = document.createElement('div')
    new_input_group.className = 'input-group mb-1'
    // clients_id
    const input_clients_id = new_input(clients_id, 'form-control col justify-content-start', 'clients_id');
    input_clients_id.readOnly = "readonly"
    input_clients_id.style.display = "none"
    // clients_name
    const input_clients_name = new_input(clients_name, 'form-control col justify-content-start', 'clients_name');
    input_clients_name.readOnly = "readonly"
    // employer_id
    const input_employer_id = new_input(employer_id, 'form-control col justify-content-start', 'employer_id');
    input_employer_id.readOnly = "readonly"
    input_employer_id.style.display = "none"
    // employer_name
    const input_employer_name = new_input(employer_name, 'form-control  col justify-content-center', 'employer_name')
    input_employer_name.readOnly = "readonly"
    // time_of_work
    const input_time_of_work = new_input(time_of_work, 'form-control  col justify-content-center', 'time_of_work')
    input_time_of_work.readOnly = "readonly"
    // day_of_work
    const input_day_of_work = new_input(day_of_work, 'form-control col justify-content-center', 'day_of_work')
    input_day_of_work.readOnly = "readonly"
    //work start
    const input_start_of_work = new_input(start_of_work, 'form-control col justify-content-center', 'start_of_work')
    input_start_of_work.readOnly = "readonly"
    input_start_of_work.style.display = "none"
    //work end
    const input_end_of_work = new_input(end_of_work, 'form-control col justify-content-center', 'end_of_work')
    input_end_of_work.readOnly = "readonly"
    input_end_of_work.style.display = "none"

    new_input_group.appendChild(input_clients_id)
    new_input_group.appendChild(input_clients_name)
    new_input_group.appendChild(input_employer_id)
    new_input_group.appendChild(input_employer_name)
    new_input_group.appendChild(input_time_of_work)
    new_input_group.appendChild(input_day_of_work)
    new_input_group.appendChild(input_start_of_work)
    new_input_group.appendChild(input_end_of_work)


    document.getElementById("action_form").appendChild(new_input_group);

}

let ExcelToJSON = function () {

    this.parseExcel = function (file) {
        let reader = new FileReader();

        reader.onload = function (e) {
            let data = e.target.result;
            let workbook = XLSX.read(data, {
                type: 'binary'
            });

            workbook.SheetNames.forEach(function (sheetName) {
                // Here is your object
                let XL_row_object = XLSX.utils.sheet_to_row_object_array(workbook.Sheets[sheetName]);
                let json_object = JSON.stringify(XL_row_object);
                console.log(json_object);

            })

        };

        reader.onerror = function (ex) {
            console.log(ex);
        };

        reader.readAsBinaryString(file);
    };
};

let parseCsv = new UploadDealcsv();
parseCsv.getCsv();
