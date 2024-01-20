$(document).ready(function() {
    var incrementButton = $('.increment');
    var decrementButton = $('.decrement');
  
    var countInput = $('.count');
  
    incrementButton.click(function() {
      var currentValue = parseInt(countInput.val());
  
      currentValue++;
  
      countInput.val(currentValue);
  
      
    });
  
          decrementButton.click(function() {
      var currentValue = parseInt(countInput.val());
  
      currentValue--;
  
      countInput.val(currentValue);
  
      if (currentValue === 1) {
        decrementButton.prop('disabled', true);
      }
    });
  });