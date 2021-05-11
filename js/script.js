$(document).ready(function()
{
    var quantitiy=0;
    $('a').css({
        color: 'white',
    })
    
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
    
})