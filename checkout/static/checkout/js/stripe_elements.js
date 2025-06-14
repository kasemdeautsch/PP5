console.log('Hi')

var stripePublicKey = $('#id_stripe_public_key').text().slice(1,-1);
var clientSecret = $('#id_client_secret').text().slice(1,-1);


var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();


 var style = {
    base: {
      iconColor: '#000',
      color: '#000',
      fontWeight: '500',
      fontFamily: 'Roboto, Open Sans, Segoe UI, sans-serif',
      fontSize: '16px',
      fontSmoothing: 'antialiased',
      ':-webkit-autofill': {
        color: '#fce883',
      },
      '::placeholder': {
        color: '#87BBFD',
      },
    },
    invalid: {
      iconColor: '#FFC7EE',
      color: '#FFC7EE',
    },
};
var card = elements.create('card', {style: style});
card.mount('#card-element');

// Handle real time validation errors from card element

card.addEventListener('change', function(e) {
    var errorDiv = $('#card-errors');
    if(e.error) {
        var html = `
        <span class="icon" role="alert">
            <i class="fas fa-times"></i>
        </span>
        <span>${e.error.message}..</span>
        `
        $(errorDiv).html(html);
    } else{
        $(errorDiv).text('')
    }
});

// Handle form submission
var form = document.getElementById('payment-form');

form.addEventListener('submit', function(event) {
    event.preventDefault();
    card.update({ 'disabled': true});
    $('#submit-button').attr('disabled', true);
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
        }
    }).then(function(result) {
        if (result.error) {
            var errorDiv = document.getElementById('card-errors');
            var html = `
                <span class="icon" role="alert">
                <i class="fas fa-times"></i>
                </span>
                <span>${result.error.message}</span>`;
            $(errorDiv).html(html);
            card.update({ 'disabled': false});
            $('#submit-button').attr('disabled', false);
        } else {
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    });
});