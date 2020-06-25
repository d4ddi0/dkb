CC=avr-gcc
OBJCOPY=avr-objcopy
MCU := atmega32u4

CFLAGS=-Os -DF_CPU=16000000UL -mmcu=$(MCU)

PORT=/dev/ttyACM0

OBJS := main.o

dkb.hex: dkb.elf
	$(OBJCOPY) -O ihex -R .eeprom $< $@

dkb.elf: $(OBJS)
	$(CC) -mmcu=$(MCU) -o $@ $^

install: dkb.hex
	./avrdude_wrap.py -c avr109 -P $(PORT) -p $(MCU) -b 57600 -U flash:w:$<:i

clean:
	$(RM) dkb.hex dkb.elf $(OBJS)

.PHONY: install clean
