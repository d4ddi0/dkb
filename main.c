#include <avr/io.h>
#include <avr/interrupt.h>
#include <avr/sleep.h>

ISR(INT0_vect)
{

}

void setup_io()
{
	DDRC |=  (1 << 7); /* portc7 (LED AKA pin13) output */
}

int main(void)
{
	setup_io();
	PORTC = (1 <<7); /* turn on the led */
	sei();
	set_sleep_mode(SLEEP_MODE_IDLE);
	sleep_mode();
}
