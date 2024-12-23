
ticker_list = ["AAPL", "GOOGL", "MSFT", "AMZN", "TSLA", "FB", "NVDA", "PYPL", "INTC", "CSCO",
"ADBE", "NFLX", "ORCL", "IBM", "AMD", "QCOM", "CRM", "TXN", "AVGO", "MU",
"TWTR", "SHOP", "SQ", "BA", "DIS", "JNJ", "WMT", "PG", "HD", "V",
"JPM", "UNH", "MA", "BAC", "XOM", "CVX", "T", "PFE", "KO", "PEP",
"LLY", "ABBV", "MRK", "COST", "NKE", "DHR", "UPS", "MS", "GS", "BLK",
"SPGI", "AMGN", "BMY", "CAT", "MMM", "GE", "F", "GM", "AZN", "NFLX"
"BABA", "TSM", "SNOW", "PLTR", "ROKU", "UBER", "LYFT", "SQM", "SPOT", "ZM",
"DOCU", "DDOG", "TEAM", "OKTA", "WDAY", "PANW", "CRWD", "ZS", "MDB", "NET",
"ETSY", "FSLR", "SEDG", "ENPH", "RUN", "BE", "BLNK", "EVGO", "LCID", "RIVN",
"NIO", "XPEV", "LI", "ARKK", "ARKG", "ARKF", "ARKQ", "ARKW", "SPCE", "GME",
"AMC", "BB", "NOK", "CPNG", "JD", "NTES", "TCEHY", "BIDU", "PDD", "SE",  "ABT",
"ADBE", "ADP", "ALL", "AMGN", "APD", "AVGO", "AXP", "BA", "BBY",
"BK", "BLK", "BMY", "CAT", "C", "CMCSA", "CME", "COST", "CVS", "CVX",
"DHR", "DIS", "DOW", "DUK", "EL", "EMR", "EXC", "FDX", "GD", "GE",
"GILD", "GM", "GS", "HAL", "HD", "HON", "IBM", "ICE", "JNJ", "JPM",
"KHC", "KMB", "KO", "KR", "LLY", "LMT", "LOW", "MCD", "MMM", "MO",
"MRK", "MS", "NFLX", "NKE", "NOC", "NOW", "ORCL", "PEP", "PFE", "PG",
"PLD", "PM", "QCOM", "RTX", "SBUX", "SCHW", "SHW", "SLB", "SO", "SPGI",
"T", "TGT", "TJX", "TMO", "TMUS", "TRV", "TXN", "UNH", "UNP", "UPS",
"USB", "V", "VLO", "VZ", "WBA", "WFC", "WMT", "XOM", "ZTS", "A",
"ABMD", "ACN", "AEE", "AEP", "AFL", "AIG", "AIZ", "AJG", "AKAM", "ALB",
"ALK", "ALXN", "AMCR", "AME", "AMP", "AMT", "ANET", "ANSS", "ANTM", "AON",
"AOS", "APA", "APTV", "ARE", "ATO", "ATVI", "AVB", "AVY", "AWK", "AZO",
"BAX", "BBWI", "BIO", "BKR", "BXP", "CDNS", "CE", "CHD", "CHRW", "CHTR",
"CL", "CLX", "CMS", "CNC", "COF", "CTAS", "CTLT", "CTSH", "CTVA", "DG"
"ACGL", "ADSK", "AEE", "AER", "AES", "AIZ", "AKR", "ALB", "ALLE", "ALNY",
"ALXN", "AMG", "AMP", "AN", "APO", "AQUA", "ARE", "ARGX", "ARNC", "ASH",
"ATO", "AXON", "BKI", "BRO", "BXP", "CACC", "CAH", "CARR", "CBRE", "CCI",
"CCK", "CE", "CERN", "CF", "CFR", "CHDN", "CHKP", "CHRW", "CINF", "CMA",
"CNP", "COG", "COKE", "COO", "CPT", "CR", "CRL", "CUBE", "CUZ", "CZR",
"DAL", "DD", "DFS", "DGX", "DLTR", "DRE", "DRI", "DTE", "DVA", "ECL",
"ED", "EEFT", "EIX", "EMN", "EPAM", "EQIX", "EQR", "ESS", "ETR", "EVR",
"EW", "EXAS", "EXP", "FANG", "FDS", "FE", "FFIV", "FHB", "FIS", "FLT",
"FMC", "FRC", "FRT", "FSLY", "FTV", "GGG", "GL", "GLPI", "GPC", "GRMN",
"HBI", "HBM", "HCA", "HES", "HLT", "HOLX", "HST", "HUBB", "HUM", "IAC",
"ACI", "AEM", "AGCO", "AGR", "AIZ", "AKAM", "ALK", "ALLE", "ALNY", "AME",
"AMPH", "ANET", "AOS", "APA", "APTV", "ASML", "ATKR", "AVLR", "AXNX", "BILL",
"BJ", "BNTX", "BPMC", "BRKR", "BSX", "CDAY", "CDW", "CEQP", "CHGG", "CIEN",
"CINF", "CREE", "CRSP", "CSL", "CSX", "CUBE", "CYBR", "DAR", "DDOG", "DISH",
"DOCN", "DOX", "DPZ", "DT", "DY", "EIX", "ELAN", "EME", "ENPH", "ENS",
"ENTG", "EPAM", "EQT", "ESLT", "ETN", "EVBG", "EWBC", "EXAS", "EXPD", "FFIV",
"FIVE", "FIX", "FND", "FRO", "FTNT", "GDDY", "GEN", "GFL", "GLOB", "GLPI",
"GLW", "GMED", "GOGO", "GPN", "GRA", "GRMN", "GTLS", "GWRE", "HAE", "HAS",
"HBI", "HII", "HIMX", "HOMB", "HUBG", "IART", "ICHR", "IDXX", "IESC", "INSP",
"IOVA", "ITRI", "IVZ", "JBL", "JBHT", "JCOM", "JNPR", "KEX", "KLAC", "KRG",
"KIM", "KLIC", "KNSL", "KRG", "KTOS", "LAMR", "LAZ", "LBRT", "LECO", "LESL",
"LFUS", "LII", "LITE", "LIVN", "LMAT", "LNTH", "LOGI", "LOVE", "LSCC", "LSTR",
"LTC", "LW", "LYV", "MANH", "MASI", "MBUU", "MCHP", "MEDP", "MHO", "MIDD",
"MKSI", "MLCO", "MODV", "MOH", "MORN", "MPLX", "MSA", "MTDR", "MTN", "MUSA",
"NATI", "NCR", "NEWR", "NFE", "NGM", "NMIH", "NTRA", "NTUS", "NWL", "NWN",
"NXGN", "NXPI", "ODFL", "OGE", "OGN", "ONEM", "ONTO", "OSIS", "OZK", "PACB",
"PAR", "PBH", "PCTY", "PENN", "PINC", "PLNT", "PLUG", "PLXS", "PODD", "PRAA",
"PRFT", "PRI", "PRIM", "PRLB", "PRO", "PSTG", "PTC", "PTEN", "PWSC", "PZZA",
"QDEL", "QLYS", "RACE", "RAMP", "RCII", "RCL", "RCM", "RDN", "REYN", "RGEN",
"RGNX", "RH", "RHI", "ROG", "RPD", "RRC", "RS", "RSG", "RXO", "SABR",
"SAM", "SANM", "SATS", "SBAC", "SBLK", "SCOR", "SCPL", "SCSC", "SFL", "SHAK",
"SHOO", "SHYF", "SI", "SITC", "SIX", "SKX", "SLG", "SM", "SMCI", "SMG",
"SNDR", "SNPS", "SOFI", "SON", "SPB", "SPCE", "SPPI", "SPT", "SPSC", "SPXC",
"SSRM", "STAA", "STAG", "STC", "STNE", "SWAV", "SWX", "SYNA", "SYRS", "TBBK",
"TCBI", "TECH", "TECK", "TER", "TEX", "TGI", "TIGO", "TMHC", "TNDM", "TPH",
"TREE", "TTC", "TTGT", "TTEK", "TTOO", "TWNK", "TWST", "TXRH", "TYL", "UBSI",
"UFPI", "UGI", "UMBF", "UMPQ", "UNFI", "UNIT", "USNA", "VAPO", "VCRA", "VG",
"VGR", "VIRT", "VNDA", "VNO", "VPG", "VREX", "VRNS", "VRSK", "VRT", "VRTS",
"VSCO", "VST", "WAL", "WASH", "WDAY", "WDFC", "WEX", "WFRD", "WH", "WING",
"WIRE", "WIX", "WK", "WLK", "WOLF", "WOR", "WST", "WWD", "XLRN", "XOMA", "XYL",
"YETI", "ZBH", "ZBRA", "ZEN", "ZI", "ZLAB", "ZUMZ", "ZYXI",
"AA", "AAN", "AAP", "AAT", "AAWW", "ABEV", "ABM", "ABR", "ABSI", "ACA", 
"ACCD", "ACHC", "ACHR", "ACIW", "ACLS", "ACM", "ACVA", "ADC", "ADMA", "ADNT",
"ADT", "AEIS", "AEL", "AER", "AGCO", "AGEN", "AGIO", "AGNC", "AGO",
"AGR", "AHCO", "AI", "AIMC", "AIR", "AIT", "AJRD", "AKR", "AKRO", "AL",
"ALBO", "ALC", "ALIT", "ALK", "ALLE", "ALSN", "ALTA", "ALTR", "ALVR", "AM",
"AMAL", "AMCX", "AME", "AMH", "AMRC", "AMRS", "AMPH", "AMSF", "AMWL", "AN",
"ANAB", "ANDE", "ANGI", "ANGO", "ANIP", "ANTE", "APA", "APAM", "APLE", "APLS",
"APOG", "APPS", "APYX", "AQB", "AQMS", "AQUA", "AR", "ARCB", "ARCH", "ARCO",
"ARDX", "ARES", "ARGX", "ARI", "ARIS", "ARLO", "ARMK", "ARNC", "ARQT", "ARRY",
"ARVN", "ASAN", "ASB", "ASGN", "ASH", "ASIX", "ASO", "ASTE", "ASX", "ATEN",
"ATGE", "ATHM", "ATI", "ATKR", "ATNX", "ATSG", "ATUS", "ATVI", "AUB", "AUBN",
"AUDC", "AVA", "AVAH", "AVAV", "AVID", "AVNS", "AVNT", "AVRO", "AVT", "AVYA",
"AWI", "AXNX", "AXS", "AXTA", "AY", "AYI", "AYX", "AZEK", "AZPN", "AZUL",
"BAND", "BANF", "BANR", "BAX", "BBAR", "BBBY", "BBIO", "BBWI", "BCLI", "BCO",
"BDC", "BDN", "BECN", "BFIN", "BFS", "BG", "BGCP", "BGS", "BHF", "BHLB",
"BIG", "BIIB", "BIO", "BJ", "BKD", "BKH", "BKI", "BLMN", "BLU", "BLUE",
"BMI", "BMRN", "BMY", "BOH", "BOOT", "BPMC", "BR", "BRBR", "BRKS", "BRKR",
"BRO", "BRSP", "BRX", "BSAC", "BSET", "BSM", "BSX", "BTBT", "BXC", "BXP",
"BYND", "CABO", "CAC", "CADE", "CAG", "CAH", "CAKE", "CAL", "CARS", "CASY",
"CATY", "CBAY", "CBU", "CBZ", "CC", "CCL", "CCOI", "CCS", "CCXI", "CDNA",
"CDW", "CDXS", "CDZI", "CEA", "CEIX", "CELH", "CERE", "CERS", "CFX", "CG",
"CGNX", "CHCO", "CHE", "CHRS", "CHWY", "CIG", "CIM", "CINF", "CLDT", "CLF"
"CMS", "CNA", "CNC", "CNDT", "CNP", "CNR", "CNX", "COCO", "CODI", "COG",
"COHR", "COHU", "COKE", "COLB", "COLD", "COLL", "COMM", "CONN", "COOP", "CORR",
"CORT", "COST", "COUR", "CPE", "CPF", "CPG", "CPK", "CPLP", "CPRT", "CPT",
"CR", "CRBP", "CREE", "CRIS", "CRK", "CRL", "CRM", "CRMT", "CRNX", "CRON",
"CROX", "CRS", "CRSP", "CRTX", "CRUS", "CRVL", "CRWD", "CSGP", "CSIQ", "CSL",
"CSPR", "CSR", "CSTM", "CSWC", "CSX", "CTAS", "CTLT", "CTMX", "CTS", "CTSH",
"CTVA", "CUBI", "CUBE", "CUK", 
"CLGX", "CLH", "CLOV", "CLVT", "CMBM", "CME", "CMG", "CMLS", "CMP", "CMPR",
"CULP", "CURO", "CUTR", "CVBF", "CVI", "CVLT",
"CVNA", "CVS", "CVX", "CW", "CWEN", "CWH", "CWK", "CWST", "CX", "CXP",
"CYBR", "CYCN", "CYH", "CZR", "DAC", "DAL", "DAKT", "DAN", "DAR", "DBD",
"DBI", "DCI", "DCO", "DD", "DDS", "DE", "DEA", "DECK", "DEI", "DEN",
"DFIN", "DFS", "DG", "DGICA", "DGII", "DHI", "DHR", "DIN", "DIOD", "DIS",
"DK", "DKNG", "DLB", "DLHC", "DLR", "DLTR", "DOC", "DOCN", "DOCU", "DORM",
"DOX", "DPZ", "DQ", "DRH", "DRI", "DRQ", "DSKE", "DSP", "DTE", "DTRT",
"DUK", "DV", "DVA", "DVAX", "DVD", "DVN", "DX", "DXC", "DXCM", "DY",
"EAF", "EAT", "EBAY", "EBS", "EBTC", "EC", "ECHO", "ECOL", "ECOM", "ED",
"EDIT", "EDR", "EDU", "EEX", "EFC", "EFSC", "EGBN", "EGHT", "EGLE", "EGO",
"EGP", "EHC", "EIG", "EIX", "EL", "ELF", "ELMD", "ELS", "ELY", "EME",
"EMN", "EMR", "ENB", "ENLC", "ENPH", "ENS", "ENV", "EOG", "EPAM", "EPC",
"EPR", "EPRT", "EQ", "EQC", "EQH", "EQIX", "EQNR", "EQR", "EQT", "ERA",
"ERIE", "ERII", "ES", "ESAB", "ESCA", "ESE", "ESI", "ESNT", "ESRT", "ESS",
"ET", "ETN", "ETNB", "ETR", "ETSY", "EVBG", "EVC", "EVE", "EVH", "EVOP",
"EW", "EXAS", "EXC", "EXEL", "EXLS", "EXP", "EXPD", "EXPE", "EXPO", "EXPR",
"EXR", "FANG", "FARM", "FAST", "FBHS", "FBNC", "FBP", "FC", "FCBC", "FCF",
"FCN", "FCX", "FDBC", "FDP", "FDS", "FDX", "FE", "FELE", "FET", "FFBC",
"FFIN", "FFIV", "FHB", "FHI", "FHN", "FICO", "FIS", "FISI", "FISV", "FITB",
"FIVN", "FIX", "FL", "FLGT", "FLIR", "FLO", "FLR", "FLS", "FLT", "FLXN",
"FLXS", "FMC", "FNB", "FND", "FNF", "FOE", "FOXA", "FOXF", "FR", "FRC",
"FRG", "FRME", "FRPH", "FRT", "FSBW", "FSK", "FSR", "FTAI", "FTDR", "FTEK",
"FTI", "FTNT", "FULT", "FUL", "FUN", "FVCB", "FVRR", "FWRD", "G", "GABC",
"GAIA", "GAIN", "GATX", "GBCI", "GBDC", "GBIO", "GBTC", "GCMG", "GCO", "GD",
"GDDY", "GDI", "GE", "GEF", "GEOS", "GERN", "GFF", "GGAL", "GGB", "GH",
"GHL", "GHM", "GHY", "GIB", "GIL", "GILD", "GILT", "GIS", "GKOS", "GL",
"GLAD", "GLNG", "GLOP", "GLPI", "GLT", "GLW", "GME", "GMED", "GMRE", "GMS",
"GNK", "GNL", "GNRC", "GNTX", "GNW", "GOGL", "GOOG", "GOSS", "GPC", "GPI",
"GPK", "GPL", "GPRE", "GPRK", "GPS", "GRBK", "GRC", "GRFS", "GRMN", "GRWG",
"GS", "GSHD", "GSK", "GSL", "GT", "GTE", "GTHX", "GTIM", "GTN", "GTX",
"GVA", "GWW", "H", "HA", "HAE", "HAIN", "HAL", "HALL", "HALO", "HAS",
"HASI", "HAYW", "HBAN", "HBCP", "HBI", "HBNC", "HCA", "HCCI", "HCI", "HCN",
"HCSG", "HDB", "HE", "HEAR", "HEES", "HEI", "HELE", "HES", "HESM", "HFWA",
"HGV", "HHC", "HI", "HIBB", "HIFS", "HIW", "HL", "HLI", "HLIO", "HLIT",
"HLS", "HLT", "HLX", "HMC", "HMN", "HNI", "HNST", "HNP", "HOFT", "HOG",
"HOLX", "HON", "HOPE", "HOTH", "HOV", "HP", "HPE", "HPQ", "HQY", "HR",
"HRB", "HRC", "HRL", "HRTX", "HSBC", "HSIC", "HSII", "HSKA", "HST", "HSTM",
"HSY", "HTA", "HTBI", "HTGC", "HTH", "HTLD", "HTLF", "HUBG", "HUBS", "HUM",
"HUN", "HURN", "HVT", "HWBK", "HWKN", "HXL", "HY", "HYMC", "HYRE", "HZO"
"A", "AA", "AAC", "AAL", "AAN", "AAP", "AAT", "AAWW", "ABEV", "ABM",
"ABR", "ABSI", "ACA", "ACCD", "ACHC", "ACHR", "ACIW", "ACLS", "ACM", "ACVA",
"ADC", "ADMA", "ADNT", "ADT", "AEIS", "AEL", "AER", "AGCO", "AGEN", "AGIO",
"AGNC", "AGO", "AGR", "AHCO", "AI", "AIMC", "AIR", "AIT", "AJRD", "AKR",
"AKRO", "AL", "ALBO", "ALC", "ALIT", "ALK", "ALLE", "ALSN", "ALTA", "ALTR",
"ALVR", "AM", "AMAL", "AMCX", "AME", "AMH", "AMRC", "AMRS", "AMPH", "AMSF",
"AMWL", "AN", "ANAB", "ANDE", "ANGI", "ANGO", "ANIP", "ANTE", "APA", "APAM",
"APLE", "APLS", "APOG", "APPS", "APYX", "AQB", "AQMS", "AQUA", "AR", "ARCB",
"ARCH", "ARCO", "ARDX", "ARES", "ARGX", "ARI", "ARIS", "ARLO", "ARMK", "ARNC",
"ARQT", "ARRY", "ARVN", "ASAN", "ASB", "ASGN", "ASH", "ASIX", "ASO", "ASTE",
"ASX", "ATEN", "ATGE", "ATHM", "ATI", "ATKR", "ATNX", "ATSG", "ATUS", "AUB",
"AUBN", "AUDC", "AVA", "AVAH", "AVAV", "AVID", "AVNS", "AVNT", "AVRO", "AVT",
"AVYA", "AWI", "AXNX", "AXS", "AXTA", "AY", "AYI", "AYX", "AZEK", "AZPN",
"AZUL", "BAND", "BANF", "BANR", "BAX", "BBAR", "BBBY", "BBIO", "BBWI", "BCLI",
"BCO", "BDC", "BDN", "BECN", "BFIN", "BFS", "BG", "BGCP", "BGS", "BHF",
"BHLB", "BIG", "BIIB", "BIO", "BJ", "BKD", "BKH", "BKI", "BLMN", "BLU",
"BLUE", "BMI", "BMRN", "BMY", "BOH", "BOOT", "BPMC", "BR", "BRBR", "BRKS",
"BRKR", "BRO", "BRSP", "BRX", "BSAC", "BSET", "BSM", "BSX", "BTBT", "BXC",
"BXP", "BYND", "CABO", "CAC", "CADE", "CAG", "CAH", "CAKE", "CAL", "CARS",
"CASY", "CATY", "CBAY", "CBU", "CBZ", "CC", "CCL", "CCOI", "CCS", "CCXI",
"CDNA", "CDW", "CDXS", "CDZI", "CEA", "CEIX", "CELH", "CERE", "CERS", "CFX",
"CG", "CGNX", "CHCO", "CHE", "CHRS", "CHWY", "CIG", "CIM", "CINF", "CLDT",
"CLF", "CMS", "CNA", "CNC", "CNDT", "CNP", "CNR", "CNX", "COCO", "CODI",
"COG", "COHR", "COHU", "COKE", "COLB", "COLD", "COLL", "COMM", "CONN", "COOP",
"CORR", "CORT", "COST", "COUR", "CPE", "CPF", "CPG", "CPK", "CPLP", "CPRT",
"CPT", "CR", "CRBP", "CREE", "CRIS", "CRK", "CRL", "CRM", "CRMT", "CRNX",
"CRON", "CROX", "CRS", "CRSP", "CRTX", "CRUS", "CRVL", "CRWD", "CSGP", "CSIQ",
"CSL", "CSPR", "CSR", "CSTM", "CSWC", "CSX", "CTAS", "CTLT", "CTMX", "CTS",
"CTSH", "CTVA", "CUBI", "CUBE", "CUK",
"CLGX", "CLH", "CLOV", "CLVT", "CMBM",
"CME", "CMG", "CMLS", "CMP", "CMPR", "CULP", "CURO", "CUTR", "CVBF", "CVI",
"CVLT", "CVNA", "CVS", "CVX", "CW", "CWEN", "CWH", "CWK", "CWST", "CX",
"CXP", "CYBR", "CYCN", "CYH", "CZR", "DAC", "DAL", "DAKT", "DAN", "DAR",
"DBD", "DBI", "DCI", "DCO", "DD", "DDS", "DE", "DEA", "DECK", "DEI",
"DEN", "DFIN", "DFS", "DG", "DGICA", "DGII", "DHI", "DHR", "DIN", "DIOD",
"DIS", "DK", "DKNG", "DLB", "DLHC", "DLR", "DLTR", "DOC", "DOCN", "DOCU",
"DORM", "DOX", "DPZ", "DQ", "DRH", "DRI", "DRQ", "DSKE", "DSP", "DTE",
"DTRT", "DUK", "DV", "DVA", "DVAX", "DVD", "DVN", "DX", "DXC", "DXCM",
"DY", "EAF", "EAT", "EBAY", "EBS", "EBTC", "EC", "ECHO", "ECOL", "ECOM",
"ED", "EDIT", "EDR", 
"EDU", "EEFT", "EEX", "EFC", "EFSC", "EGBN", "EGHT", "EGLE", "EGO", "EGP",
"EHC", "EIG", "EIX", "EL", "ELF", "ELMD", "ELS", "ELY", "EME", "EMN",
"EMR", "ENB", "ENLC", "ENPH", "ENS", "ENV", "EOG", "EPAM", "EPC", "EPR",
"EPRT", "EQ", "EQC", "EQH", "EQIX", "EQNR", "EQR", "EQT", "ERA", "ERIE",
"ERII", "ES", "ESAB", "ESCA", "ESE", "ESI", "ESNT", "ESRT", "ESS", "ET",
"ETN", "ETNB", "ETR", "ETSY", "EVBG", "EVC", "EVE", "EVH", "EVOP", "EW",
"EXAS", "EXC", "EXEL", "EXLS", "EXP", "EXPD", "EXPE", "EXPO", "EXPR", "EXR",
"FANG", "FARM", "FAST", "FBHS", "FBNC", "FBP", "FC", "FCBC", "FCF", "FCN",
"FCX", "FDBC", "FDP", "FDS", "FDX", "FE", "FELE", "FET", "FFBC", "FFIN",
"FFIV", "FHB", "FHI", "FHN", "FICO", "FIS", "FISI", "FISV", "FITB", "FIVN",
"FIX", "FL", "FLGT", "FLIR", "FLO", "FLR", "FLS", "FLT", "FLXN", "FLXS",
"FMC", "FNB", "FND", "FNF", "FOE", "FOXA", "FOXF", "FR", "FRC", "FRG",
"FRME", "FRPH", "FRT", "FSBW", "FSK", "FSR", "FTAI", "FTDR", "FTEK", "FTI",
"FTNT", "FULT", "FUL", "FUN", "FVCB", "FVRR", "FWRD", "G", "GABC", "GAIA",
"GAIN", "GATX", "GBCI", "GBDC", "GBIO", "GBTC", "GCMG", "GCO", "GD", "GDDY",
"GDI", "GE", "GEF", "GEOS", "GERN", "GFF", "GGAL", "GGB", "GH", "GHL",
"GHM", "GHY", "GIB", "GIL", "GILD", "GILT", "GIS", "GKOS", "GL", "GLAD",
"GLNG", "GLOP", "GLPI", "GLT", "GLW", "GME", "GMED", "GMRE", "GMS", "GNK",
"GNL", "GNRC", "GNTX", "GNW", "GOGL", "GOSS", "GPC", "GPI", "GPK", "GPL",
"GPRE", "GPRK", "GPS", "GRBK", "GRC", "GRFS", "GRMN", "GRWG", "GS", "GSHD",
"GSK", "GSL", "GT", "GTE", "GTHX", "GTIM", "GTN", "GTX", "GVA", "GWW",
"H", "HA", "HAE", "HAIN", "HAL", "HALL", "HALO", "HAS", "HASI", "HAYW",
"HBAN", "HBCP", "HBI", "HBNC", "HCA", "HCCI", "HCI", "HCN", "HCSG", "HDB",
"HE", "HEAR", "HEES", "HEI", "HELE", "HES", "HESM", "HFWA", "HGV", "HHC",
"HI", "HIBB", "HIFS", "HIW", "HL", "HLI", "HLIO", "HLIT", "HLS", "HLT",
"HLX", "HMC", "HMN", "HNI", "HNST", "HNP", "HOFT", "HOG", "HOLX", "HON",
"HOPE", "HOTH", "HOV", "HP", "HPE", "HPQ", "HQY", "HR", "HRB", "HRC",
"HRL", "HRTX", "HSBC", "HSIC", "HSII", "HSKA", "HST", "HSTM", "HSY", "HTA",
"HTBI", "HTGC", "HTH", "HTLD", "HTLF", "HUBG", "HUBS", "HUM", "HUN", "HURN",
"HVT", "HWBK", "HWKN", "HXL", "HY", "HYMC", "HYRE", "HZO", "IAA", "IAC",
"IART", "IBKR", "IBM", "IBOC", "ICE", "ICHR", "ICLR", "ICON", "IDCC", "IDEX",
"IDN", "IDXX", "IESC", "IEX", "IFF", "IFIN", "IGMS", "IHRT", "IIVI", "ILMN",
"IMAX", "IMKTA", "IMMR", "IMMU", "IMRA", "INCY", "INFN", "INFO", "INFY", "INGN",
"INM", "INMD", "INN", "INSG", "INST", "INT", "INTA", "INTC", "INTU", "INVA",
"INVE", "INVH", "IONS", "IOVA", "IP", "IPAR", "IPG", "IPGP", "IQV", "IR",
"IRBT", "IRDM", "IREN", "IRMD", "IRTC", "IRWD", "ISBC", "ISRG", "IT", "ITCI",
"ITGR", "ITI", "ITRI", "ITT", "ITW", "IVC", "IVR", "IVZ", "IX", "JACK",
"JAZZ", "JBGS", "JBL", "JBHT", "JCI", "JEF", "JJSF", "JKHY", "JLL", "JMAC",
"JOUT", "JPM", "JRVR", "JVA", "JWN", "KAI", "KALU", "KAMN", "KBAL", "KDP",
"KE", "KELYA", "KEM", "KEY", "KEYS", "KFY", "KHC", "KIM", "KIND", "KINS",
"KINZ", "KIRK", "KL", "KLIC", "KLAC", "KMB", "KMI", "KMPR", "KMT", "KMX",
"KN", "KNSL", "KNTK", "KNX", "KO", "KOP", "KOPN", "KOS", "KPTI", "KR",
"KRC", "KRG", "KSS", "KTB", "KTOS", "KURA", "KW", "KWR", "L", "LABL",
"LAC", "LAD", "LADR", "LAKE", "LAMR", "LANC", "LAND", "LARK", "LAUR", "LAWS",
"LAZ", "LBRT", "LC", "LCID", "LCII", "LDL", "LDOS", "LEA", "LECO", "LEE",
"LEG", "LEJU", "LEN", "LES", "LESL", "LEVI", "LFUS", "LFT", "LGCY", "LGIH",
"LGND", "LH", "LHX", "LI", "LII", "LILA", "LIM", "LIN", "LINC", "LIND"
"LITE", "LIVN", "LKQ", "LL", "LLEX", "LLNW", "LLO", "LLY", "LMAT", "LMT",
"LNC", "LNG", "LNN", "LNT", "LNTH", "LOCO", "LOGI", "LOOP", "LOVE", "LOW",
"LPG", "LPLA", "LPSN", "LPX", "LQDT", "LRCX", "LSCC", "LSTR", "LSXMA", "LSXMB",
"LSXMK", "LTBR", "LTRPA", "LTRPB", "LUB", "LULU", "LUMN", "LUNA", "LUV", "LVS",
"LW", "LWAY", "LX", "LXFR", "LXP", "LYB", "LYFT", "LYG", "LYTS", "LYV",
"M", "MA", "MAA", "MAC", "MAIN", "MAN", "MANH", "MANT", "MAR", "MAS",
"MAT", "MATW", "MAV", "MAXR", "MBI", "MBOT", "MBUU", "MC", "MCB", "MCD",
"MCEP", "MCFT", "MCHP", "MCK", "MCO", "MCRB", "MCRI", "MCS", "MCY", "MD",
"MDB", "MDLZ", "MDP", "MDRX", "MDT", "MDU", "MDWD", "MDXG", "MED", "MEDP",
"MEDS", "MEET", "MEG", "MEI", "MEIP", "MELI", "MEOH", "MERC", "MESA", "MET",
"MFC", "MFGP", "MFH", "MFIN", "MFLX", "MFM", "MG", "MGEE", "MGI", "MGIC",
"MGM", "MGNX", "MGPI", "MGRC", "MGTX", "MGY", "MHH", "MHK", "MHLD", "MHO",
"MIC", "MICR", "MIK", "MIME", "MIR", "MITK", "MITT", "MIY", "MKC", "MKL",
"MKSI", "MKTX", "MLI", "MLM", "MLNK", "MLP", "MLR", "MLSS", "MLVF", "MMC",
"MMP", "MMS", "MMSI", "MMYT", "MN", "MNKD", "MNOV", "MNRL", "MNSB", "MNSF",
"MNST", "MO", "MOD", "MODN", "MOH", "MOLN", "MOS", "MOV", "MP", "MPAA",
"MPB", "MPC", "MPLX", "MPWR", "MQ", "MR", "MRAM", "MRCC", "MRCY", "MREO",
"MRIN", "MRK", "MRLN", "MRO", "MRVI", "MRVL", "MS", "MSA", "MSBI", "MSC",
"MSCI", "MSFT", "MSGE", "MSGS", "MSI", "MSM", "MSON", "MSTR", "MSVB", "MT",
"MTB", "MTCH", "MTDR", "MTG", "MTH", "MTLS", "MTN", "MTOR", "MTR", "MTRN",
"MTRX", "MTSC", "MTW", "MTX", "MU", "MUDS", "MUR", "MUSA", "MVIS", "MVO",
"MX", "MXC", "MXIM", "MYE", "MYGN", "MYMD", "MYOV", "MYRG", "MYTE", "NABL",
"NAII", "NAK", "NAVI", "NBHC", "NBIX", "NBN", "NBR", "NBRV", "NBTB", "NBW",
"NBY", "NC", "NCA", "NCBS", "NCLH", "NCMI", "NCNO", "NCR", "NCSM", "NDAQ",
"NDLS", "NDRA", "NE", "NEE", "NEM", "NEN", "NEOG", "NEON", "NEP", "NEPT",
"NET", "NETE", "NEU", "NEWR", "NEWT", "NEXT", "NFG", "NFLX", "NGG", "NGHC",
"NGHCZ", "NGM", "NGS", "NGVC", "NHC", "NHI", "NHTC", "NI", "NIC", "NICE",
"NICK", "NILE", "NIMC", "NIML", "NIMR", "NINE", "NIO", "NISN", "NIU", "NJR",
"NKE", "NKG", "NKLA", "NKN", "NKSH", "NKTR", "NL", "NLOK", "NLS", "NLY",
"NM", "NMIH", "NMK", "NMN", "NMM", "NMR", "NMRK", "NMT", "NMY", "NMZ",
"NNA", "NNBR", "NNDM", "NNI", "NNOX", "NNVC", "NNY", "NOAH", "NOC", "NODK",
"NOG", "NOK", "NOM", "NOMD", "NOTE", "NOV", "NOVA", "NOVN", "NOVT", "NOW",
"NP", "NPCE", "NPK", "NPO", "NPTN", "NR", "NRG", "NRGX", "NRIM", "NRK",
"NRO", "NRT", "NRUC", "NRZ", "NS", "NSC", "NSIT", "NSP", "NSPR", "NSYS",
"NTAP", "NTB", "NTCT", "NTES", "NTGR", "NTIC", "NTLA", "NTNX", "NTRA", "NTRS",
"NTUS", "NTWK", "NU", "NUAN", "NUE", "NURO", "NUS", "NUVA", "NUWE", "NVAX",
"NVCR", "NVDA", "NVEC", "NVEE", "NVFY", "NVGS", "NVMI", "NVNO", "NVO", "NVOS",
"NVR", "NVRO", "NVS", "NVT", "NVTA", "NVTS", "NWBI", "NWE", "NWHM", "NWL",
"NWLI", "NWN", "NWPX", "NWS", "NWSA", "NXGN", "NXPI", "NXRT", "NXST", "NXTC",
"NXTD", "NYC", "NYCB", "NYMT", "NYMX", "NYT", "NYV", "O", "OAS", "OB",
"OBCI", "OBEL", "OBI", "OBLG", "OBSV", "OBT", "OC", "OCAX", "OCFC", "OCFT",
"OCGN", "OCN", "OCSI", "OCSL", "OCUP", "OCX", "ODC", "ODFL", "ODP", "OESX",
"OFED", "OFG", "OFIX", "OGE", "OGEN", "OGI", "OHI", "OI", "OII", "OIIM",
"OKE", "OKTA", "OLB", "OLED", "OLK", "OLLI", "OLMA", "OLN", "OLP", "OM",
"OMAB", "OMC", "OMEG", "OMER", "OMEX", "OMI", "OMN", "OMQT", "OMRK", "ON",
"ONB", "ONCY", "ONEM", "ONEO", "ONEY", "ONTF", "ONTX", "ONVO", "OOMA", "OP",
"OPBK", "OPCH", "OPI", "OPINL", "OPK", "OPNT", "OPRT", "OPT", "OPTN", "OR",
"ORA", "ORAN", "ORBC", "ORCC", "ORCL", "ORG", "ORGO", "ORIC", "ORLY", "ORMP",
"ORN", "ORRF", "OSBC", "OSCR", "OSG", "OSIS", "OSK", "OSMT", "OSPN", "OSS",
"OSTK", "OSUR", "OSW", "OTEC", "OTEL", "OTEX", "OTIC", "OTIS", "OTLK", "OTRA",
"OTIS", "OTRK", "OTTR", "OUST", "OVBC", "OVID", "OVLY", "OVV", "OWL", "OXLC",
"OXM", "OXY", "OZK", "PAA", "PAAS", "PAC", "PACB", "PACK", "PACW", "PAG",
"PAGP", "PAGS", "PAHC", "PAK", "PAM", "PANL", "PANW", "PAR", "PARR", "PASG",
"PATH", "PATI", "PATK", "PAVM", "PAY", "PAYC", "PAYO", "PAYS", "PAYX", "PB",
"PBCT", "PBF", "PBFS", "PBH", "PBHC", "PBI", "PBIP", "PBLA", "PBPB", "PBR",
"PBYI", "PCAR", "PCB", "PCF", "PCG", "PCH", "PCOM", "PCRX", "PCSB", "PCT",
"PCTI", "PCTY", "PCVX", "PCYG", "PCYO", "PD", "PDCE", "PDCO", "PDD", "PDEX",
"PDFS", "PDLB", 
"PDM", "PDO", "PDOT", "PDS", "PDSB", "PEAK", "PEAR", "PEB",
"PEBK", "PEBO", "PEG", "PEGA", "PEGR", "PENN", "PEP", "PEPL", "PERF", "PERI",
"PESI", "PETQ", "PETS", "PETV", "PETZ", "PEY", "PFBC", "PFC", "PFDR", "PFE",
"PFG", "PFGC", "PFHD", "PFIE", "PFIN", "PFIS", "PFLT", "PFMT", "PFNX", "PFS",
"PFSI", "PFSW", "PG", "PGNY", "PGR", "PGRE", "PGRW", "PGRX", "PGTI", "PH",
"PHAT", "PHCF", "PHG", "PHI", "PHK", "PHM", "PHR", "PHT", "PHUN", "PHX",
"PI", "PIAI", "PICC", "PII", "PIK", "PINC", "PING", "PINS", "PIOE", "PIPR",
"PIRS", "PIXY", "PJT", "PK", "PKBK", "PKE", "PKG", "PKI", "PKOH", "PKX",
"PLAB", "PLAY", "PLCE", "PLD", "PLG", "PLL", "PLM", "PLNT", "PLOW", "PLPC",
"PLRX", "PLSE", "PLTK", "PLTR", "PLUG", "PLUS", "PLX", "PLXP", "PLXS", "PLYA",
"PRTY", "PRVB", "PRVL", "PRVR", "PRY", "PRYAM", "PRYR", "PSA", "PSAC", "PSAG",
"PSB", "PSCC", "PSCD", "PSCE", "PSCF", "PSCH", "PSCI", "PSCM", "PSCT", "PSEC",
"PSET", "PSF", "PSHG", "PSMT", "PSN", "PSNL", "PSO", "PSTG", "PSTL", "PSTV",
"PSX", "PT", "PTA", "PTC", "PTCT", "PTE", "PTEN", "PTGX", "PTH", "PTI",
"PTIC", "PTIE", "PTIX", "PTMN", "PTN", "PTNR", "PTON", "PTRA", "PTRS", "PTSI",
"PTVCA", "PUBM", "PUCK", "PUK", "PULM", "PUMP", "PUYI", "PVBC", "PVH", "PVL",
"PW", "PWFL", "PWOD", "PWR", "PX", "PXD", "PXHI", "PXLW", "PYCR", "PYN",
"PYPL", "PYR", "PZC", "PZN", "PZZA", "QADA", "QADB", "QCOM", "QCRH", "QD",
"QDEL", "QEP", "QFIN", "QGEN", "QIWI", "QLGN", "QLI", "QLK", "QLRO", "QLS",
"QLY", "QLYS", "QMC", "QMCO", "QMG", "QNST", "QRHC", "QRTEA", "QRTEB", "QTEK",
"QTM", "QTNT", "QTRX", "QUAD", "QUBT", "QUIK", "QUMU", "QUOT", "QURE", "QVCC",
"R", "RAAS", "RACE", "RAD", "RADA", "RAIL", "RAMP", "RAND", "RAPT", "RARX",
"RAS", "RAVE", "RAVN", "RAX", "RBB", "RBBN", "RBCAA", "RBCN", "RBKB", "RBNC",
"RBT", "RC", "RCA", "RCAT", "RCEL", "RCFA", "RCG", "RCHG", "RCII", "RCKY",
"RCL", "RCON", "RCRT", "RCUS", "RDC", "RDFN", "RDHL", "RDNT", "RDN", "RDNTC",
"RDS", "RDUS", "RDVT", "RDWR", "RDY", "RE", "REAL", "REC", "REDF", "REE",
"REED", "REFR", "REG", "REGI", "REGN", "REKR", "RELY", "REN", "RENE", "RENN",
"REPH", "REPL", "RES", "RETA", "RETO", "REV", "REVB", "REX", "REXN", "REXX",
"REY", "RF", "RFI", "RFIL", "RFP", "RGA", "RGC", "RGCO", "RGEN", "RGLD",
"RGLS", "RGNX", "RGP", "RGR", "RGS", "RGT", "RH", "RHI", "RHP", "RIBT",
"RICK", "RIDE", "RIG", "RIGL", "RILY", "RILYL", "RILYZ", "RIO", "RIOT", "RIVE",
"RIVN", "RKDA", "RKLB", "RL", "RLAY", "RLGT", "RLGY", "RLI", "RLMD", "RLX",
"RM", "RMAX", "RMBS", "RMCF", "RMD", "RMED", "RMGC", "RMGCU", "RMGCV", "RMGV",
"RMO", "RMPL", "RMPLP", "RMR", "RMT", "RMTI", "RNA", "RNAZ", "RNDB", "RNDV",
"RNEM", "RNG", "RNGR", "RNLX", "RNR", "RNST", "RNWK", "ROAD", "ROBT", "ROCC",
"ROCE", "ROCK", "ROCR", "ROCRU", "ROCRW", "ROG", "ROIC", "ROIV", "ROK", "ROKU",
"AAL", "AAON", "AAP", "AAWW", "ABBV", "ABEO", "ABEV", "ABG", "ABM", "ABNB",
"ABT", "ACAD", "ACB", "ACCD", "ACH", "ACI", "ACN", "ACOR", "ADBE", "ADI",
"ADM", "ADP", "ADSK", "AEE", "AEP", "AFL", "AFRM", "AGCO", "AGEN", "AGIO",
"AGN", "AGNC", "AIG", "AIMC", "AIN", "AIR", "AJG", "AKAM", "ALB", "ALE",
"ALGN", "ALK", "ALL", "ALLE", "ALNY", "AMAT", "AMBA", "AMCX", "AMD", "AME",
"AMGN", "AMN", "AMP", "AMRC", "AMZN", "AN", "ANET", "ANSS", "AON", "AOS",
"APA", "APD", "APH", "APLE", "APPN", "APTV", "ARE", "ARGX", "ARNC", "ARR",
"ARW", "ARWR", "ASAN", "ASH", "ASML", "ASO", "ASX", "ATEN", "ATGE", "ATKR",
"ATVI", "AVA", "AVAV", "AVGO", "AVLR", "AVNT", "AVT", "AVTR", "AVY", "AXP",
"AXTA", "AYI", "AZEK", "AZN", "AZO", "BA", "BAC", "BAH", "BALL", "BAX",
"BBY", "BC", "BCE", "BCO", "BDC", "BDN", "BDX", "BE", "BEKE", "BEN",
"BEP", "BERY", "BFAM", "BG", "BGCP", "BGNE", "BGS", "BHF", "BIDU", "BIG",
"BIIB", "BIO", "BIP", "BJ", "BKE", "BKH", "BKNG", "BKR", "BL", "BLDR",
"BLK", "BLL", "BLMN", "BLUE", "BMRN", "BMI", "BMY", "BNS", "BOH", "BOOT",
"BOX", "BP", "BPOP", "BR", "BRBR", "BRC", "BRK.B", "BRKR", "BRO", "BRP",
"BSET", "BSM", "BSX", "BUD", "BURL", "BWXT", "BX", "BXP", "BYND", "C",
"CACC", "CAG", "CAH", "CAL", "CAMP", "CAR", "CARG", "CARR", "CAT", "CB",
"ROL"
"CBOE", "CBRE", "CCK", "CCL", "CCS", "CDAY", "CDK", "CDNS", "CDW", "CE",
"CEIX", "CELH", "CERN", "CF", "CFG", "CG", "CHD", "CHGG", "CHKP", "CHRW",
"CHTR", "CI", "CINF", "CIT", "CL", "CLF", "CLH", "CLNY", "CLR", "CLX",
"CMA", "CMC", "CMG", "CMI", "CMS", "CNC", "CNO", "CNP", "COF", "COHR",
"COIN", "COLM", "CONN", "COO", "COP", "COST", "CPE", "CPG", "CQP", "CR",
"CRBP", "CRL", "CRM", "CRON", "CRS", "CRSP", "CRTO", "CSCO", "CSIQ", "CSL",
"CSX", "CTAS", "CTLT", "CTMX", "CTSH", "CTVA", "CUBI", "CUBE", "CVAC", "CVE",
"CVNA", "CVS", "CVX", "CW", "CWH", "CWT", "CYBR", "CYH", "D", "DAL",
"DD", "DDD", "DDS", "DE", "DEA", "DECK", "DEI", "DEN", "DG", "DGICA",
"DGII", "DHI", "DHR", "DIOD", "DIS", "DISH", "DLB", "DLHC", "DLR", "DLTR",
"DOCN", "DOX", "DPZ", "DQ", "DRI", "DRQ", "DSGX", "DTE", "DUK", "DV",
"DVA", "DVN", "DXC", "DXCM", "DY", "EA", "EAF", "EAT", "EBAY", "EBS",
"ECL", "ED", "EDIT", "EDU", "EEX", "EFC", "EGHT", "EGL", "EGP", "EHC",
"EIX", "EL", "ELF", "ELS", "EME", "EMN", "EMR", "ENB", "ENDP", "ENPH",
"EOG", "EPAM", "EPC", "EPR", "EQIX", "EQNR", "EQR", "EQX", "ERIC", "ES",
"ESS", "ET", "ETN", "ETR", "ETSY", "EVBG", "EVER", "EVRI", "EVT", "EW",
"EXAS", "EXC", "EXEL", "EXPD", "EXPE", "EXR", "F", "FANG", "FAST", "FBHS",
"FDP", "FE", "FFIN", "FHI", "FIS", "FISV", "FITB", "FIX", "FL", "FLGT",
"FLO", "FLR", "FLS", "FLT", "FMC", "FNB", "FND", "FNF", "FOE", "FOXA",
"FR", "FRC", "FRT", "FSLY", "FTNT", "FTV", "FULT", "FUL", "FWRD", "G",
"GATX", "GBDC", "GBIO", "GBTC", "GCI", "GCMG", "GE", "GEF", "GERN", "GFF",
"GGAL", "GGB", "GILD", "GIS", "GKOS", "GL", "GLNG", "GLPI", "GLT", "GLW",
"GM", "GME", "GNRC", "GOOG", "GPC", "GPI", "GPN", "GPS", "GRMN", "GRTX",
"GS", "GSHD", "GT", "GTIM", "GTLB", "GTS", "GTT", "GWW", "HAL", "HAS",
"HBAN", "HBI", "HCA", "HCCI", "HCSG", "HDB", "HE", "HEI", "HES", "HFC",
"HGV", "HHC", "HI", "HIBB", "HIG", "HII", "HL", "HLI", "HLT", "HMC",
"HOLX", "HON", "HPE", "HPQ", "HRB", "HRL", "HRTX", "HSBC", "HSIC", "HSKA",
"HST", "HUBG", "HUM", "HUN", "HWM", "HXL", "HY", "HZNP", "IAC", "IART",
"IBKR", "IBM", "ICE", "ICHR", "IDEX", "IDN", "IDXX", "IFF", "IGMS", "IHRT"
"PBT", "PBYI", "PCAR", "PCH", "PCG", "PCTY", "PD", "PDCE", "PDEX", "PDFS",
"PEAK", "PEB", "PEGA", "PEG", "PENN", "PEP", "PERI", "PETS", "PFE", "PFG",
"PFGC", "PFLT", "PG", "PGNY", "PGR", "PGTI", "PH", "PHAT", "PHD", "PHG",
"PHI", "PHM", "PI", "PINS", "PIPR", "PJT", "PK", "PKE", "PKG", "PKI",
"PLAB", "PLAY", "PLCE", "PLD", "PLMR", "PLNT", "PLOW", "PLTR", "PLUG", "PLXS",
"PM", "PMT", "PNC", "PNFP", "PNM", "PNR", "PNTG", "PODD", "POLY", "POOL",
"POR", "POST", "PPBI", "PPC", "PPG", "PPL", "PRGO", "PRI", "PRIM", "PRLB",
"PRMW", "PRO", "PROV", "PRTA", 
"PRVB", "PSA", "PSB", "PSMT", "PSN", "PTC",
"PTEN", "PTGX", "PTRA", "PTRY", "PVH", "PVL", "PWFL", "PWR", "PX", "PXD",
"PYPL", "QCOM", "QLYS", "QRTEA", "QSR", "QTWO", "QUAD", "QUOT", "QURE", "RACE",
"RAD", "RAMP", "RBA", "RBC", "RBGLY", "RBLX", "RC", "RCL", "RCM", "RDN",
"RDWR", "RE", "REAL", "REG", "REGN", "RENN", "REPH", "REPL", "RES", "REV",
"RFP", "RGA", "RGEN", "RGLD", "RGS", "RH", "RHI", "RHP", "RIOT", "RJF",
"RL", "RLGT", "RLGY", "RLX", "RMAX", "RMD", "RMED", "RMR", "RMTI", "RNA",
"RNG", "RNGR", "RNR", "ROAD", "ROG", "ROKU", "ROL", "ROP", "ROST", "RPAI",
"RPM", "RRC", "RRD", "RS", "RSG", "RST", "RSYS", "RTLR", "RTX", "RVLV",
"RVNC", "RVP", "RWGE", "RY", "RYAAY", "RYAM", "RYI", "RYN", "SAFT", "SAGE",
"SAIA", "SAIC", "SATS", "SAVA", "SAVE", "SB", "SBAC", "SBH", "SBRA", "SBSW",
"SC", "SCCO", "SCHN", "SCHW", "SCI", "SCL", "SCS", "SDGR", "SDPI", "SE",
"SEDG", "SEE", "SEEL", "SEM", "SENS", "SF", "SFBC", "SFE", "SFL", "SFM",
"SFS", "SGEN", "SGH", "SH", "SHAK", "SHEN", "SHLS", "SHO", "SHOP", "SHW",
"SIFY", "SIG", "SIGI", "SIKA", "SILK", "SINA", "SITC", "SIX", "SJI", "SJM",
"SJT", "SKX", "SKYW", "SLAB", "SLB", "SLCA", "SLF", "SLG", "SLGN", "SLM",
"SLN", "SM", "SMCI", "SMG", "SMH", "SMP", "SMPL", "SMRT", "SMTC", "SNAP",
"SNDL", "SNDX", "SNY", "SO", "SOVO", "SP", "SPCE", "SPGI", "SPNS", "SPOT",
"SPR", "SPT", "SPWR", "SQ", "SQM", "SR", "SRPT", "SRRE", "SSB", "SSD",
]