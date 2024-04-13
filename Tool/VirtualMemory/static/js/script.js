document.addEventListener("DOMContentLoaded", function() {
    // Your JavaScript code
    document.getElementById("form-data").addEventListener("submit", colorHitOrMiss);
});

function colorHitOrMiss(event) {    

    alert(1)
    
    var table = document.getElementById("table");
    var rows = table.rows;

    console.log(table)

    for (var i = 1; i < rows[0].cells.length; i++) {
        var headerCell = rows[0].cells[i];
        for (var j = 1; j < rows.length; j++) {
            if (headerCell === rows[i].cells[j]) {
                alert(headerCell);
            }
        }
    }

    return false;
}
