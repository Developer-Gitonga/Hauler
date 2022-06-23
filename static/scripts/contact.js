$(document).ready(function() {
  $("form#form").submit(function(event) {
      // event.preventDefault();
      var name = $("input#name").val();
      var email = $("input#email").val();
      var message = $("textarea#subject").val();
      if (name && email) {
          alert(name + ", we have received your message. Thank you for considering us. We shall respond as soon as possible.Big up!!");
      } else {
          alert("Please enter your name and email!");
      }

  });

});