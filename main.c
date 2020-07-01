#include <avr/io.h>
#include <avr/interrupt.h>
#include <avr/sleep.h>
#include <util/delay.h>

//ISR(INT2_vect)
//{
	//PORTC = (1 <<7); /* turn on the led */
//}

#define FALLING_EDGE 2
#define IRQ2_OFFSET(bits) (2 * bits)

void setup_io()
{
	DDRC |=  (1 << 7); /* portc7 (LED AKA pin13) output */
//	EIMSK = 1 << IRQ2_OFFSET(1); /* enable IRQ2 */
//	EICRA = FALLING_EDGE << IRQ2_OFFSET(2); /* IRQ2 trigger type */
}

int main(void)
{
	setup_io();
	PORTC = (1 <<7); /* turn off the led */
//	sei();
	//set_sleep_mode(SLEEP_MODE_IDLE);
	//sleep_mode();
	while (1) {
	    _delay_ms(1000);
	    PORTC = (1 <<7); /* turn on the led */
	    _delay_ms(1000);
	    PORTC = (0 <<7); /* turn off the led */
	}
}
