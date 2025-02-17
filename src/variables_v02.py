field_map = {
    './/DatosDelCertificador/Fecha': 'DateCee',
    './/IdentificacionEdificio/ReferenciaCatastral': 'ReferenciaCatastral',
    './/IdentificacionEdificio/Provincia': 'Provincia',
    './/IdentificacionEdificio/ComunidadAutonoma': 'ComunidadAutonoma',
    './/IdentificacionEdificio/ZonaClimatica': 'ZonaClimatica',
    './/IdentificacionEdificio/TipoDeEdificio': 'TipoDeEdificio',
    './/IdentificacionEdificio/NormativaVigente': 'NormativaVigente',
    './/IdentificacionEdificio/Direccion': 'Direccion',
    './/IdentificacionEdificio/NombreDelEdificio': 'NombreDelEdificio',
    './/DatosGeneralesyGeometria/SuperficieHabitable': 'SuperficieHabitable',
    './/IdentificacionEdificio/Procedimiento': 'Procedimiento',
    './/IdentificacionEdificio/AlcanceInformacionXML': 'AlcanceInformacionXML',
    './/IdentificacionEdificio/Municipio': 'Municipio',
    './/IdentificacionEdificio/AnoConstruccion': 'YearConstruccion',
    './/DatosGeneralesyGeometria/PorcentajeSuperficieHabitableCalefactada': 'PorcentajeSuperficieHabitableCalefactada',
    './/DatosGeneralesyGeometria/DensidadFuentesInternas': 'DensidadFuentesInternas',
    './/DatosGeneralesyGeometria/Compacidad': 'Compacidad',
    './/DatosGeneralesyGeometria/VolumenEspacioHabitable': 'VolumenEspacioHabitable',
    './/DatosGeneralesyGeometria/VentilacionTotal': 'VentilacionTotal',
    './/DatosGeneralesyGeometria/DemandaDiariaACS': 'DemandaDiariaACS',
    './/DatosGeneralesyGeometria/NumeroDePlantasSobreRasante': 'NumeroDePlantasSobreRasante',
    './/DatosGeneralesyGeometria/NumeroDePlantasBajoRasante': 'NumeroDePlantasBajoRasante',
    './/DatosGeneralesyGeometria/PorcentajeSuperficieHabitableRefrigerada': 'PorcentajeSuperficieHabitableRefrigerada',
    './/DatosGeneralesyGeometria/PorcentajeSuperficieAcristalada/E': 'PorcentajeSuperficieAcristaladaE',
    './/DatosGeneralesyGeometria/PorcentajeSuperficieAcristalada/NO': 'PorcentajeSuperficieAcristaladaNO',
    './/DatosGeneralesyGeometria/PorcentajeSuperficieAcristalada/NE': 'PorcentajeSuperficieAcristaladaNE',
    './/DatosGeneralesyGeometria/PorcentajeSuperficieAcristalada/O': 'PorcentajeSuperficieAcristaladaO',
    './/DatosGeneralesyGeometria/PorcentajeSuperficieAcristalada/N': 'PorcentajeSuperficieAcristaladaN',
    './/DatosGeneralesyGeometria/PorcentajeSuperficieAcristalada/S': 'PorcentajeSuperficieAcristaladaS',
    './/DatosGeneralesyGeometria/PorcentajeSuperficieAcristalada/SO': 'PorcentajeSuperficieAcristaladaSO',
    './/DatosGeneralesyGeometria/PorcentajeSuperficieAcristalada/SE': 'PorcentajeSuperficieAcristaladaSE',
    './/Demanda/EdificioObjeto/Global': 'DemandaEdificioObjetoGlobal',
    './/Demanda/EdificioObjeto/ACS': 'DemandaEdificioObjetoACS',
    './/Demanda/EdificioObjeto/Refrigeracion': 'DemandaEdificioObjetoRefrigeracion',
    './/Demanda/EdificioObjeto/Calefaccion': 'DemandaEdificioObjetoCalefaccion',
    './/Demanda/EdificioDeReferencia/ACS': 'DemandaEdificioDeReferenciaACS',
    './/Demanda/EdificioDeReferencia/Refrigeracion': 'DemandaEdificioDeReferenciaRefrigeracion',
    './/Demanda/EdificioDeReferencia/Calefaccion': 'DemandaEdificioDeReferenciaCalefaccion',
    './/Demanda/EdificioDeReferencia/Global': 'DemandaEdificioDeReferenciaGlobal',
    './/Consumo/FactoresdePaso/FinalAPrimariaNoRenovable/GasNatural': 'FactoresdePasoFinalAPrimariaNoRenovableGasNatural',
    './/Consumo/FactoresdePaso/FinalAPrimariaNoRenovable/BiomasaOtros': 'FactoresdePasoFinalAPrimariaNoRenovableBiomasaOtros',
    './/Consumo/FactoresdePaso/FinalAPrimariaNoRenovable/GasoleoC': 'FactoresdePasoFinalAPrimariaNoRenovableGasoleoC',
    './/Consumo/FactoresdePaso/FinalAPrimariaNoRenovable/ElectricidadPeninsular': 'FactoresdePasoFinalAPrimariaNoRenovableElectricidadPeninsular',
    './/Consumo/FactoresdePaso/FinalAPrimariaNoRenovable/GLP': 'FactoresdePasoFinalAPrimariaNoRenovableGLP',
    './/Consumo/FactoresdePaso/FinalAPrimariaNoRenovable/Carbon': 'FactoresdePasoFinalAPrimariaNoRenovableCarbon',
    './/Consumo/FactoresdePaso/FinalAPrimariaNoRenovable/Biocarburante': 'FactoresdePasoFinalAPrimariaNoRenovableBiocarburante',
    './/Consumo/FactoresdePaso/FinalAPrimariaNoRenovable/BiomasaPellet': 'FactoresdePasoFinalAPrimariaNoRenovableBiomasaPellet',
    './/Consumo/FactoresdePaso/FinalAEmisiones/GasNatural': 'FactoresdePasoFinalAEmisionesGasNatural',
    './/Consumo/FactoresdePaso/FinalAEmisiones/BiomasaOtros': 'FactoresdePasoFinalAEmisionesBiomasaOtros',
    './/Consumo/FactoresdePaso/FinalAEmisiones/GasoleoC': 'FactoresdePasoFinalAEmisionesGasoleoC',
    './/Consumo/FactoresdePaso/FinalAEmisiones/ElectricidadPeninsular': 'FactoresdePasoFinalAEmisionesElectricidadPeninsular',
    './/Consumo/FactoresdePaso/FinalAEmisiones/GLP': 'FactoresdePasoFinalAEmisionesGLP',
    './/Consumo/FactoresdePaso/FinalAEmisiones/Carbon': 'FactoresdePasoFinalAEmisionesCarbon',
    './/Consumo/FactoresdePaso/FinalAEmisiones/Biocarburante': 'FactoresdePasoFinalAEmisionesBiocarburante',
    './/Consumo/FactoresdePaso/FinalAEmisiones/BiomasaPellet': 'FactoresdePasoFinalAEmisionesBiomasaPellet',
    './/Consumo/EnergiaFinalVectores/GasNatural/Calefaccion': 'ConsumoEnergiaFinalVectoresGasNaturalCalefaccion',
    './/Consumo/EnergiaFinalVectores/GasNatural/Global': 'ConsumoEnergiaFinalVectoresGasNaturalGlobal',
    './/Consumo/EnergiaFinalVectores/GasNatural/ACS': 'ConsumoEnergiaFinalVectoresGasNaturalACS',
    './/Consumo/EnergiaFinalVectores/GasNatural/Refrigeracion': 'ConsumoEnergiaFinalVectoresGasNaturalRefrigeracion',
    './/Consumo/EnergiaFinalVectores/GasNatural/Iluminacion': 'ConsumoEnergiaFinalVectoresGasNaturalIluminacion',
    './/Consumo/EnergiaFinalVectores/ElectricidadPeninsular/Calefaccion': 'ConsumoEnergiaFinalVectoresElectricidadPeninsularCalefaccion',
    './/Consumo/EnergiaFinalVectores/ElectricidadPeninsular/Global': 'ConsumoEnergiaFinalVectoresElectricidadPeninsularGlobal',
    './/Consumo/EnergiaFinalVectores/ElectricidadPeninsular/ACS': 'ConsumoEnergiaFinalVectoresElectricidadPeninsularACS',
    './/Consumo/EnergiaFinalVectores/ElectricidadPeninsular/Refrigeracion': 'ConsumoEnergiaFinalVectoresElectricidadPeninsularRefrigeracion',
    './/Consumo/EnergiaFinalVectores/ElectricidadPeninsular/Iluminacion': 'ConsumoEnergiaFinalVectoresElectricidadPeninsularIluminacion',
    './/Consumo/EnergiaFinalVectores/BiomasaOtros/Calefaccion': 'ConsumoEnergiaFinalVectoresBiomasaOtrosCalefaccion',
    './/Consumo/EnergiaFinalVectores/BiomasaOtros/Global': 'ConsumoEnergiaFinalVectoresBiomasaOtrosGlobal',
    './/Consumo/EnergiaFinalVectores/BiomasaOtros/ACS': 'ConsumoEnergiaFinalVectoresBiomasaOtrosACS',
    './/Consumo/EnergiaFinalVectores/BiomasaOtros/Refrigeracion': 'ConsumoEnergiaFinalVectoresBiomasaOtrosRefrigeracion',
    './/Consumo/EnergiaFinalVectores/BiomasaOtros/Iluminacion': 'ConsumoEnergiaFinalVectoresBiomasaOtrosIluminacion',
    './/Consumo/EnergiaFinalVectores/GasoleoC/Calefaccion': 'ConsumoEnergiaFinalVectoresGasoleoCCalefaccion',
    './/Consumo/EnergiaFinalVectores/GasoleoC/Global': 'ConsumoEnergiaFinalVectoresGasoleoCGlobal',
    './/Consumo/EnergiaFinalVectores/GasoleoC/ACS': 'ConsumoEnergiaFinalVectoresGasoleoCACS',
    './/Consumo/EnergiaFinalVectores/GasoleoC/Refrigeracion': 'ConsumoEnergiaFinalVectoresGasoleoCRefrigeracion',
    './/Consumo/EnergiaFinalVectores/GasoleoC/Iluminacion': 'ConsumoEnergiaFinalVectoresGasoleoCIluminacion',
    './/Consumo/EnergiaFinalVectores/GLP/Calefaccion': 'ConsumoEnergiaFinalVectoresGLPCalefaccion',
    './/Consumo/EnergiaFinalVectores/GLP/Global': 'ConsumoEnergiaFinalVectoresGLPGlobal',
    './/Consumo/EnergiaFinalVectores/GLP/ACS': 'ConsumoEnergiaFinalVectoresGLPACS',
    './/Consumo/EnergiaFinalVectores/GLP/Refrigeracion': 'ConsumoEnergiaFinalVectoresGLPRefrigeracion',
    './/Consumo/EnergiaFinalVectores/GLP/Iluminacion': 'ConsumoEnergiaFinalVectoresGLPIluminacion',
    './/Consumo/EnergiaFinalVectores/Carbon/Calefaccion': 'ConsumoEnergiaFinalVectoresCarbonCalefaccion',
    './/Consumo/EnergiaFinalVectores/Carbon/Global': 'ConsumoEnergiaFinalVectoresCarbonGlobal',
    './/Consumo/EnergiaFinalVectores/Carbon/ACS': 'ConsumoEnergiaFinalVectoresCarbonACS',
    './/Consumo/EnergiaFinalVectores/Carbon/Refrigeracion': 'ConsumoEnergiaFinalVectoresCarbonRefrigeracion',
    './/Consumo/EnergiaFinalVectores/Carbon/Iluminacion': 'ConsumoEnergiaFinalVectoresCarbonIluminacion',
    './/Consumo/EnergiaFinalVectores/Biocarburante/Calefaccion': 'ConsumoEnergiaFinalVectoresBiocarburanteCalefaccion',
    './/Consumo/EnergiaFinalVectores/Biocarburante/Global': 'ConsumoEnergiaFinalVectoresBiocarburanteGlobal',
    './/Consumo/EnergiaFinalVectores/Biocarburante/ACS': 'ConsumoEnergiaFinalVectoresBiocarburanteACS',
    './/Consumo/EnergiaFinalVectores/Biocarburante/Refrigeracion': 'ConsumoEnergiaFinalVectoresBiocarburanteRefrigeracion',
    './/Consumo/EnergiaFinalVectores/Biocarburante/Iluminacion': 'ConsumoEnergiaFinalVectoresBiocarburanteIluminacion',
    './/Consumo/EnergiaFinalVectores/BiomasaPellet/Calefaccion': 'ConsumoEnergiaFinalVectoresBiomasaPelletsCalefaccion',
    './/Consumo/EnergiaFinalVectores/BiomasaPellet/Global': 'ConsumoEnergiaFinalVectoresBiomasaPelletsGlobal',
    './/Consumo/EnergiaFinalVectores/BiomasaPellet/ACS': 'ConsumoEnergiaFinalVectoresBiomasaPelletsACS',
    './/Consumo/EnergiaFinalVectores/BiomasaPellet/Refrigeracion': 'ConsumoEnergiaFinalVectoresBiomasaPelletsRefrigeracion',
    './/Consumo/EnergiaFinalVectores/BiomasaPellet/Iluminacion': 'ConsumoEnergiaFinalVectoresBiomasaPelletsIluminacion',
    './/Consumo/EnergiaPrimariaNoRenovable/Calefaccion': 'ConsumoEnergiaPrimariaNoRenovableCalefaccion',
    './/Consumo/EnergiaPrimariaNoRenovable/Global': 'ConsumoEnergiaPrimariaNoRenovableGlobal',
    './/Consumo/EnergiaPrimariaNoRenovable/ACS': 'ConsumoEnergiaPrimariaNoRenovableACS',
    './/Consumo/EnergiaPrimariaNoRenovable/Refrigeracion': 'ConsumoEnergiaPrimariaNoRenovableRefrigeracion',
    './/Consumo/EnergiaPrimariaNoRenovable/Iluminacion': 'ConsumoEnergiaPrimariaNoRenovableIluminacion',
    './/EmisionesCO2/ConsumoElectrico': 'EmisionesCO2ConsumoElectrico',
    './/EmisionesCO2/TotalConsumoElectrico': 'EmisionesCO2TotalConsumoElectrico',
    './/EmisionesCO2/TotalConsumoOtros': 'EmisionesCO2TotalConsumoOtros',
    './/EmisionesCO2/Global': 'EmisionesCO2Global',
    './/EmisionesCO2/Calefaccion': 'EmisionesCO2Calefaccion',
    './/EmisionesCO2/ACS': 'EmisionesCO2ACS',
    './/EmisionesCO2/Refrigeracion': 'EmisionesCO2Refrigeracion',
    './/EmisionesCO2/Iluminacion': 'EmisionesCO2Iluminacion',
    './/Calificacion/Demanda/Calefaccion': 'CalificacionDemandaCalefaccion',
    './/Calificacion/Demanda/Refrigeracion': 'CalificacionDemandaRefrigeracion',
    './/Calificacion/Demanda/EscalaCalefaccion/A': 'CalificacionDemandaEscalaCalefaccionA',
    './/Calificacion/Demanda/EscalaCalefaccion/B': 'CalificacionDemandaEscalaCalefaccionB',
    './/Calificacion/Demanda/EscalaCalefaccion/C': 'CalificacionDemandaEscalaCalefaccionC',
    './/Calificacion/Demanda/EscalaCalefaccion/D': 'CalificacionDemandaEscalaCalefaccionD',
    './/Calificacion/Demanda/EscalaCalefaccion/E': 'CalificacionDemandaEscalaCalefaccionE',
    './/Calificacion/Demanda/EscalaCalefaccion/F': 'CalificacionDemandaEscalaCalefaccionF',
    './/Calificacion/Demanda/EscalaRefrigeracion/A': 'CalificacionDemandaEscalaRefrigeracionA',
    './/Calificacion/Demanda/EscalaRefrigeracion/B': 'CalificacionDemandaEscalaRefrigeracionB',
    './/Calificacion/Demanda/EscalaRefrigeracion/C': 'CalificacionDemandaEscalaRefrigeracionC',
    './/Calificacion/Demanda/EscalaRefrigeracion/D': 'CalificacionDemandaEscalaRefrigeracionD',
    './/Calificacion/Demanda/EscalaRefrigeracion/E': 'CalificacionDemandaEscalaRefrigeracionE',
    './/Calificacion/Demanda/EscalaRefrigeracion/F': 'CalificacionDemandaEscalaRefrigeracionF',
    './/Calificacion/EnergiaPrimariaNoRenovable/Calefaccion': 'CalificacionEnergiaPrimariaNoRenovableCalefaccion',
    './/Calificacion/EnergiaPrimariaNoRenovable/Refrigeracion': 'CalificacionEnergiaPrimariaNoRenovableRefrigeracion',
    './/Calificacion/EnergiaPrimariaNoRenovable/Iluminacion': 'CalificacionEnergiaPrimariaNoRenovableIluminacion',
    './/Calificacion/EnergiaPrimariaNoRenovable/Global': 'CalificacionEnergiaPrimariaNoRenovableGlobal',
    './/Calificacion/EnergiaPrimariaNoRenovable/EscalaGlobal/A': 'CalificacionEnergiaPrimariaNoRenovableEscalaGlobalA',
    './/Calificacion/EnergiaPrimariaNoRenovable/EscalaGlobal/B': 'CalificacionEnergiaPrimariaNoRenovableEscalaGlobalB',
    './/Calificacion/EnergiaPrimariaNoRenovable/EscalaGlobal/C': 'CalificacionEnergiaPrimariaNoRenovableEscalaGlobalC',
    './/Calificacion/EnergiaPrimariaNoRenovable/EscalaGlobal/D': 'CalificacionEnergiaPrimariaNoRenovableEscalaGlobalD',
    './/Calificacion/EnergiaPrimariaNoRenovable/EscalaGlobal/E': 'CalificacionEnergiaPrimariaNoRenovableEscalaGlobalE',
    './/Calificacion/EnergiaPrimariaNoRenovable/EscalaGlobal/F': 'CalificacionEnergiaPrimariaNoRenovableEscalaGlobalF',
    './/Calificacion/EmisionesCO2/Calefaccion': 'CalificacionEmisionesC02Calefaccion',
    './/Calificacion/EmisionesCO2/Refrigeracion': 'CalificacionEmisionesC02Refrigeracion',
    './/Calificacion/EmisionesCO2/Iluminacion': 'CalificacionEmisionesC02Iluminacion',
    './/Calificacion/EmisionesCO2/Global': 'CalificacionEmisionesC02Global',
    './/Calificacion/EmisionesCO2/EscalaGlobal/A': 'CalificacionEmisionesC02EscalaGlobalA',
    './/Calificacion/EmisionesCO2/EscalaGlobal/B': 'CalificacionEmisionesC02EscalaGlobalB',
    './/Calificacion/EmisionesCO2/EscalaGlobal/C': 'CalificacionEmisionesC02EscalaGlobalC',
    './/Calificacion/EmisionesCO2/EscalaGlobal/D': 'CalificacionEmisionesC02EscalaGlobalD',
    './/Calificacion/EmisionesCO2/EscalaGlobal/E': 'CalificacionEmisionesC02EscalaGlobalE',
    './/Calificacion/EmisionesCO2/EscalaGlobal/F': 'CalificacionEmisionesC02EscalaGlobalF',
}
