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
	./avrdude_wrap.py -c avr109 -P $(PORT) -p ATMEGA32U4 -b 57600 -U flash:w:$<

clean:
	$(RM) dkb.hex dkb.elf $(OBJS)

.PHONY: install clean
