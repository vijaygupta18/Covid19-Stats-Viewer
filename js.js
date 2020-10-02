document.getElementById("stats2").disabled = true;
document.getElementById("stats1").disabled = true;
document.getElementById("stats4").disabled = true;

function getData() {
    var country = document.getElementById('country').value;
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            document.myform.stats1.value = 'Confirmed Cases - ' + JSON.parse(this.responseText)['confirmed'].value
            document.myform.stats2.value = 'Recovered - ' + JSON.parse(this.responseText)['recovered'].value

            document.myform.stats4.value = 'Death(s) - ' + JSON.parse(this.responseText)['deaths'].value
        }
    };
    xhttp.open("GET", "https://covid19.mathdro.id/api/countries/" + country, true);
    xhttp.send();
}