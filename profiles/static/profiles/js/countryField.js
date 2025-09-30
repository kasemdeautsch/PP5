// Add the proper color on the country field on start and change event
let countryField=document.getElementById('id_default_country').value;
if(!countryField) {
    document.getElementById('id_default_country').style.color="#87BBFD";
}
$('#id_default_country').change(function() {
    let countrySelected = $(this).val();
    if(!countrySelected){
        $(this).css('color', "#87BBFD");
    } else {
        $(this).css('color', "#000");
    }
});