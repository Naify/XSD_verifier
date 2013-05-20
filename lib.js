
function hideBtn(){
	$('#res').html("File is loading");
}
	         
function handleResponse(mes) {
	$('#upload').show();
	if (mes.errors != null) {
		$('#res').html("Errors: " + mes.errors);
	}   
	else {
		$('#res').html("File " + mes.name + " loaded");   
	}


}