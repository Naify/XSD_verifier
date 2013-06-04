$(document).ready(function() { 
	var options = {
		target: '#logbox'
		// success: function(answer){		
			// $("#logbox").html(answer); //Insert chat log into the #chatbox div				
		// }
	};

	$('#former').ajaxForm(options);

//some changes	
	// $('#former').submit(function() {
		// alert('ololo');
		// $(this).find(':disabled').removeAttr('disabled');
		// $(this).ajaxSubmit(options);
		// return false;
	// });

	// $('#former').ajaxForm(function() {
		// var options = {
		  // target: "#logbox",
		  // url: "server/server.py",
		  // success: function() {
			// alert("thx!");
		  // }
		// };

		// alert("Thank you for your comment!"); 
	// }); 
	
});

function getName (str){
    if (str.lastIndexOf('\\')){
        var i = str.lastIndexOf('\\')+1;
    }
    else{
        var i = str.lastIndexOf('/')+1;
    }						
    var filename = str.slice(i);			
    var uploaded = document.getElementById("fileformlabel");
    uploaded.innerHTML = filename;
};