VEDO = read.csv("edit_blabla.csv", sep= ";")
VEDO$V0_Geburtsdatum <- sub("^", 11, VEDO$V0_Geburtsdatum )
VEDO$V0_Geburtsdatum <-as.numeric(VEDO$V0_Geburtsdatum)


write.csv2(VEDO,"VEEDO.csv")

str(VEDO$V0_Geburtsdatum)



df <- transform(VEDO, V0_Geburtsdatum = as.Date(as.character(V0_Geburtsdatum), "%Y%m%d"))
