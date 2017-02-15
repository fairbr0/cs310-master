var inst

var count = 1

function presentFinish() {
  $('#original_article').empty();
  $('#summary_A').empty();
  $('#summary_B').empty();

  $('#title').text("Finished. Thank you!");
  $('#next').text("New");

  count = 0;
}

function setContent() {
  if (count == 21) {
    presentFinish();
    return;
  }

  if (count == 0) {
    $('#title').text("Summation comparison tests");
    $('#next').text("Next");
  }

  $('#number').text("Article " + count);
  $('#original_article').empty();
  $('#summary_A').empty();
  $('#summary_B').empty();


  $.ajax({url:'./resources/bodies/article' + count + '.txt', type: 'GET',dataType: 'text', statusCode: {
      200 : function(data) {
        console.log(data)
        $('#original_article').text(data);
      }
    }
  });

  $.ajax({url:'./resources/summaries/_article' + count + '.txt', dataType: 'text', statusCode: {
      200 : function(data) {
        $('#summary_A').text(data);
      }
    }
  });

  $.ajax({url:'./resources/summaries/smmry' + count + '.txt', dataType: 'text', statusCode: {
      200 : function(data) {
        $('#summary_B').text(data);
      }
    }
  });
/*
  jQuery.get('./resources/summaries/_article' + count + '.txt', dataType: 'text',function(data) {
    $('#original_article').add(data)
  });

  jQuery.get('./resources/summaries/smmry' + count + '.txt', dataType: 'text',function(data) {
    $('#original_article').add(data)
  });*/

  count += 1
}


$(document).ready(function() {

  setContent()
  $('#next').click(function() {
    setContent()
  })
});
