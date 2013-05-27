$(document).ready(function() {

	$('#former').ajaxForm(function() {
	
		success: function(answer){		
			$("#logbox").html(answer); //Insert chat log into the #chatbox div				
		}
		
	});
	
 });