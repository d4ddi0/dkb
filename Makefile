CC=avr-gcc
OBJCOPY=avr-objcopy

CFLAGS=-Os -DF_CPU=16000000UL -mmcu=atmega32u4

PORT=/dev/ttyACM0

OBJS := main.o

dkb.hex: dkb.elf
	$(OBJCOPY) -O ihex -R .eeeprom $< $@

dkb.elf: $(OBJS)
	$(CC) -o $@ $^

install: dkb.hex
	avrdude -F -V -c arduino -p ATMEGA32U4 -P ${PORT} -b 115200 -U flash:w:$<

clean:
	$(RM) dkb.hex dkb.elf $(OBJS)

.PHONY: install clean
