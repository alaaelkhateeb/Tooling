
include config.mk

FinalTargetName=MasterApplication.exe

allObjs = $(allSrcs:.c=.o)
allDeps = $(allSrcs:.c=.d)
allGen = $(allSrcs:.c=.o)
allGen += $(allSrcs:.c=.d)
allGen += $(FinalTargetName)
$(FinalTargetName) : CFLAG = 
$(allObjs): CFLAG = -c
$(allDeps): CFLAG = -MM
file = progress.txt

$(FinalTargetName) : $(allObjs) 
	@$(CC) $(CFLAG) $^ -o $@ 
	@cmd /C "progress.bat"
	@cmd /C echo 100>$(file)
	@cmd /C "progress.py cat $(file)"
	@echo ""
	@echo ""


$(allObjs) : %.o : %.c 
	@$(CC) $(CFLAG) $< -o $@
	@cmd /C "progress.bat"
	@cmd /C "progress.py cat $(file)"
	@echo ""
	@echo ""

$(allDeps) : %.d : %.c | Dependencies
	@$(CC) $(CFLAG) $< -o $@
	@copy /y $@ Dependencies


Dependencies:
	@mkdir $@

.PHONY: clean link onlyCompile depend all

clean: 
	DEL /Q $(FinalTargetName) $(allObjs) $(allDeps) Dependencies
	rmdir Dependencies
	@echo 0 > $(file)

link: 
	$(CC) $(CFLAG) $(allObjs) -o $(FinalTargetName)
	@cmd /C "progress.bat"
	@cmd /C "progress.py cat $(file)"

onlyCompile: $(allObjs)

depend: $(allDeps)

all: $(allDeps) 
	$(MAKE) $(FinalTargetName)

