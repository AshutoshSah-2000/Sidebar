

function NLGFunction() {
    fetch('/getdata/').then(function (response) {
        document.getElementById("content").innerHTML=response
        console.log("CLICKED NLG!!")
        response.json().then(function data)
        {
            console.log(data)
        }
    })
  }

  $(document).ready(function () {

    $('#sidebarCollapse').on('click', function () {
        $('#sidebar').toggleClass('active');
    });

});