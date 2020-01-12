CC=avr-gcc
OBJCOPY=avr-objcopy

CFLAGS=-Os -DF_CPU=16000000UL -mmcu=atmega32u4

PORT=/dev/ttyACM0

OBJS := main.o

pr.hex: pr.elf
	$(OBJCOPY) -O ihex -R .eeeprom $< $@

pr.elf: $(OBJS)
	$(CC) -o $@ $^

install: pr.hex
	avrdude -F -V -c arduino -p ATMEGA32U4 -P ${PORT} -b 115200 -U flash:w:$<

clean:
	$(RM) pr.hex pr.elf $(OBJS)

.PHONY: install clean
