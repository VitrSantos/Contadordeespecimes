antoceros = hepaticas = musgos = 0
print('Digite "fim" após inserir todas as famílias desejadas.')
print('-'*40)
while True:
    familia = str(input('Insira o nome da família: ')).strip().upper()
    if familia == 'FIM':
        break
    if familia == 'ANTHOCEROTACEAE' or familia == 'DENDROCEROTACEAE' or familia == 'NOTOTHYLADACEAE' or familia == 'PHYMATOCEROTACEAE':
        antoceros += 1
    elif familia == 'ACROBOLBACEAE' or familia == 'ADELANTHACEAE' or familia == 'ANEURACEAE' or familia == 'ARNELLIACEAE' or familia == 'AYTONIACEAE' or familia == 'BALANTIOPSIDACEAE'  or familia == 'CALYPOGEIACEAE'  or familia == 'CEPHALOZIACEAE' or familia == 'CEPHALOZIELLACEAE' or familia == 'CHONECOLEACEAE' or familia == 'CORSINIACEAE' or familia == 'CYATHODIACEAE' or familia == 'DUMORTIERACEAE' or familia == 'FOSSOMBRONIACEAE' or familia == 'FRULLANIACEAE' or familia == 'GEOCALYCACEAE' or familia == 'GYMNOMITRIACEAE' or familia == 'HERBERTACEAE' or familia == 'JAMESONIELLACEAE' or familia == 'JUNGERMANNIACEAE' or familia == 'LEJEUNEACEAE' or familia == 'LEPICOLEACEAE' or familia == 'LEPIDOZIACEAE' or familia == 'LOPHOCOLEACEAE' or familia == 'LUNULARIACEAE' or familia == 'MARCHANTIACEAE' or familia == 'METZGERIACEAE' or familia == 'MONOCLEACEAE' or familia == 'OXYMITRACEAE' or familia == 'PALLAVICINIACEAE' or familia == 'PALLAVICINIACEAE' or familia == 'PELLIACEAE' or familia == 'PLAGIOCHILACEAE' or familia == 'PLEUROZIACEAE' or familia == 'PORELLACEAE' or familia == 'RADULACEAE' or familia == 'RICCIACEAE' or familia == 'SCAPANIACEAE' or familia == 'SPHAEROCARPACEAE' or familia == 'TARGIONIACEAE' or familia == 'TRICHOCOLEACEAE':
        hepaticas += 1
    elif familia == 'ADELOTHECIACEAE' or familia == 'AMBLYSTEGIACEAE' or familia == 'ANDREAEACEAE' or familia == 'ANOMODONTACEAE' or familia == 'ARCHIDIACEAE' or familia == 'AULACOMNIACEAE' or familia == 'BARTRAMIACEAE' or familia == 'BRACHYTHECIACEAE' or familia == 'RUCHIACEAE' or familia == 'BRYACEAE' or familia == 'CALLIERGONACEAE' or familia == 'CALYMPERACEAE' or familia == 'CATAGONIACEAE' or familia == 'CRYPHAEACEAE' or familia == 'DALTONIACEAE' or familia == 'DICRANACEAE' or familia == 'DIPHYSCIACEAE' or familia == 'DITRICHACEAE' or familia == 'ENTODONTACEAE' or familia == 'EPHEMERACEAE' or familia == 'ERPODIACEAE' or familia == 'EUSTICHIACEAE' or familia == 'FABRONIACEAE' or familia == 'FISSIDENTACEAE' or familia == 'FONTINALACEAE' or familia == 'FUNARIACEAE' or familia == 'GRIMMIACEAE' or familia == 'HEDWIGIACEAE' or familia == 'HELICOPHYLLACEAE' or familia == 'HOOKERIACEAE' or familia == 'HYDROPOGONACEAE' or familia == 'HYLOCOMIACEAE' or familia == 'HYPNACEAE' or familia == 'HYPOPTERYGIACEAE' or familia == 'LEMBOPHYLLACEAE' or familia == 'LEPYRODONTACEAE' or familia == 'LESKEACEAE' or familia == 'LEUCOBRYACEAE' or familia == 'LEUCODONTACEAE' or familia == 'LEUCOMIACEAE' or familia == 'METEORIACEAE' or familia == 'MNIACEAE' or familia == 'MYRINIACEAE' or familia == 'NECKERACEAE' or familia == 'ORTHODONTIACEAE' or familia == 'ORTHOTRICHACEAE' or familia == 'PHYLLODREPANIACEAE' or familia == 'PHYLLOGONIACEAE' or familia == 'PILOTRICHACEAE' or familia == 'PLAGIOTHECIACEAE' or familia == 'POLYTRICHACEAE' or familia == 'POTTIACEAE' or familia == 'PRIONODONTACEAE' or familia == 'PTERIGYNANDRACEAE' or familia == 'PTEROBRYACEAE' or familia == 'PTYCHOMITRIACEAE' or familia == 'PTYCHOMNIACEAE' or familia == 'PYLAISIADELPHACEAE' or familia == 'RACOPILACEAE' or familia == 'REGMATODONTACEAE' or familia == 'RHABDOWEISIACEAE' or familia == 'RHACHITHECIACEAE' or familia == 'RHACOCARPACEAE' or familia == 'RHIZOGONIACEAE' or familia == 'RIGODIACEAE' or familia == 'RUTENBERGIACEAE' or familia == 'SELIGERIACEAE' or familia == 'SEMATOPHYLLACEAE' or familia == 'SPHAGNACEAE' or familia == 'SPLACHNACEAE' or familia == 'SPLACHNOBRYACEAE' or familia == 'STEREOPHYLLACEAE' or familia == 'SYMPHYODONTACEAE' or familia == 'THUIDIACEAE':
        musgos += 1
print(f'-'*40, f'\nO número de espécimes de Antóceros é: {antoceros}\nO número de espéciems de Hepáticas é: {hepaticas}\nO número de Musgos é: {musgos}')