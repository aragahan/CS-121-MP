$(document).ready(function()
{
    var quantitiy=0;
  
    $('.quantity-right-plus').click(function(e){
        e.preventDefault();
        var quantity = parseInt($('#quantity').val());
        $('#quantity').val(quantity + 1);
     });
 
      $('.quantity-left-minus').click(function(e){
         e.preventDefault();
         var quantity = parseInt($('#quantity').val());
         if(quantity>0)
         {
             $('#quantity').val(quantity - 1);
            }
     });

    $('#add-to-cart').hover(function(){
        $(this).css("background-color", "#343a40");
    },function(){
        $(this).css("background-color", "#1ea2fa");
    }) 
    (function() {
    const parent = document.querySelector('.range-slider');

    if (!parent) {
        return;
    }

    const rangeS = parent.querySelectorAll('input[type="range"]'),
          numberS = parent.querySelectorAll('input[type="number"]');

    rangeS.forEach((el) => {
        el.oninput = () => {
            let slide1 = parseFloat(rangeS[0].value),
                slide2 = parseFloat(rangeS[1].value);

            if (slide1 > slide2) {
                [slide1, slide2] = [slide2, slide1];
            }

            numberS[0].value = slide1;
            numberS[1].value = slide2;
        }
    });

    numberS.forEach((el) => {
        el.oninput = () => {
            let number1 = parseFloat(numberS[0].value),
                number2 = parseFloat(numberS[1].value);

            if (number1 > number2) {
                let tmp = number1;
                numberS[0].value = number2;
                numberS[1].value = tmp;
            }

            rangeS[0].value = number1;
            rangeS[1].value = number2;
        }
    });
  })

})();
