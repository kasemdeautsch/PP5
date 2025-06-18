let countryField=document.getElementById('id_default_country').value;
if(!countryField) {
    document.getElementById('id_default_country').style.color="#87BBFD";
};
$('#id_default_country').change(function() {
    let countryField = $(this).val();
    if(!countryField){
        $(this).css('color', "#87BBFD");
    } else {
        $(this).css('color', "#000");
    }
})