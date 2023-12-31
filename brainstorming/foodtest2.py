"""
This program is written to familiarize with click's .confirm() tools and seek to do something similar to foodtest.py
"""
import click

total = 0.00

def get_burger_options():
    global total

    while True:
        selected_options = []
        total += 5.00
        subtotal = 5.00

        impossible = click.confirm('Do you want to substitute beef patty for impossible patty?')
        cheese = click.confirm('Do you want to add cheese to the burger?')
        ketchup = click.confirm('Do you want to add ketchup to the burger?')
        lettuce = click.confirm('Do you want to add lettuce to the burger?')
        tomato = click.confirm('Do you want to add tomato to the burger?')
        pickle = click.confirm('Do you want to add pickles to the burger?')
        mushroom = click.confirm('Do you want to add mushrooms to the burger?')

        if impossible:
            click.echo('You have substituted for impossible meat.')
            selected_options.append('impossible meat')
            total += 1.00
            subtotal += 1.00
        if cheese:
            click.echo('You have added cheese.')
            selected_options.append('cheese')
            total += 0.50
            subtotal += 0.50
        if ketchup:
            click.echo('You have added ketchup.')
            selected_options.append('ketchup')
        if lettuce:
            click.echo('You have added lettuce.')
            selected_options.append('lettuce')
            total += 0.50
            subtotal += 0.50
        if tomato:
            click.echo('You have added tomato.')
            selected_options.append('tomato')
            total += 0.50
            subtotal += 0.50
        if pickle:
            click.echo('You have added pickles.')
            selected_options.append('pickles')
            total += 0.25
            subtotal += 0.25
        if mushroom:
            click.echo('You have added mushrooms.')
            selected_options.append('mushrooms')
            total += 0.25
            subtotal += 0.25

        

        # Want to make a list to add orders and have a cumulative print summary at the end 

        options_text = ', '.join(selected_options)
        if options_text:
            click.echo(f"Your burger includes {options_text}. The subtotal is ${subtotal:.2f}")
        else:
            click.echo(f"No added ingredients/toppings. The subtotal is ${subtotal:.2f}")
        
        more_food = click.confirm('Do you want to order more food?')
        if not more_food:
            click.echo(f"Thank you! Your order total is ${total:.2f}")
            break


@click.command()
@click.argument('name_of_order')
def burger(name_of_order):
    order = f"Your order is for {name_of_order}."
    click.echo(order)
    get_burger_options()

if __name__ == '__main__':
    burger()
