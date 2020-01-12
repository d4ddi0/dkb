#include <avr/io.h>
#include <avr/interrupt.h>
#include <avr/sleep.h>

void setup_io()
{
}

int main(void)
{
	setup_io();
	sei();
	set_sleep_mode(SLEEP_MODE_IDLE);
	sleep_mode();
}
