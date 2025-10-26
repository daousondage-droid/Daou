import stripe

stripe.api_key = "sk_test_your_key_here"  # Remplace par ta vraie clé Stripe

def create_checkout_session():
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'eur',
                'product_data': {
                    'name': 'Accès Premium Sirri',
                },
                'unit_amount': 500,  # 5 euros
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url='https://tonsite.com/succes',
        cancel_url='https://tonsite.com/annule',
    )
    return session.url
